#we will have all python code of main page here.
#create own htnl code files as per need and push them.
from flask import Flask,request,session,request,redirect,url_for,send_from_directory,render_template
import datetime
import mysql.connector
import json
import sys
import random
app=Flask(__name__)
app.secret_key="zonda"

@app.route('/home_page')
def home_page():  
    try:
        with mysql.connector.connect(host="localhost",user="root",password="sanket@123",database="SNS") as connection:
            with connection.cursor() as cursor:

                cursor.execute("select * from POST_DATA;")
                result= cursor.fetchall()

    except Error as e:
        print(e)
    username=None
    if 'username' in session:
        username=session['username']
    records_login_info=result
    page=render_template("Main_page.html",records=result,username=username,records_login_info=records_login_info)
    return page

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method=='GET':
        page=render_template("login.html")
        return page

    elif request.method=='POST':
        username=request.form['uname']
        password=request.form['psw']
        return redirect(url_for("home_page"))

@app.route('/new_login',methods = ['POST', 'GET'])
def new_login():
    if request.method=='GET':
        print("**************1")
        page=render_template("new_login.html")
        return page

    elif request.method=='POST':
        print("**************2")
        username=request.form['uname']
        mail=request.form['mail']
        mobile_number=request.form['mobile_number']
        password=request.form['psw']
        introduction=request.form['introduction']
        print("**************3")
        page=render_template('login.html')
        return page

@app.route('/')
def default_page():
    return redirect(url_for("home_page"))

if __name__=='__main__':
    app.run(host="0.0.0.0",port=50000)