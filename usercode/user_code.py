from flask import Blueprint,Flask,request,session,request,redirect,url_for,send_from_directory,render_template
import datetime
import mysql.connector
import json
import sys
import random

user_code = Blueprint ("user_code",__name__,static_folder="static",template_folder="templates")

@user_code.route('/login',methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    #     USER_ID int,
    # NAME varchar(50),
    # EMAIL varchar(50),
    # MOBILE_NUMBER varchar(50),
    # PASSWORD varchar(50),
    # INTRODUCTION varchar(500),
    # primary key (USER_ID)
    if request.method=="POST":
        username=request.form['uname']
        password=request.form['psw']
        
        return redirect(url_for("home_page"))
    
def add_user_to_database(username,email,mobile_number,introduction,password):
    user_id=str(random.randint(0,10000))
    try:
        with mysql.connector.connect(host="localhost",user="root",password="sanket@123",database="SNS") as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"""INSERT INTO USER_DATA VALUES ('{user_id}','{username}','{email}','{mobile_number}','{introduction}','{password}');""")
                connection.commit()

    except Error as e:
        print(e)
    

@user_code.route('/register',methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    
    if request.method=="POST":
        username=request.form['uname']
        email=request.form['Email']
        mobile_number=request.form['mobile_number']
        introduction=request.form['introduction']
        password=request.form['psw']
        add_user_to_database(username,email,mobile_number,introduction,password)
        return redirect(url_for("home_page"))
