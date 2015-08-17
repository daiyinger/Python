#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os
import time
from ftplib import FTP 
 
def ftp_up(filename = "for.py"): 
    ftp=FTP() 
    ftp.set_debuglevel(0)#打开调试级别2，显示详细信息;0为关闭调试信息 
    ftp.connect('218.83.155.184',21)#连接 
    ftp.login('daiyinger','199105')#登录，如果匿名登录则用空串代替即可 
    #print ftp.getwelcome()#显示ftp服务器欢迎信息 
    #ftp.cwd('xxx/xxx/') #选择操作目录 
    bufsize = 1024#设置缓冲块大小 
    file_handler = open(filename,'rb')#以读模式在本地打开文件 
    ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)#上传文件 
    ftp.set_debuglevel(0) 
    file_handler.close() 
    ftp.quit() 
    #print ("ftp up OK")

def ftp_del(filename = "log.txt"): 
    ftp=FTP() 
    ftp.set_debuglevel(0) 
    ftp.connect('218.83.155.184',21) 
    ftp.login('daiyinger','199105') 
    ftp.delete(filename)
    ftp.quit() 
    #print ("ftp down OK")

def find(filename):  
    return False

def ftp_find(filename = "log.txt"): 
    ftp=FTP() 
    ftp.set_debuglevel(0) 
    ftp.connect('218.83.155.184',21) 
    ftp.login('daiyinger','199105') 
    ftp_f_list = ftp.nlst()  
    if filename in ftp_f_list:
        ftp.quit()
        #print ("ftp find OK")
        return True  
    else:
        ftp.quit()
        #print ("ftp find False")
        return False     
 
def ftp_down(filename = "log.txt"):
    ftp=FTP() 
    ftp.set_debuglevel(0) 
    ftp.connect('218.83.155.184',21) 
    ftp.login('daiyinger','199105') 
    bufsize = 1024 
    localfilename = "local.txt" 
    file_handler = open(localfilename,'wb').write #以写模式在本地打开文件
    ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler,bufsize)#接收服务器上文件并写入本地文件 
    ftp.set_debuglevel(0)
    ftp.quit()
    #print ("ftp down OK")

#ftp_down("index.html")
#ftp_up("for.py")
#ftp_del("for.py")
#ftp_find("1.txt")
#ftp_down("log.txt")

sh_header = "#!/bin/sh\r\n"

running=True
while running:
    cmd = input('Enter an cmd: ')
    f = open(('cmd.o'),"w")
    #f.write(sh_header)
    f.write("sudo ")
    f.write(cmd)
    f.close()
    if ftp_find("log_out.txt"):
        ftp_del("log_out.txt")
    ftp_up('cmd.o')
    time.sleep(2)
    if ftp_find("log_out.txt"):
        ftp_down('log_out.txt') #cmd.sh log_out.txt
        fs = open('local.txt')
        lines = fs.read()
        print (lines,)
        fs.close() # close the file
        ftp_del("log_out.txt")
    
else:
    print ('The while loop is over.')
    # Do anything else you want to do here

	
