#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os
import time
import sys
import threading  
import socket, traceback
from ftplib import FTP

#udp_received=0
receivedContent=''

def ftp_login(): 
    ftp=FTP() 
    ftp.set_debuglevel(0) 
    ftp.connect('218.83.155.184',21) 
    ftp.login('daiyinger','199105') 
    return ftp;  
 
def ftp_up(ftp,filename): 
    bufsize = 1024#设置缓冲块大小 
    file_handler = open(filename,'rb')#以读模式在本地打开文件 
    ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)#上传文件 
    ftp.set_debuglevel(0) 
    file_handler.close() 
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

class UDP_Thread():
	host = ''
	port = 10008
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((host, port))
	print ('Start')
	ftp = ftp_login()
	while True:
		message, address = s.recvfrom(8192)
		#print ('Ups ')
		fp = open("8288stat.txt",'w')
		curTime = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime(time.time()))
		fp.write(curTime)
		receivedContent=message.decode()+"\n"
		fp.write(receivedContent)
		fp.close()
		ftp_up(ftp,'8288stat.txt')
	        
UDP_Thread().start();



	
