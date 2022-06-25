import mysql.connector
import random


def write(post_data):
    postId = str(random.randint(0,10000000000))

    try:
        with mysql.connector.connect(host="localhost", user="root", password="Mysql*24", database="pml") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                cursor.execute(f"""INSERT INTO post_data (postId, postTitle, content, authorId, currentdate)
                                VALUES ('{postId}', '{post_data["postTitle"]}', '{post_data["content"]}', {post_data["authorId"]}, '{post_data["currentdate"]}'
                                """)
                connection.commit()
                print(f"Post is written to disk id={postId}")
    except Error as e:
        print(e)


def delete():
    try:
        with mysql.connector.connect(host="localhost", user="root", password=None, database="mydb") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                cursor.execute("""delete from Person where PERSONID='5'
                    """)
                connection.commit()

    except Error as e:
        print(e)


def read_record_from_user():
    postTitle=input("Title of post")
    content=input("Post Content:")
    
    return {
        'Title of post': postTitle,
        'Post Content': content
    }

post_data = read_record_from_user()
write(post_data)
