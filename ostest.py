# -*- coding: utf-8 -*-
import socket
# import subprocess
#
# proc = subprocess.Popen('ipconfig',
#                         stdin=None,
#                         stdout=subprocess.PIPE,
#                         stderr=subprocess.PIPE,
#                         shell=True
#                         )
#
# outinf = proc.stdout.read().decode('GBK')
# outerr = proc.stderr.read().decode('GBK')

class musicplayer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is  None :
            cls.instance = super().__new__(cls)

        return cls.instance
    def __init__(self):
        print("初始化")

player1 = musicplayer()
print(player1)

player2 = musicplayer()
print(player2)





