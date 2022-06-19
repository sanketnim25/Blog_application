#we will have all python code of main page here.
#create own htnl code files as per need and push them.
from flask import Flask,request,session,request,redirect,url_for,send_from_directory,render_template
import datetime
import mysql.connector
import user
import json
import sys
import random
app=Flask(__name__)
app.secret_key="zonda"

@app.route('/Home_page')
def Home_page():  
    try:
        with mysql.connector.connect(host="localhost",user="root",password="sanket@123",database="SNS") as connection:
            with connection.cursor() as cursor:

                cursor.execute("select * from POST_DATA")
                result= cursor.fetchall()

    except Error as e:
        print(e)
    username=None
    if 'username' in session:
        username=session['username']

    page=render_template("welcome_page.html",records=result,username=username)
    return page