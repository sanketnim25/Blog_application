user_register="""INSERT INTO USER_DATA VALUES ('{user_id}','{username}','{email}','{mobile_number}','{introduction}','{password}');"""
user_update="""UPDATE user_data set name='{username}', email='{email}',Mobile_number='{mobile_number}',password='{password}',introduction='{introduction}' where user_id='{user_info[0][0]}';"""
user_delete="""DELETE FROM USER_DATA where user_id='{id}';"""



post_delete=""""DELETE FROM post_DATA where user_id='{id}';""""

comment_delete="""DELETE FROM comment_DATA where user_id='{id}';"""
