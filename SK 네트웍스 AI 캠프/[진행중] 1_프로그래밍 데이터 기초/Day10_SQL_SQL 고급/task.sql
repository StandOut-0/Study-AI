/* 
Self Study Workbook v2.0

본 Workbook에서 제시하고 있는 테이블들은 춘 대학교의 교육시스템을 관리하기 위한 테이블입니다.
테이블은 모두 6개로 구성되었으며, 테이블 구조 및 속성들(컬럼 타입 및 Nullable 여부 등)은
본 시스템을 운영함에 있어서 성능 및 효율성을 고려하여 만들어져 있는 상태입니다.
(따라서 데이터 모델링 관점에서는 다소 적합하지 않은 부분도 있을 수 있습니다)

제공된 테이블 레이아웃을 충분히 파악한 후, 주어진 문제를 스스로 풀어보시기 바랍니다.
*/


/* 
========================================================
1. 학과 TB_DEPARTMENT
========================================================
Attribute Name   Column Name       Data type      Null Option   Is PK   Is FK   Parent table
학과 번호        DEPARTMENT_NO     VARCHAR2(10)   NOT NULL      Yes     No
학과 이름        DEPARTMENT_NAME   VARCHAR2(20)   NOT NULL      No      No
계열             CATEGORY          VARCHAR2(20)   NULL          No      No
개설 여부        OPEN_YN           CHAR(1)        NULL          No      No
정원             CAPACITY          NUMBER         NULL          No      No
*/

use homeworkdb;
set FOREIGN_KEY_CHECKS = 0;
drop table TB_DEPARTMENT;
set FOREIGN_KEY_CHECKS = 1;
CREATE TABLE TB_DEPARTMENT (
    DEPARTMENT_NO   VARCHAR(10) NOT NULL,
    DEPARTMENT_NAME VARCHAR(20) NOT NULL,
    CATEGORY        VARCHAR(20),
    OPEN_YN         CHAR(1),
    CAPACITY        int,
    CONSTRAINT PK_DEPARTMENT PRIMARY KEY (DEPARTMENT_NO)
);

/* 
========================================================
2. 학생 TB_STUDENT
========================================================
Attribute Name     Column Name          Data type      Null Option   Is PK   Is FK   Parent table
학생 번호          STUDENT_NO           VARCHAR2(10)   NOT NULL      Yes     No
학과 번호          DEPARTMENT_NO        VARCHAR2(10)   NOT NULL      No      Yes     TB_DEPARTMENT
학생 이름          STUDENT_NAME         VARCHAR2(30)   NOT NULL      No      No
학생 주민번호      STUDENT_SSN          VARCHAR2(14)   NULL          No      No
학생 주소          STUDENT_ADDRESS      VARCHAR2(100)  NULL          No      No
입학 일자          ENTRANCE_DATE        DATE           NULL          No      No
휴학 여부          ABSENCE_YN           CHAR(1)        NULL          No      No
지도 교수 번호     COACH_PROFESSOR_NO   VARCHAR2(10)   NULL          No      Yes     TB_PROFESSOR
* 휴학생인 경우 ABSENCE_YN = 'Y'
*/

set FOREIGN_KEY_CHECKS = 0;
drop table TB_STUDENT;
set FOREIGN_KEY_CHECKS = 1;

CREATE TABLE TB_STUDENT (
    STUDENT_NO          VARCHAR(10) NOT NULL,
    DEPARTMENT_NO       VARCHAR(10) NOT NULL,
    STUDENT_NAME        VARCHAR(30) NOT NULL,
    STUDENT_SSN         VARCHAR(14),
    STUDENT_ADDRESS     VARCHAR(100),
    ENTRANCE_DATE       DATE,
    ABSENCE_YN          CHAR(1),
    COACH_PROFESSOR_NO  VARCHAR(10),
    CONSTRAINT PK_STUDENT PRIMARY KEY (STUDENT_NO),
    CONSTRAINT FK_STU_DEPT FOREIGN KEY (DEPARTMENT_NO)
        REFERENCES TB_DEPARTMENT(DEPARTMENT_NO),
    CONSTRAINT FK_STU_PROF FOREIGN KEY (COACH_PROFESSOR_NO)
        REFERENCES TB_PROFESSOR(PROFESSOR_NO)
);


/*

========================================================
3. 과목 TB_CLASS
========================================================
Attribute Name        Column Name               Data type      Null Option   Is PK   Is FK   Parent table
과목 번호             CLASS_NO                  VARCHAR2(10)   NOT NULL      Yes     No
학과 번호             DEPARTMENT_NO            VARCHAR2(10)   NOT NULL      No      Yes     TB_DEPARTMENT
선수 과목 번호        PREATTENDING_CLASS_NO    VARCHAR2(10)   NULL          No      Yes     TB_CLASS
과목 이름             CLASS_NAME               VARCHAR2(30)   NOT NULL      No      No
과목 구분             CLASS_TYPE               VARCHAR2(10)   NULL          No      No

*/

set FOREIGN_KEY_CHECKS = 0;
drop table TB_CLASS;
set FOREIGN_KEY_CHECKS = 1;
CREATE TABLE TB_CLASS (
    CLASS_NO               VARCHAR(10) NOT NULL,
    DEPARTMENT_NO          VARCHAR(10) NOT NULL,
    PREATTENDING_CLASS_NO  VARCHAR(10),
    CLASS_NAME             VARCHAR(30) NOT NULL,
    CLASS_TYPE             VARCHAR(10),
    CONSTRAINT PK_CLASS PRIMARY KEY (CLASS_NO),
    CONSTRAINT FK_CLASS_DEPT FOREIGN KEY (DEPARTMENT_NO)
        REFERENCES TB_DEPARTMENT(DEPARTMENT_NO),
    CONSTRAINT FK_CLASS_PRE FOREIGN KEY (PREATTENDING_CLASS_NO)
        REFERENCES TB_CLASS(CLASS_NO)
);


/*
========================================================
4. 과목 교수 TB_CLASS_PROFESSOR
========================================================
Attribute Name     Column Name     Data type      Null Option   Is PK   Is FK   Parent table
과목 번호          CLASS_NO        VARCHAR2(10)   NOT NULL      Yes     Yes     TB_CLASS
교수 번호          PROFESSOR_NO    VARCHAR2(10)   NOT NULL      Yes     Yes     TB_PROFESSOR
*/

set FOREIGN_KEY_CHECKS = 0;
drop table TB_CLASS_PROFESSOR;
set FOREIGN_KEY_CHECKS = 1;
CREATE TABLE TB_CLASS_PROFESSOR (
    CLASS_NO     VARCHAR(10) NOT NULL,
    PROFESSOR_NO VARCHAR(10) NOT NULL,
    CONSTRAINT PK_CLASS_PROF PRIMARY KEY (CLASS_NO, PROFESSOR_NO),
    CONSTRAINT FK_CP_CLASS FOREIGN KEY (CLASS_NO)
        REFERENCES TB_CLASS(CLASS_NO),
    CONSTRAINT FK_CP_PROF FOREIGN KEY (PROFESSOR_NO)
        REFERENCES TB_PROFESSOR(PROFESSOR_NO)
);


/*

========================================================
5. 교수 TB_PROFESSOR
========================================================
Attribute Name     Column Name        Data type      Null Option   Is PK   Is FK   Parent table
교수 번호          PROFESSOR_NO       VARCHAR2(10)   NOT NULL      Yes     No
교수 이름          PROFESSOR_NAME     VARCHAR2(30)   NOT NULL      No      No
교수 주민번호      PROFESSOR_SSN      VARCHAR2(14)   NULL          No      No
교수 주소          PROFESSOR_ADDRESS  VARCHAR2(100)  NULL          No      No
학과 번호          DEPARTMENT_NO      VARCHAR2(10)   NULL          No      Yes     TB_DEPARTMENT
*/
set FOREIGN_KEY_CHECKS = 0;
drop table TB_PROFESSOR;
set FOREIGN_KEY_CHECKS = 1;
CREATE TABLE TB_PROFESSOR (
    PROFESSOR_NO      VARCHAR(10) NOT NULL,
    PROFESSOR_NAME    VARCHAR(30) NOT NULL,
    PROFESSOR_SSN     VARCHAR(14),
    PROFESSOR_ADDRESS VARCHAR(100),
    DEPARTMENT_NO     VARCHAR(10),
    CONSTRAINT PK_PROFESSOR PRIMARY KEY (PROFESSOR_NO),
    CONSTRAINT FK_PROF_DEPT FOREIGN KEY (DEPARTMENT_NO)
        REFERENCES TB_DEPARTMENT(DEPARTMENT_NO)
);


/*

========================================================
6. 성적 TB_GRADE
========================================================
Attribute Name   Column Name   Data type       Null Option   Is PK   Is FK   Parent table
학기 번호        TERM_NO       VARCHAR2(10)    NOT NULL      Yes     No
과목 번호        CLASS_NO      VARCHAR2(10)    NOT NULL      Yes     Yes     TB_CLASS
학생 번호        STUDENT_NO    VARCHAR2(10)    NOT NULL      Yes     Yes     TB_STUDENT
학점             POINT         NUMBER(3,2)     NULL          No      No
*/
set FOREIGN_KEY_CHECKS = 0;
drop table TB_GRADE;
set FOREIGN_KEY_CHECKS = 1;

CREATE TABLE TB_GRADE (
    TERM_NO     VARCHAR(10) NOT NULL,
    CLASS_NO    VARCHAR(10) NOT NULL,
    STUDENT_NO  VARCHAR(10) NOT NULL,
    POINT       DECIMAL(3,2),
    CONSTRAINT PK_GRADE PRIMARY KEY (TERM_NO, CLASS_NO, STUDENT_NO),
    CONSTRAINT FK_GRADE_CLASS FOREIGN KEY (CLASS_NO)
        REFERENCES TB_CLASS(CLASS_NO),
    CONSTRAINT FK_GRADE_STUDENT FOREIGN KEY (STUDENT_NO)
        REFERENCES TB_STUDENT(STUDENT_NO)
);




/* 
========================================================
춘 기술대학교 SQL 문제 모음
========================================================


1. 학과 이름과 계열 출력
--------------------------------------------------------
학과 테이블(TB_DEPARTMENT)의 학과 이름과 계열을 출력하시오.
단, 출력 헤더는 "학과 명", "계열"로 표시한다.

출력 예)
학과 명              계열
-------------------- --------------------
국어국문학과         인문사회
영어영문학과         인문사회
사학과               인문사회
철학과               인문사회
법학과               인문사회
행정학과             인문사회
...
체육학과             예체능

63 rows selected
*/

use homeworkdb;

INSERT INTO TB_DEPARTMENT (DEPARTMENT_NO, DEPARTMENT_NAME, CATEGORY, OPEN_YN, CAPACITY) VALUES ('001', '국어국문학과', '인문사회', 'Y', 20);
INSERT INTO TB_DEPARTMENT (DEPARTMENT_NO, DEPARTMENT_NAME, CATEGORY, OPEN_YN, CAPACITY) VALUES ('002', '영어영문학과', '인문사회', 'Y', 36);
INSERT INTO TB_DEPARTMENT (DEPARTMENT_NO, DEPARTMENT_NAME, CATEGORY, OPEN_YN, CAPACITY) VALUES ('003', '사학과', '인문사회', 'Y', 28);
INSERT INTO TB_DEPARTMENT (DEPARTMENT_NO, DEPARTMENT_NAME, CATEGORY, OPEN_YN, CAPACITY) VALUES ('050', '미술학과', '예체능', 'Y', 25);
INSERT INTO TB_DEPARTMENT (DEPARTMENT_NO, DEPARTMENT_NAME, CATEGORY, OPEN_YN, CAPACITY) VALUES ('060', '체육학과', '예체능', 'Y', 30);

select DEPARTMENT_NAME 학과명, CATEGORY 계열
from tb_department
order by DEPARTMENT_NAME;


/* 

2. 학과별 정원 출력
--------------------------------------------------------
학과별 정원을 다음 형식으로 출력하시오.

출력 예)
학과별 정원
------------------------------------------------
국어국문학과의 정원은 20명 입니다.
영어영문학과의 정원은 36명 입니다.
사학과의 정원은 28명 입니다.
철학과의 정원은 28명 입니다.
...
미술학과의 정원은 ...
산업디자인학과의 정원은 ...
체육학과의 정원은 ...

63 rows selected
*/
select CONCAT(`DEPARTMENT_NAME`,'의 정원은 ', capacity, '명 입니다.')
 from tb_department;





/* 

3. 국어국문학과 휴학 중인 여학생 조회
--------------------------------------------------------
"국어국문학과"에 재학 중인 학생 중
현재 휴학 상태(ABSENCE_YN = 'Y')인 여학생을 조회하시오.

조건:
- 학과코드는 TB_DEPARTMENT에서 조회
- 학생 테이블: TB_STUDENT

출력)
STUDENT_NAME
--------------------
홍길동 (예시)
핚수현
*/
use homeworkdb;
SET FOREIGN_KEY_CHECKS = 0;
SET FOREIGN_KEY_CHECKS = 1;
INSERT INTO TB_STUDENT 
(STUDENT_NO, DEPARTMENT_NO, STUDENT_NAME, STUDENT_SSN, STUDENT_ADDRESS, ENTRANCE_DATE, ABSENCE_YN, COACH_PROFESSOR_NO) 
VALUES 
('A217005', '001', '한수현', '821119-2122202', '전주시 덕진구', '2002-03-01', 'Y', 'P002');

INSERT INTO TB_STUDENT 
(STUDENT_NO, DEPARTMENT_NO, STUDENT_NAME, STUDENT_SSN, STUDENT_ADDRESS, ENTRANCE_DATE, ABSENCE_YN, COACH_PROFESSOR_NO) 
VALUES 
('A513079', '002', '홍경희', '851225-2345678', '서울시 강남구', '2005-03-01', 'N', 'P003');

INSERT INTO TB_STUDENT 
(STUDENT_NO, DEPARTMENT_NO, STUDENT_NAME, STUDENT_SSN, STUDENT_ADDRESS, ENTRANCE_DATE, ABSENCE_YN, COACH_PROFESSOR_NO) 
VALUES 
('A211375', '001', '최허현', '841102-1154425', '전주시 완산구', '2002-03-01', 'N', 'P002');

select student_name from tb_student
where department_no =
    (select department_no from tb_department where DEPARTMENT_name = '국어국문학과')
and ABSENCE_YN = 'Y';




/* 

4. 장기 연체자 학생 이름 조회
--------------------------------------------------------
다음 학번을 가진 학생들의 이름을 조회하시오.

대상 학번:
A513079, A513090, A513091, A513110, A513119

출력)
STUDENT_NAME
--------------------
홍경희
최경희
정경훈
정경환
이경환
*/

select * from tb_student;

set FOREIGN_KEY_CHECKS = 0;
INSERT INTO TB_STUDENT 
VALUES 
('A513090', '002', '최경희', '860101-1234567', '서울시 서초구', '2005-03-01', 'N', 'P003');

INSERT INTO TB_STUDENT 
VALUES 
('A513091', '003', '정경훈', '850303-2233445', '대전시 중구', '2005-03-01', 'N', 'P004');

INSERT INTO TB_STUDENT 
VALUES 
('A513110', '003', '정경환', '840707-3344556', '부산시 해운대구', '2005-03-01', 'N', 'P004');

INSERT INTO TB_STUDENT 
VALUES 
('A513119', '004', '이경환', '830909-4455667', '광주시 북구', '2005-03-01', 'N', 'P005');
set FOREIGN_KEY_CHECKS = 1;
select STUDENT_NAME from tb_student
where student_no in ('A513079', 'A513090', 'A513091', 'A513110', 'A513119');




/* 

5. 입학정원 20~30명 학과 조회
--------------------------------------------------------
입학정원이 20명 이상 30명 이하인 학과의
학과 이름과 계열을 출력하시오.

출력)
DEPARTMENT_NAME      CATEGORY
-------------------- --------------------
국어국문학과         인문사회
사학과               인문사회
철학과               인문사회
...
미술학과             예체능
산업디자인학과       예체능
체육학과             예체능

24 rows selected
*/
select DEPARTMENT_NAME, category from tb_department
where capacity >= 20 and capacity <= 30;





/* 

6. 총장 이름 조회
--------------------------------------------------------
춘 기술대학교의 총장을 제외한 교수들은 모두 학과를 가지고 있다.
이를 이용하여 총장의 이름을 조회하는 SQL을 작성하시오.

출력)
PROFESSOR_NAME
--------------------
임해정
*/
set FOREIGN_KEY_CHECKS = 0;

INSERT INTO TB_PROFESSOR (PROFESSOR_NO, PROFESSOR_NAME, PROFESSOR_SSN, PROFESSOR_ADDRESS, DEPARTMENT_NO) VALUES ('P001', '임해정', '650101-1234567', '서울시 중구', NULL);
INSERT INTO TB_PROFESSOR (PROFESSOR_NO, PROFESSOR_NAME, PROFESSOR_SSN, PROFESSOR_ADDRESS, DEPARTMENT_NO) VALUES ('P002', '김교수', '700505-1111111', '경기도 수원시', '001');
INSERT INTO TB_PROFESSOR (PROFESSOR_NO, PROFESSOR_NAME, PROFESSOR_SSN, PROFESSOR_ADDRESS, DEPARTMENT_NO) VALUES ('P003', '이교수', '751010-2222222', '전주시 완산구', '002');

INSERT INTO TB_CLASS_PROFESSOR (CLASS_NO, PROFESSOR_NO) VALUES ('C0405500', 'P002');
INSERT INTO TB_CLASS_PROFESSOR (CLASS_NO, PROFESSOR_NO) VALUES ('C0409000', 'P002');
INSERT INTO TB_CLASS_PROFESSOR (CLASS_NO, PROFESSOR_NO) VALUES ('C3051900', 'P003');
set FOREIGN_KEY_CHECKS = 1;
select * from tb_professor;
select PROFESSOR_NAME from tb_professor
where department_no is null;





/* 

7. 학과 미지정 학생 확인
--------------------------------------------------------
학과가 지정되지 않은 학생이 존재하는지 확인하는 SQL을 작성하시오.
*/

select count(*) from tb_student
where department_no is null;




/* 

8. 선수과목이 존재하는 과목 조회
--------------------------------------------------------
선수과목(PREATTENDING_CLASS_NO)이 존재하는 과목의
과목 번호를 조회하시오.

출력)
CLASS_NO
----------
C0405500
C0409000
C3745400
C0432500
C3051900
C3221500

6 rows selected
*/
set FOREIGN_key_checks = 0;
TRUNCATE TABLE TB_CLASS;
INSERT INTO TB_CLASS VALUES ('C0405500', '001', NULL, '국문학개론', '전공필수');
INSERT INTO TB_CLASS VALUES ('C0409000', '001', 'C0405500', '국어사', '전공선택');
INSERT INTO TB_CLASS VALUES ('C3745400', '002', 'C3051900', '영어회화', '전공선택');
INSERT INTO TB_CLASS VALUES ('C0432500', '003', 'C0405500', '문학개론', '전공필수');
INSERT INTO TB_CLASS VALUES ('C3051900', '002', NULL, '영어기초', '교양');
INSERT INTO TB_CLASS VALUES ('C3221500', '004', 'C3051900', '고급영어', '전공선택');
INSERT INTO TB_CLASS VALUES ('C1111111', '002', 'C0409000', '심화국어', '전공선택');
INSERT INTO TB_CLASS VALUES ('C2222222', '003', 'C3745400', '고급영어회화', '전공선택');
set FOREIGN_key_checks = 1;
select CLASS_NO from tb_class
where PREATTENDING_CLASS_NO is not null;





/* 

9. 계열(CATEGORY) 종류 조회
--------------------------------------------------------
춘 기술대학교에 존재하는 계열을 중복 없이 조회하시오.

출력)
CATEGORY
--------------------
공학
예체능
의학
인문사회
자연과학

*/
set FOREIGN_key_checks = 0;
INSERT INTO TB_DEPARTMENT VALUES ('101', '컴퓨터공학과', '공학', 'Y', 40);
INSERT INTO TB_DEPARTMENT VALUES ('102', '간호학과', '의학', 'Y', 30);
INSERT INTO TB_DEPARTMENT VALUES ('103', '수학과', '자연과학', 'Y', 30);
INSERT INTO TB_DEPARTMENT VALUES ('104', '기계공학과', '공학', 'Y', 40);
set FOREIGN_key_checks = 1;
select DISTINCT CATEGORY from tb_department;





/* 
10. 02학번 전주 거주 재학생 조회
--------------------------------------------------------
2002학번 학생 중 전주 거주자 모임을 만들려고 한다.
단, 휴학 학생은 제외한다.

출력:
STUDENT_NO     STUDENT_NAME     STUDENT_SSN
----------     --------------   --------------
A217005        고수현           821119-2122202
A211375        최허현           841102-1154425
...
11 rows selected
*/
select * from tb_student;

set FOREIGN_key_checks = 0;
INSERT INTO TB_STUDENT VALUES
('A212001', '002', '이민수', '820101-1234567', '전주시 덕진구', '2002-03-01', 'N', 'P003');

INSERT INTO TB_STUDENT VALUES
('A213002', '002', '박지훈', '821231-2345678', '서울시 강남구', '2002-03-01', 'N', 'P003');

INSERT INTO TB_STUDENT VALUES
('A214003', '003', '김하늘', '820505-3456789', '전주시 완산구', '2002-03-01', 'Y', 'P004');

INSERT INTO TB_STUDENT VALUES
('A215004', '003', '정우성', '821010-4567890', '전주시 덕진구', '2002-03-01', 'N', 'P004');

INSERT INTO TB_STUDENT VALUES
('A216005', '004', '한지민', '821212-5678901', '부산시 해운대구', '2002-03-01', 'N', 'P005');

INSERT INTO TB_STUDENT VALUES
('A218006', '004', '오세훈', '821111-6789012', '전주시 덕진구', '2002-03-01', 'N', 'P005');
select * from tb_student;

UPDATE TB_STUDENT
SET STUDENT_ADDRESS = '전주시 덕진구',
    ABSENCE_YN = 'N'
WHERE STUDENT_NO = 'A217005';
UPDATE TB_STUDENT
SET STUDENT_ADDRESS = '전주시 완산구',
    ABSENCE_YN = 'N'
WHERE STUDENT_NO = 'A211375';


INSERT INTO TB_STUDENT VALUES
('A212010', '001', '김민수', '820101-1111111', '전주시 덕진구', '2002-03-01', 'N', 'P002');

INSERT INTO TB_STUDENT VALUES
('A212011', '001', '이서연', '820202-2222222', '전주시 완산구', '2002-03-01', 'N', 'P002');

INSERT INTO TB_STUDENT VALUES
('A212012', '001', '박지훈', '820303-3333333', '전주시 덕진구', '2002-03-01', 'N', 'P002');

INSERT INTO TB_STUDENT VALUES
('A212013', '001', '정하늘', '820404-4444444', '전주시 완산구', '2002-03-01', 'N', 'P002');

INSERT INTO TB_STUDENT VALUES
('A212014', '001', '오세훈', '820505-5555555', '전주시 덕진구', '2002-03-01', 'N', 'P002');

INSERT INTO TB_STUDENT VALUES
('A212015', '001', '한지민', '820606-6666666', '전주시 완산구', '2002-03-01', 'N', 'P002');

UPDATE TB_STUDENT
SET STUDENT_ADDRESS = '전주시 덕진구',
    ABSENCE_YN = 'N',
    STUDENT_SSN = '821119-2122202'
WHERE STUDENT_NO = 'A217005';

UPDATE TB_STUDENT
SET STUDENT_ADDRESS = '전주시 완산구',
    ABSENCE_YN = 'N',
    STUDENT_SSN = '841102-1154425'
WHERE STUDENT_NO = 'A211375';

INSERT INTO TB_STUDENT 
VALUES (
'A212016',
'001',
'이준호',
'820707-7777777',
'전주시 덕진구',
'2002-03-01',
'N',
'P002'
);

UPDATE TB_STUDENT
SET STUDENT_NAME = '고수현',
    STUDENT_SSN = '821119-2122202',
    STUDENT_ADDRESS = '전주시 덕진구',
    ABSENCE_YN = 'N'
WHERE STUDENT_NO = 'A217005';
UPDATE TB_STUDENT
SET STUDENT_SSN = '821102-1154425',
    STUDENT_ADDRESS = '전주시 완산구',
    ABSENCE_YN = 'N',
    STUDENT_NAME = '최허현'
WHERE STUDENT_NO = 'A211375';

DELETE FROM TB_STUDENT
WHERE STUDENT_NO = 'A212010';

select * from tb_student;
set FOREIGN_key_checks = 1;

select STUDENT_NO, STUDENT_NAME, STUDENT_SSN 
from tb_student
where STUDENT_SSN like '82%'
and student_address like '%전주%'
and ABSENCE_YN = 'N';
