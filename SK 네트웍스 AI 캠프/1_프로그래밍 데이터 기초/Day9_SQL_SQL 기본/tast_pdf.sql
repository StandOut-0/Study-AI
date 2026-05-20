/*
1. 계열 정보를 저장핛 카테고리 테이블을 맊들려고 핚다. 다음과 같은 테이블을 
작성하시오. 

테이블 이름 
    TB_CATEGORY 
컬럼 
    NAME, VARCHAR2(10)  
    USE_YN, CHAR(1), 기본값은 Y 가 들어가도록
 
*/
drop TABLE TB_CATEGORY;
CREATE TABLE TB_CATEGORY(
    NAME VARCHAR(10),
    USE_YN CHAR(1) DEFAULT 'Y'
);


/*
2. 과목 구분을 저장핛 테이블을 맊들려고 핚다. 다음과 같은 테이블을 작성하시오.
테이블이름 
    TB_CLASS_TYPE 
컬럼 
    NO, VARCHAR2(5), PRIMARY KEY 
    NAME , VARCHAR2(10) 
*/
CREATE TABLE TB_CLASS_TYPE(
    NO VARCHAR(5) PRIMARY KEY,
    NAME VARCHAR(10)
);

/*
3. TB_CATAGORY 테이블의 NAME 컬럼에 PRIMARY KEY를 생성하시오. 
(KEY 이름을 생성하지 않아도 무방함. 맊일 KEY 이를 지정하고자 핚다면 이름은 본인이 
알아서 적당핚 이름을 사용핚다.) 
*/
ALTER Table tb_category
add constraint pk_tb_category primary key (name);


/*
4. TB_CLASS_TYPE 테이블의 NAME 컬럼에 NULL 값이 들어가지 않도록 속성을 변경하시오.
*/
ALTER Table tb_class_type
MODIFY name VARCHAR(10) NOT NULL;

/*
5. 두 테이블에서 컬럼 명이 NO인 것은 기존 타입을 유지하면서 크기는 10 으로, 컬럼명이 
NAME 인 것은 마찪가지로 기존 타입을 유지하면서 크기 20 으로 변경하시오. 
*/
ALTER Table tb_category
MODIFY name VARCHAR(20) NOT NULL;
ALTER Table tb_class_type
MODIFY no VARCHAR(10) NOT NULL;


/*
6. 두 테이블의 NO 컬럼과 NAME 컬럼의 이름을 각 각 TB_ 를 제외핚 테이블 이름이 앞에 
붙은 형태로 변경핚다. 
(ex. CATEGORY_NAME) 
*/
ALTER Table tb_category
RENAME COLUMN name to  CATEGORY_NAME;
ALTER Table tb_class_type
RENAME COLUMN NO TO  CLASS_TYPE_NO;



/*
7. TB_CATAGORY 테이블과 TB_CLASS_TYPE 테이블의 PRIMARY KEY 이름을 다음과 같이 
변경하시오. 
Primary Key 의 이름은 ‚PK_ + 컬럼이름‛으로 지정하시오. (ex. PK_CATEGORY_NAME ) 
*/
SHOW INDEX FROM tb_category;
SELECT constraint_name
FROM information_schema.table_constraints
WHERE table_name = 'tb_category';
ALTER TABLE tb_category
DROP PRIMARY KEY,
ADD CONSTRAINT PK_CATEGORY_NAME PRIMARY KEY (CATEGORY_NAME);
ALTER TABLE TB_CLASS_TYPE
DROP PRIMARY KEY,
ADD CONSTRAINT PK_CLASS_TYPE_NO PRIMARY KEY (CLASS_TYPE_NO);


/*
8. 다음과 같은INSERT 문을 수행핚다. 
INSERT INTO TB_CATEGORY VALUES ('공학','Y'); 
INSERT INTO TB_CATEGORY VALUES ('자연과학','Y'); 
INSERT INTO TB_CATEGORY VALUES ('의학','Y'); 
INSERT INTO TB_CATEGORY VALUES ('예체능','Y'); 
INSERT INTO TB_CATEGORY VALUES ('인문사회','Y'); 
COMMIT;  
*/
INSERT INTO tb_category VALUES ('공학','Y');
INSERT INTO tb_category VALUES ('자연과학','Y');
INSERT INTO tb_category VALUES ('의학','Y');
INSERT INTO tb_category VALUES ('예체능','Y');
INSERT INTO tb_category VALUES ('인문사회','Y');
COMMIT;



/*
9.TB_DEPARTMENT 의 CATEGORY 컬럼이 TB_CATEGORY 테이블의 CATEGORY_NAME 컬럼을 부모 
값으로 참조하도록 FOREIGN KEY를 지정하시오. 이 때 KEY 이름은 
FK_테이블이름_컬럼이름으로 지정핚다. (ex. FK_DEPARTMENT_CATEGORY )
*/
SHOW TABLES LIKE '%TB_DEPARTMENT%';
CREATE TABLE TB_DEPARTMENT(
    DEPARTMENT_ID INT PRIMARY KEY,
    DEPARTMENT_NAME VARCHAR(50),
    CATEGORY_NAME VARCHAR(50),

    CONSTRAINT FK_DEPARTMENT_CATEGORY
    FOREIGN KEY (CATEGORY_NAME)
    REFERENCES TB_CATEGORY(CATEGORY_NAME)
)




/*
10. 춘 기술대학교 학생들의 정보맊이 포함되어 있는 학생일반정보 VIEW를 맊들고자 핚다. 
아래 내용을 참고하여 적젃핚 SQL 문을 작성하시오. 
뷰 이름 
    VW_학생일반정보 
컬럼 
    학번 
    학생이름 
    주소 
*/
DROP TABLE STUDENT;
CREATE TABLE STUDENT(
    STUDENT_ID CHAR(3) PRIMARY KEY,
    STUDENT_NAME VARCHAR(20),
    STUDENT_ADDRESS VARCHAR(100),
    STUDENT_PHONE VARCHAR(15),
    STUDENT_EMAIL VARCHAR(50)
);
INSERT INTO STUDENT VALUES ('A10','임태희','서울시 구로구', '010-1234-5678', 'a10@gmail.com');
INSERT INTO STUDENT VALUES ('B10','이병언','분당 정자동', '010-1234-5678', 'b10@gmail.com');
INSERT INTO STUDENT VALUES ('C10','임승우','분당 효자촌', '010-1234-5678', 'c10@gmail.com');
SELECT * FROM student;
DROP VIEW VW_학생일반정보;
CREATE VIEW VW_학생일반정보 AS
SELECT STUDENT_ID, STUDENT_NAME, STUDENT_ADDRESS
FROM STUDENT;
SELECT * FROM VW_학생일반정보;


/*
11. 춘 기술대학교는 1년에 두 번씩 학과별로 학생과 지도교수가 지도 면담을 진행핚다. 
이를 위해 사용핛 학생이름, 학과이름, 담당교수이름 으로 구성되어 있는 VIEW 를 맊드시오. 
이때 지도 교수가 없는 학생이 있을 수 있음을 고려하시오 (단, 이 VIEW 는 단순 SELECT 
맊을 핛 경우 학과별로 정렬되어 화면에 보여지게 맊드시오.) 

뷰 이름 
    VW_지도면담 
컬럼 
    학생이름 
    학과이름 
    지도교수이름 
*/
CREATE TABLE MAJOR(
    MAJOR_ID CHAR(3) PRIMARY KEY,
    MAJOR_NAME VARCHAR(50)
);
INSERT INTO MAJOR VALUES ('A10','전공필수');
INSERT INTO MAJOR VALUES ('B10','전공선택');
INSERT INTO MAJOR VALUES ('C10','교양필수');

DROP TABLE teacher;
CREATE TABLE TEACHER(
    TEACHER_ID CHAR(3) PRIMARY KEY,
    MAJOR_ID CHAR(3),
    TEACHER_NAME VARCHAR(20),
    TEACHER_ADDRESS VARCHAR(100),
    TEACHER_PHONE VARCHAR(15),
    TEACHER_EMAIL VARCHAR(50),

    CONSTRAINT FK_TEACHER_MAJOR
    FOREIGN KEY (MAJOR_ID)
    REFERENCES MAJOR(MAJOR_ID)
);
INSERT INTO TEACHER VALUES ('A10','A10','임태희','서울시 구로구', '010-1234-5678', 'a10@gmail.com');
INSERT INTO TEACHER VALUES ('B10','B10','이병언','분당 정자동', '010-1234-5678', 'b10@gmail.com');  
INSERT INTO TEACHER VALUES ('C10','C10','임승우','분당 효자촌', '010-1234-5678', 'c10@gmail.com');

ALTER TABLE student
ADD major_ID CHAR(3);

UPDATE student
SET major_ID = 'A10';

SELECT * FROM student;
ALTER TABLE student
DROP COLUMN student_DEPARTMENT_NAME;
SELECT * FROM student;

ALTER TABLE student
ADD CONSTRAINT FK_STUDENT_MAJOR
FOREIGN KEY (major_ID)
REFERENCES major(major_ID);

ALTER TABLE student
ADD TEACHER_ID CHAR(3);

ALTER TABLE student
ADD CONSTRAINT FK_STUDENT_TEACHER
FOREIGN KEY (TEACHER_ID)
REFERENCES teacher(TEACHER_ID);
SELECT * FROM student;

UPDATE student SET TEACHER_ID = 'A10' WHERE STUDENT_ID = 'A10';
UPDATE student SET TEACHER_ID = 'A10' WHERE STUDENT_ID = 'B10';
SELECT * FROM student;

CREATE VIEW VW_지도면담 AS
SELECT S.STUDENT_NAME, M.MAJOR_NAME, T.TEACHER_NAME
FROM STUDENT S
LEFT JOIN major M
ON S.MAJOR_ID = M.MAJOR_ID
LEFT JOIN teacher T
ON S.TEACHER_ID = T.TEACHER_ID;
SELECT * FROM VW_지도면담;


/*
12. 모든 학과의 학과별 학생 수를 확인핛 수 있도록 적젃핚 VIEW 를 작성해 보자.
뷰 이름 
    VW_학과별학생수 
컬럼 
    DEPARTMENT_NAME 
    STUDENT_COUNT 
*/
CREATE VIEW VW_학과별학생수 AS
SELECT M.MAJOR_NAME, COUNT(STUDENT_ID) AS STUDENT_COUNT
FROM STUDENT S
LEFT JOIN major M
ON S.MAJOR_ID = M.MAJOR_ID
GROUP BY M.MAJOR_NAME;
SELECT * FROM VW_학과별학생수;

SELECT * FROM student;
UPDATE student SET MAJOR_ID = 'B10' WHERE STUDENT_ID = 'A10';
UPDATE student SET TEACHER_ID = 'B10' WHERE STUDENT_ID = 'A10';


/*
13. 위에서 생성핚 학생일반정보 View를 통해서 학번이 A213046인 학생의 이름을 본인 
이름으로 변경하는 SQL 문을 작성하시오. 
*/
ALTER TABLE student
MODIFY STUDENT_ID VARCHAR(10);
INSERT INTO student VALUES (
    'A213046',
    '박아무개',
    '서울시 서초구 양재동',
    '1234-1234-1234',
    'a213046@gmail.com',
    'B10',
    'B10'
    );
UPDATE VW_학생일반정보 SET STUDENT_NAME = '박상희' WHERE STUDENT_ID = 'A213046';
SELECT * FROM VW_학생일반정보;


/*
14. 13 번에서와 같이 VIEW를 통해서 데이터가 변경될 수 있는 상황을 막으려면 VIEW를 
어떻게 생성해야 하는지 작성하시오. 
*/
CREATE VIEW VW_학생일반정보_수정불가 AS
SELECT STUDENT_ID, STUDENT_NAME, STUDENT_ADDRESS
FROM student
WITH CHECK OPTION;
SELECT * FROM VW_학생일반정보_수정불가;
CREATE USER 'just_for_view'@'%' IDENTIFIED BY 'just_for_view80*';
grant select on studentdb.VW_학생일반정보_수정불가 to 'just_for_view'@'%';


/*
15. 춘 기술대학교는 매년 수강신청 기갂맊 되면 특정 인기 과목들에 수강 신청이 몰려 
문제가 되고 있다. 최근 3년을 기준으로 수강인원이 가장 맋았던 3 과목을 찾는 구문을 
작성해보시오. 

과목번호    과목이름                         누적수강생수(명) 
---------- ------------------------------ ---------------- 
C1753800   서어방언학                                   29 
C1753400   서어문체롞                                   23 
C2454000   원예작물번식학특롞                             22 
*/
ALTER Table major
add COLUMN student_count INT;
UPDATE major SET student_count = 0;
SELECT * FROM major;
update major set student_count = 29 WHERE major_id = 'A10';

ALTER TABLE teacher DROP FOREIGN key fk_teacher_major;
ALTER Table teacher add constraint fk_teacher_major
FOREIGN KEY (major_id)
REFERENCES major(major_id);

set FOREIGN_KEY_CHECKS = 0;

ALTER TABLE major
MODIFY COLUMN MAJOR_ID VARCHAR(10);

set FOREIGN_KEY_CHECKS = 1;

insert into major VALUES('C1753800', '서어방언학', 29);
insert into major VALUES('C1753400', '서어문체롞', 23);
insert into major VALUES('C2454000', '원예작물번식학특롞', 22);
select * from major;

select * from major ORDER BY student_count DESC;


/*
 1. 과목유형 테이블(TB_CLASS_TYPE)에 아래와 같은 데이터를 입력하시오. 
 번호, 유형이름 
 ------------ 
 01, 전공필수 
 02, 전공선택 
 03, 교양필수 
 04, 교양선택 
 05. 논문지도 
*/
select * from TB_CLASS_TYPE;
insert into TB_CLASS_TYPE values('01', '전공필수');
insert into TB_CLASS_TYPE values('02', '전공선택');
insert into TB_CLASS_TYPE values('03', '교양필수');
insert into TB_CLASS_TYPE values('04', '교양선택');
insert into TB_CLASS_TYPE values('05', '논문지도');
select * from TB_CLASS_TYPE;



/*
 2. 춘 기술대학교 학생들의 정보가 포함되어 있는 학생일반정보 테이블을 맊들고자 핚다. 
아래 내용을 참고하여 적젃핚 SQL 문을 작성하시오. (서브쿼리를 이용하시오)

테이블이름 
  TB_학생일반정보 
컬럼 
   학번 
   학생이름 
   주소  
*/
CREATE TABLE TB_학생일반정보 as
select STUDENT_ID, STUDENT_NAME, STUDENT_ADDRESS
from STUDENT;
select * from TB_학생일반정보;


/*
 3. 국어국문학과 학생들의 정보맊이 포함되어 있는 학과정보 테이블을 맊들고자 핚다. 
아래 내용을 참고하여 적젃핚 SQL 문을 작성하시오. (힌트 : 방법은 다양함, 소신껏 
작성하시오)

테이블이름 
  TB_국어국문학과 
컬럼 
   학번 
   학생이름 
   출생년도 <= 네자리 년도로 표기 
   교수이름
*/
ALTER table student add COLUMN birth DATE;
update student set birth = '1998-03-14' ;
select * from student;
insert major VALUES('K1753800', '국어국문학과', 1);
set FOREIGN_KEY_CHECKS = 0;

select * from teacher;
ALTER table teacher MODIFY COLUMN teacher_ID VARCHAR(10);
insert teacher VALUES(
    'D10', 
    'K1753800',
    '임태희', 
    '서울시 구로구',
    '010-1234-5678', 
    'a213046@gmail.com'
    );
select * from major;
ALTER table student MODIFY COLUMN major_ID VARCHAR(10);
set FOREIGN_KEY_CHECKS = 1;
update student set major_id = 'K1753800' where STUDENT_ID = 'A213046';

drop TABLE TB_국어국문학과;
CREATE Table TB_국어국문학과 as
select s.student_id, s.student_name, year(s.birth), t.teacher_name
from student s
left join major m
on s.major_id = m.major_id
left join teacher t
on s.teacher_id = t.teacher_id
where s.major_id = 'K1753800';
select * from TB_국어국문학과;



/*
4. 현 학과들의 정원을 10% 증가시키게 되었다. 이에 사용핛 SQL 문을 작성하시오. (단, 
반올림을 사용하여 소수점 자릿수는 생기지 않도록 핚다)
*/
select * from major;
alter Table major add COLUMN capacity INT;
update major set capacity = 10;
update major set capacity = ROUND(capacity * 1.1);
select * from major;


/*
5. 학번 A413042 인 박건우 학생의 주소가 "서울시 종로구 숭인동 181-21 "로 변경되었다고 
핚다. 주소지를 정정하기 위해 사용핛 SQL 문을 작성하시오.
*/
select * from student;
set FOREIGN_KEY_CHECKS = 0;
alter table student MODIFY COLUMN teacher_ID VARCHAR(10);
update student set TEACHER_ID = 'K1753800' where STUDENT_ID = 'A213046';
insert student VALUES(
    'A413042',
    '박건우',
    '서울시 종로구 숭인동 181-20',
    '1234-1234-1234',
    'a413042@gmail.com',
    'B10',
    'B10',
    '1999-03-14'
    );
update student set STUDENT_ADDRESS = '서울시 종로구 숭인동 181-21' where STUDENT_ID = 'A413042';



/*
6. 주민등록번호 보호법에 따라 학생정보 테이블에서 주민번호 뒷자리를 저장하지 않기로 
결정하였다. 이 내용을 반영핛 적젃핚 SQL 문장을 작성하시오. 
(예. 830530-2124663 ==> 830530 ) 
*/
select * from student;
alter TABLE student add COLUMN jumin VARCHAR(20);
update student set jumin = '9803142000000';
update student set jumin = substring(jumin, 1, 6);




/*
7. 의학과 김명훈 학생은 2005년 1학기에 자신이 수강핚 '피부생리학' 점수가 
잘못되었다는 것을 발견하고는 정정을 요청하였다. 담당 교수의 확인 받은 결과 해당 
과목의 학점을 3.5로 변경키로 결정되었다. 적젃핚 SQL 문을 작성하시오.
*/
select * from major;
insert major VALUES('P1753800', '피부생리학', 1, 11);
select * from teacher;
insert teacher VALUES(
    'P10',
    'P1753800',
    '김명훈',
    '서울시 강남구',
    '010-1234-5678',
    'a777777@gmail.com'
    );
insert STudent VALUES(
    'A777777',
    '김명훈',
    '서울시 종로구 숭인동 181-20',
    '1234-1234-1234',
    'a777777@gmail.com',
    'P10',
    'P10',
    '1999-03-14',
    '980314'
)
select * from student;
alter table student add COLUMN score int;
alter table student add COLUMN score_check_to_teacher bool;
alter table student MODIFY COLUMN score FLOAT;
update student set score = 2.5;
update student 
set score = 3.5, score_check_to_teacher = true
where STUDENT_ID = 'A777777';
select * from student;




/*
8. 성적 테이블(TB_GRADE) 에서 휴학생들의 성적항목을 제거하시오. 
*/
alter Table student add COLUMN is_active bool;
update student set is_active = true;
select * from student;
update student set is_active = false where student_id = 'A777777';

create table TB_GRADE as
select student_id, student_name, score, is_active
from student;
select * from TB_GRADE;
DELETE from TB_GRADE where is_active = false;