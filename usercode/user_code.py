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
    if request.method=="POST":
        username=request.form['uname']
        password=request.form['psw']
        matching_profile=check_for_existing_users_with_same_name(username)
        if len(matching_profile)==1:
            if password==matching_profile[0][4]:
                session['username']=matching_profile[0][1]
                return redirect(url_for("home_page"))
        else:
            return redirect(url_for("login"))

def check_for_existing_users_with_same_name(username):
    try:
        with mysql.connector.connect(host="localhost",user="root",password="sanket@123",database="SNS") as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"""select * from USER_DATA where name='{username}';""")
                result=cursor.fetchall()
    except Error as e:
        print(e)
    return(result)

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

@user_code.route('/delete_profile',methods=["GET","POST"])
def delete_profile():
    if request.method=="GET":
        return render_template("delete_profile.html")
    if request.method=="POST":
        username=session['username']
        matching_profile=check_for_existing_users_with_same_name(username)
        password=request.form['psw']
        if password==matching_profile[0][4]:
            delete_user_from_database(username,password)
            return redirect(url_for("home_page"))
        else:
            return redirect(url_for("delete_profile"))

def delete_user_from_database(username,password):
    try:
        with mysql.connector.connect(host="localhost",user="root",password="sanket@123",database="SNS") as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"""select * from user_data where name='{username}';""")
                result= cursor.fetchall()
                id=result[0][0]
                cursor.execute(f"""DELETE FROM post_DATA where user_id='{id}';""")
                cursor.execute(f"""DELETE FROM comment_DATA where user_id='{id}';""")
                cursor.execute(f"""DELETE FROM USER_DATA where user_id='{id}';""")
                connection.commit()
    except Error as e:
            print(e)

@user_code.route('/update_profile',methods=["GET","POST"])
def update_profile():
    username=session['username']
    user_info=check_for_existing_users_with_same_name(username)
    if request.method=="GET":
        return render_template("update_profile.html",user_info=user_info)

    if request.method=="POST":
        if request.form['uname']=="" or request.form['uname']==None:
            pass
        else:
            username=request.form['uname']
        if request.form['email']=="" or request.form['email']==None:
            email=user_info[0][2]
        else:
            email=request.form['email']
        if request.form['mobile_number']=="" or request.form['mobile_number']==None:
            mobile_number=user_info[0][3]
        else:
            mobile_number=request.form['mobile_number']
        if request.form['password']=="" or request.form['password']==None:
            password=user_info[0][4]
        else:
            password=request.form['password']
        if request.form['introduction']=="" or request.form['introduction']==None:
            introduction=user_info[0][5]
        else:
            introduction=request.form['introduction']      
        try:
            with mysql.connector.connect(host="localhost",user="root",password="sanket@123",database="SNS") as connection:
                with connection.cursor() as cursor:
                    cursor.execute(f"""UPDATE user_data 
                                        set name='{username}', email='{email}',Mobile_number='{mobile_number}',password='{introduction}',password='{introduction}'
                                        where user_id='{user_info[0][4]}';""")
        except Error as e:
            print(e)
        return redirect(url_for("home_page"))

@user_code.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for("home_page"))
