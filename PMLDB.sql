create table user_data(
	userId int(50) not null,
	username varchar(50),
	name varchar(100),
	email varchar(50),
	password varchar(50),
	mobile varchar(15),
	primary key(userId)
);
create table post_data(
	postId int not null auto_increment,
	postTitle varchar(100),
	content varchar(1000),
	authorId int(50),
	version int,
	currentdate datetime,
	primary key(postId),
	foreign key(authorId) references user_data(userId)on DELETE CASCADE
);
create table comment_data(
	commentId int not null auto_increment,
	commentText varchar(500),
	commentedPost int,
	commentedBy int(50),
	currentdate datetime,
	primary key(commentId),
	foreign key(commentedPost) references post_data(postId) on DELETE CASCADE,
	foreign key (commentedBy) references user_data(userId) on DELETE CASCADE
);

#insert into post_data(postId, postTitle, content, authorId, version, currentdate) values ("1", "title", "hello", "7167", "1", "2022-02-21 09:32:33");

insert into user_data(userid, username, name, email, password, mobile) values ("1", "p", "p", "p", "p", "9967874691");

SELECT u.userId, p.authorId, u.name, p.postTitle, p.content, p.currentdate FROM user_data u INNER JOIN post_data p ON u.userId = p.authorId;

insert into post_data(postTitle, content, authorId, version, currentdate) values (title, content, userId, "1", "2022-02-21 09:32:33");