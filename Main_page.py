
from flask import Blueprint,Flask,request,session,request,redirect,url_for,send_from_directory,render_template
import datetime
import mysql.connector
import json
import sys
import random
from usercode.user_code import user_code

app=Flask(__name__)
app.register_blueprint(user_code, url_prefix="/usercode")
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

@app.route('/')
def default_page():
    return redirect(url_for("home_page"))

if __name__=='__main__':
    app.run(host="0.0.0.0",port=50000)