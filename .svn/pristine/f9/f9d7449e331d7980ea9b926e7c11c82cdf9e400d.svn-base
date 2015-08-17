#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os
import time
import codecs
from ftplib import FTP 
 
def ftp_up(ftp,filename): 
    bufsize = 1024#设置缓冲块大小 
    file_handler = open(filename,'rb')#以读模式在本地打开文件 
    ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)#上传文件 
    ftp.set_debuglevel(0) 
    file_handler.close() 
    #print ("ftp up OK")

def ftp_del(ftp,filename = "log.txt"): 
    ftp.delete(filename)
    #print ("ftp down OK")

def find(filename):  
    return False

def ftp_login(): 
    ftp=FTP() 
    ftp.set_debuglevel(0) 
    ftp.connect('218.83.155.184',21) 
    ftp.login('daiyinger','199105') 
    return ftp;  

def ftp_find(ftp,filename = "log.txt"): 
    ftp_f_list = ftp.nlst()  
    if filename in ftp_f_list:
        #print ("ftp find OK")
        return True  
    else:
        #print ("ftp find False")
        return False     
 
def ftp_down(ftp,filename = "log.txt"):
    bufsize = 1024 
    localfilename = "local.txt" 
    file_handler = open(localfilename,'wb').write #以写模式在本地打开文件
    ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler,bufsize)#接收服务器上文件并写入本地文件 
    ftp.set_debuglevel(0)
    #print ("ftp down OK")

def ConvertCN(s):  
	return s.encode('gb18030')  

#ftp_down("index.html")
#ftp_up("for.py")
#ftp_del("for.py")
#ftp_find("1.txt")
#ftp_down("log.txt")

sh_header = "#!/bin/sh\r\n"
ftp = ftp_login()
running=True
while running:
    cmd = input('Enter an cmd: ')
    f = open(('cmd1.o'),"w")
    #f.write(sh_header)
    f.write("sudo ")
    f.write(cmd)
    f.close()
    if ftp_find(ftp,"log_out.txt"):
        ftp_del(ftp,"log_out.txt")
    ftp_up(ftp,'cmd1.o')
    time.sleep(2)
    if ftp_find(ftp,"log_out.txt"):
        ftp_down(ftp,'log_out.txt') #cmd.sh log_out.txt
        fs =codecs.open('local.txt','r','utf-8')
        lines = fs.read()
        print (lines,)
        fs.close() # close the file
        ftp_del(ftp,"log_out.txt")
    
else:
    print ('The while loop is over.')
    # Do anything else you want to do here

	
