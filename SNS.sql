drop database SNS;
create database SNS;
use SNS;
CREATE TABLE USER_DATA (
    USER_ID int,
    NAME varchar(50),
    EMAIL varchar(50),
    MOBILE_NUMBER varchar(50),
    PASSWORD varchar(50),
    INTRODUCTION varchar(500),
    primary key (USER_ID)
);
CREATE TABLE POST_DATA (
    USER_ID int,
    POST_ID int,
    VERSION_ID int,
    TITLE varchar(50),
    SUMMARY varchar(500),
    CONTENT varchar(5000),
    POST_TIME datetime,
    primary key (POST_ID),
    foreign key (USER_ID) references USER_DATA(USER_ID)
);
CREATE TABLE COMMENT_DATA (
    USER_ID int,
    POST_ID int,
    COMMENT_ID int,
    CONTENT varchar(500),
    COMMENT_TIME datetime,
    primary key (COMMENT_ID),
    foreign key (USER_ID) references USER_DATA(USER_ID),
    foreign key (POST_ID) references POST_DATA(POST_ID)
);