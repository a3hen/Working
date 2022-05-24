# -*- coding: utf-8 -*-
import re
import paramiko

class Ssh :

    def __init__(self,ip,port,username,passwd,command):
        self.ip = ip
        self.port = port
        self.username = username
        self.passwd = passwd
        self.command = command

    def method_processing_data(self):
        ssh = paramiko.SSHClient()
        know_host = paramiko.AutoAddPolicy()
        ssh.set_missing_host_key_policy(know_host)

        ssh.connect(
            hostname = self.ip,
            port = self.port,
            username = self.username,
            password = self.passwd
                    )

        stdin, stdout, stderr = ssh.exec_command(self.command)
        output_info = stdout.read().decode('utf-8')
        ssh.close()

        return output_info

def filter_data(keyword,data):
    processing_step1 = re.findall(keyword+r'([\w\W]*)'+keyword, data)[0]
    processing_step2 = re.findall(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', processing_step1)[0]
    return processing_step2

# def test(keyword,data):
#     processing_step1 = re.findall(keyword, data)
#     return processing_step1

# if __name__ == '__main__' :
#     with open("新建文本文档.txt") as f :
#         test_data = f.read()
#     jieguo = filter_data("ens192",test_data)
#     print(jieguo)
