#!/usr/bin/python
import crypt   #导入crypt模块
import time
import hashlib
class Htpasswd(object):
'''
Htpasswd use to blast password file generate by htpasswd command
'''
    def __init__(self, password_file, dictionary_file) 
        self.password_file = password_file
        self.dictionary_file = dictionary_file

    def run(self)
        with open(self.password_file, 'r') as pf:
            for msg in pf.readlines():
                username, encrypt_msg = msg.strip('\n').split(':')
                if len(encrypt_msg) == 13:
                    self.crypt(username, encrypt_msg)
                elif len(encrypt_msg) == 37:
                    self.md5(username, encrypt_msg)

    def crypt(self, username, encrypt_msg)
        'crypt function use to blast password generate by crypt encryption'
        salt = encrypt_msg[0:2]
        with open(self.dictionary_file, 'r') as df:
            for word in df.readlines():
                if crypt.crypt(word,salt) == encrypt_msg:
                    print("{0}'s password is {1}".format(username, word))
                    break

    def md5(self, username, encrypt_msg)
        'md5 function use to blast password generate by md5 encryption'
        




if __name__ == '__main__':

