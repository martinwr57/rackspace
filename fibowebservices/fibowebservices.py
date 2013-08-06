# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

import sys, os, time, random

app = Flask(__name__)


app.debug = True


@app.route('/')
def api_root():
    return 'Welcome to the fibonacci RESTful web service!'    
       
        
@app.route('/fibonacci/<n>')
def api_fibonacci(n):
    """given n, method returns fibonacci 0 to n range"""
    result=[]
    n = int(n)
    
    if n < 0:        
        raise ValueError, "No negative number here."    
    else:               
        a, b = 0, 1
        for i in range(0,n):
            result.append(a)
            a,b, = b,a+b
    fp = open('C:\\fibowebservices\\fibonacci.xsd', 'w')
    fp.write('<?xml version="1.0" encoding="utf-8"?>\r\n')
    fp.write('<fibonacci>\r\n')
    for i,j in enumerate(result):
        fp.writelines('<value index=' '"' '%s' '"' '>' '%s' '</value>' '\r\n' % (i, j))
    fp.write('</fibonacci>\r\n')        
    fp.close()  
    return "XML message written! " + str(result) 

     
        
       
@app.route('/fibonacciup/<n>')      
def api_fibonacciup(n): # return Fibonacci series up to n
    result = []
    n = int(n)
    
    if n < 0:        
        raise ValueError, "No negative number here."    
    else:          
        a, b = 0, 1
        while b < n:
            result.append(b)
            a, b = b, a+b
        return 'Returning a fibonacci series up to ' + str(n) + '  ' + str(result)
               
    
if __name__ == '__main__':
   app.run()
  
