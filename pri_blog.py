from flask import Blueprint,Flask,request,session,request,redirect,url_for,send_from_directory,render_template
import datetime
from datetime import datetime
import mysql.connector
import json
import sys
import random

blog = Flask(__name__, template_folder='template')
blog.secret_key = "iamsecretkey"

@blog.route('/')
def home_page():
    return redirect(url_for("login"))
    
@blog.route('/register', methods = ["GET", "POST"])
def register():
    new_user = []
    if request.method=="GET":
        return render_template("register.html")
    
    elif request.method=="POST":
        username=request.form['username']
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']
        password=request.form['password']
        matched_username = check_for_existing_username(username)
        if len(matched_username)!=0:                                                    #username already exists
            return redirect(url_for("register"))
        else:
            new_user == add_new_user_to_database(username, name, email, password, mobile)
            session['username'] = request.form['username']
            return redirect(url_for("login"))    
        
def check_for_existing_username(username):
    query = f"""select * from user_data where username='{username}';"""
    try:
        with mysql.connector.connect(host="localhost",user="root",password="Mysql*24", database = "pml") as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result=cursor.fetchall()
    except Error as e:
        print(e)
    return(result)
     
def add_new_user_to_database(username, name, email, password, mobile):
    userId = str(random.randint(0,10000))
    query1 = f"""insert into user_data(userId, username, name, email, password, mobile) values ("{userId}", "{username}", "{name}", "{email}", "{password}", "{mobile}");"""
    try:
        with mysql.connector.connect(host="localhost",user="root",password="Mysql*24", database = "pml") as connection:
            with connection.cursor() as cursor:
                cursor.execute(query1)
                connection.commit();
    except Error as e:
        print(e)
    
@blog.route('/login' , methods=["GET", "POST"])
def login():
    global user_Id
    if request.method == "GET":
        page = render_template("login.html")
        return page
    elif request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        matched_profile = check_for_same_username(username)
        if len(matched_profile)==1:
            if password==matched_profile[0][4]:
                print(username)
                session['username']=matched_profile[0][1]
                user_Id = matched_profile[0][0]
                return redirect(url_for("timeline"))
            else:
                return redirect(url_for("login"))
        else:
            return redirect(url_for("register"))
                
def check_for_same_username(username):
    query = f"""select * from user_data where username='{username}';"""
    try:
        with mysql.connector.connect(host="localhost",user="root",password="Mysql*24", database = "pml") as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result=cursor.fetchall()
    except Error as e:
        print(e)
    return(result)
   
    

@blog.route('/timeline',methods = ["GET", "POST"])
def timeline():
    result = []
    try:
        with mysql.connector.connect(host="localhost",user="root",password="Mysql*24", database = "pml") as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT u.userId, p.authorId, u.name, p.postTitle, p.content, p.currentdate FROM user_data u INNER JOIN post_data p ON u.userId = p.authorId;")
                result=cursor.fetchall()
    except Error as e:
        print(e)
    if 'username' in session:
        username = session['username']
    return render_template("timeline.html", result = result, username = username)
    
    

@blog.route('/comment', methods = ["GET", "POST"])
def comment():
    if request.method=="GET":
        return render_template("comment.html")
    
    elif request.method=="POST":
        return render_template("comment.html")

    
@blog.route('/profile', methods=["GET", "POST"])
def profile():
    currdatetime = datetime.now()
    if request.method == "GET":
        res = []
        query3 = f"""select * from post_data where authorId = '{user_Id}';"""
        try:
            with mysql.connector.connect(host="localhost",user="root",password="Mysql*24", database = "pml") as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query3)
                    res=cursor.fetchall()
        except Error as e:
            print(e)
        return render_template("profile.html", res = res)
    elif request.method == "POST":
        title=request.form['title']
        content=request.form['content']
        query2 = f"""insert into post_data(postTitle, content, authorId, version, currentdate) values ('{title}', '{content}', '{user_Id}', "1", '{currdatetime}');"""
        try:
            with mysql.connector.connect(host="localhost",user="root",password="Mysql*24", database = "pml") as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query2)
                    connection.commit()
        except Exception as e:
            print(e)
        return redirect(url_for("timeline"))

        
@blog.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for("login"))
    
    
@blog.route('/delete_account')
def delete_account():
    if 'username' in session:
        username = session['username']
    try:
        with mysql.connector.connect(host="localhost",user="root",password="Mysql*24", database = "pml") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                cursor.execute(f"""delete from user_data where username = '{username}';""")
                connection.commit();
    except Exception as e:
        print(e)
    return redirect(url_for("register"))


    
if __name__ == "__main__":
    blog.run(host="0.0.0.0", port=50000)