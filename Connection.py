# -*- coding: utf-8 -*-
import re
import paramiko

class Ssh :

    def __init__(self,ip,port,username,passwd):
        self.ip = ip
        self.port = port
        self.username = username
        self.passwd = passwd
        self.ssh = paramiko.SSHClient()

    def start_connection(self):
        know_host = paramiko.AutoAddPolicy()
        self.ssh.set_missing_host_key_policy(know_host)
        self.ssh.connect(
            hostname = self.ip,
            port = self.port,
            username = self.username,
            password = self.passwd
                    )

    def stay_connection(self,command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        output_info = stdout.read().decode('utf-8')
        return output_info

    def close_connection(self):
        self.ssh.close()


def filter_data(keyword,data):
    processing = re.findall(r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})  [\w\s]{1,8}  '+keyword,data)
    return processing
