#!/usr/bin/env python3
import re
import time
import sys
import paramiko

# 定义函数
def Monitor(HOST,PORT,USER,PASSWORD):
    # 创建SSH连接
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=HOST,port=PORT,username=USER,password=PASSWORD,timeout=5)
    ssh_shell = ssh.invoke_shell()
    # 将命令存在一个列表中
    cmds = ['','display cpu-usage\n' ]
    for cmd in cmds:
        command = ssh_shell.sendall(cmd)
        time.sleep(1)
        res = ssh_shell.recv(9999).decode().split("\r\n")
    ssh.close()
    value = []
    for line in res:
        if line.find("5 minutes") != -1:
            value += line.split()
    print("inspect_result:" + value[0].strip())

    print("script_run_status:0")
    print("script_error_info:")
    print("inspect_info:")
if __name__ == "__main__":
    Monitor(HOST,PORT,USER,PASSWORD)
