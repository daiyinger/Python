#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os
import time
import sys
from ftplib import FTP 
 
def ftp_up(filename,password): 
    ftp=FTP() 
    ftp.set_debuglevel(2)#打开调试级别2，显示详细信息;0为关闭调试信息 
    ftp.connect('218.83.155.184',21)#连接 
    ftp.login('daiyinger',password)#登录，如果匿名登录则用空串代替即可 
    #print ftp.getwelcome()#显示ftp服务器欢迎信息 
    ftp.cwd('upfile') #选择操作目录 
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
password = input('Please Input Password\n',)
while True:
	s = input('Please Drog File To This Window\n',)
	if s == "exit":
		break
	ftp_up(s,password)
	print ('Up ',s)


	
