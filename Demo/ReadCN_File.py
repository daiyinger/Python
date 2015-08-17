#!/usr/bin/env python
#coding=utf-8 
import os
import codecs

f = codecs.open('local.txt','r','utf-8')
line = f.read()
print (line,)
f.close()
