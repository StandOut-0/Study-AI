select user();
-- use studentdb;

drop table user_account;
drop table if exits manage;

create table user_account(
user_id int primary key comment '사용자 번호',
user_name varchar(50) not null comment '사용자 이름',
user_pwd varchar(30) not null comment '패스워드',
user_email varchar(50) not null UNIQUE comment '이메일',
created_at DATETIME DEFAULT CURRENT_TIMESTAMP comment '생성일'
) comment = '사용자 계정 테이블';

create Table orders(
    order_no char(4) comment '주문번호',
    cust_no char(4) comment '고객번호',
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP comment '주문일자',
    ship_date DATETIME comment '배송일자',
    ship_address varchar(50) comment '배송주소',
    quantity int comment '주문수량'
    ) comment = '주문 테이블';

INSERT INTO orders VALUES
('1234','1234','2021-01-01 00:00:00','2021-01-02 00:00:00','서울 강남구 삼성동',10);

INSERT INTO orders VALUES
('1236','1234', DEFAULT, DEFAULT, '서울 강남구 삼성동',10);

select * from orders;

create table tbl_notnull(
    nid char(3) not null,
    sname VARCHAR(10)
)
INSERT INTO tbl_notnull VALUES ('100','ORACLE');
INSERT INTO tbl_notnull VALUES (NULL,'ORACLE');
select * from tbl_notnull;

CREATE TABLE TABLE_UNIQUE(
    ID CHAR(3) UNIQUE,
    SNAME VARCHAR(20)
    );
INSERT INTO TABLE_UNIQUE
VALUES ('100','ORACLE');
INSERT INTO TABLE_UNIQUE
VALUES ('100','ORACLE');
select * from TABLE_UNIQUE;

CREATE TABLE TABLE_UNIQUE2(ID CHAR(3),
SNAME VARCHAR(20),
SCODE CHAR(2),
CONSTRAINT TN2_ID_UN UNIQUE (ID,SNAME));

INSERT INTO TABLE_UNIQUE2
VALUES ('100', 'ORACLE', '01');
INSERT INTO TABLE_UNIQUE2
VALUES ('200', 'ORACLE', '01');
INSERT INTO TABLE_UNIQUE2
VALUES ('200','ORACLE','02');

DESC TABLE_UNIQUE2;
DESCRIBE TABLE_UNIQUE2;

SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'TABLE_UNIQUE2';

CREATE TABLE TABLE_CHECK (
    EMP_ID CHAR(3) PRIMARY KEY,
    SALARY int CHECK ( SALARY > 0 ),
MARRIAGE CHAR(1),
CONSTRAINT CHK_MRG CHECK ( MARRIAGE IN ( 'Y','N' ) ) );

INSERT INTO TABLE_CHECK
VALUES ('100', -100, 'Y');

INSERT INTO TABLE_CHECK
VALUES ('100', 500, '?');

create table tbl_pk(
    pid CHAR(3),
    sname VARCHAR(20),
    scode CHAR(2),
    CONSTRAINT tbl_pk_pk PRIMARY KEY (pid,sname)
)

insert into tbl_pk values ('10','ORACLE','01');
insert into tbl_pk values ('10',null,'01');
select * from tbl_pk;
show keys from tbl_pk


CREATE TABLE TABLE_SUBQUERY1
AS SELECT EMP_ID, EMP_NAME, SALARY, DEPT_NAME, JOB_TITLE
FROM EMPLOYEE
LEFT JOIN DEPARTMENT USING (DEPT_ID)
LEFT JOIN JOB USING (JOB_ID);


DESC TABLE_SUBQUERY1;

CREATE TABLE TABLE_FK
(ID CHAR(3),
SNAME VARCHAR(20),
LID CHAR(2) REFERENCES LOCATION ( LOCATION_ID ) );
DESC TABLE_FK;

CREATE TABLE TABLE_FK2
(ID CHAR(3),
SNAME VARCHAR(20),
LID CHAR(2),
CONSTRAINT FK1 FOREIGN KEY ( LID ) REFERENCES LOCATION ( LOCATION_ID ) );

SELECT CONSTRAINT_NAME AS 이름,
CONSTRAINT_TYPE AS 유형,
R_CONSTRAINT_NAME AS 참조,
DELETE_RULE AS 삭제규칙,
SEARCH_CONDITION AS 내용
FROM employee
WHERE TABLE_NAME='CONSTRAINT_EMP';

SELECT *
FROM information_schema.TABLE_CONSTRAINTS;

SELECT *
FROM information_schema.KEY_COLUMN_USAGE;

ALTER Table table_check RENAME to table_check2;
ALTER TABLE table_fk2
RENAME COLUMN lid TO lid2;

CREATE TABLE EMP5
(EMP_ID CHAR(3),
EMP_NAME VARCHAR(20),
ADDR1 VARCHAR(20) DEFAULT '서울',
ADDR2 VARCHAR(100));
INSERT INTO EMP5
VALUES ('A10','임태희', DEFAULT, '청담동');
INSERT INTO EMP5
VALUES ('B10', '이병언', DEFAULT, '분당 정자동');
SELECT * FROM EMP5;

ALTER TABLE EMP5
MODIFY ADDR1 VARCHAR(50) DEFAULT '경기';
INSERT INTO EMP5
VALUES ('C10', '임승우', DEFAULT, '분당 효자촌');
SELECT * FROM EMP5;


delete from table_fk

alter table table_fk drop COLUMN id;
alter table table_fk drop COLUMN sname;
alter table table_fk drop COLUMN lid;

create table tbl_nopk(
    tid char(3),
    sname VARCHAR(20)
) engine=innodb;

create table tbl_fk4(
    fid char(3),
    fname VARCHAR(20),

    constraint tbl_fk4 foreign key (fid) references tbl_nopk(tid)
) engine=innodb;


CREATE TABLE parent (
    parent_id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE child (
    child_id INT PRIMARY KEY,
    parent_id INT,
    name VARCHAR(50),
    
    CONSTRAINT fk_parent
    FOREIGN KEY (parent_id)
    REFERENCES parent(parent_id)

    ON DELETE SET NULL
    ON UPDATE CASCADE
);

INSERT INTO parent VALUES (1, 'A');
INSERT INTO parent VALUES (2, 'B');
INSERT INTO child VALUES (101, 1, 'Kim');
INSERT INTO child VALUES (102, 1, 'Lee');
INSERT INTO child VALUES (103, 2, 'Park');

select * from child;

DELETE FROM parent WHERE parent_id = 1;
select * from child;

UPDATE parent
SET parent_id = 20
WHERE parent_id = 2;

select * from child;

