-- 계정 : student / 암호 : Student80
-- studentdb 사용
-- 수업용 실습 스크립트
show databases;
-- create database studentdb;
USE studentdb;

drop table if exists sal_grade;
drop table if exists employee;
drop table if exists job;
drop table if exists department;
drop table if exists location;
drop table if exists country;
drop table if exists employee_role;
drop table if exists role_history;


CREATE TABLE COUNTRY
(
  COUNTRY_ID   CHAR(2) comment '국가코드',
  COUNTRY_NAME VARCHAR(30) NOT NULL comment '국가명',
  CONSTRAINT PK_CTRID PRIMARY KEY(COUNTRY_ID)
) ENGINE=InnoDB comment = '직원 근무 국가 정보 테이블';


CREATE TABLE LOCATION
(
  LOCATION_ID CHAR(2) comment '지역코드',
  COUNTRY_ID  CHAR(2) comment '국가코드',
  LOC_DESCRIBE VARCHAR(40) comment '지역명',
  CONSTRAINT PK_LOCID PRIMARY KEY(LOCATION_ID),
  CONSTRAINT FK_CTRID FOREIGN KEY(COUNTRY_ID) REFERENCES COUNTRY (country_id)
) ENGINE=InnoDB comment = '직원 근무 지역 정보 테이블';


CREATE TABLE DEPARTMENT
(
  DEPT_ID CHAR(2) comment '부서코드',
  DEPT_NAME VARCHAR(30) comment '부서이름',
  LOC_ID  CHAR(2) NOT NULL comment '지역코드',
  CONSTRAINT PK_DEPTID PRIMARY KEY(DEPT_ID),
  CONSTRAINT FK_LOCID FOREIGN KEY(LOC_ID) REFERENCES LOCATION (location_id)
) ENGINE=InnoDB comment = '부서 정보 테이블';


CREATE TABLE JOB
(
  JOB_ID     CHAR(2) comment '직급코드',
  JOB_TITLE  VARCHAR(35) comment '직급명',
  MIN_SAL  INT comment '직급 최저 급여',
  MAX_SAL INT comment '직급 최대 급여',
  CONSTRAINT PK_JOBID PRIMARY KEY(JOB_ID)
) ENGINE=InnoDB comment = '직급 정보 테이블';


CREATE TABLE SAL_GRADE
(
 SLEVEL  CHAR(1) PRIMARY KEY comment '급여등급',
 LOWEST  INT comment '최소급여',
 HIGHEST INT comment '최고급여'
) ENGINE=InnoDB comment = '급여 레벨 테이블';


CREATE TABLE EMPLOYEE
(
  EMP_ID      CHAR(3) comment '사번',
  EMP_NAME    VARCHAR(20)  NOT NULL comment '사원명', 
  EMP_NO      CHAR(14)     NOT NULL comment '주민등록번호', 
  EMAIL       VARCHAR(25)  comment '이메일',
  PHONE       VARCHAR(12)  comment '핸드폰번호',
  HIRE_DATE   DATE DEFAULT (CURDATE())  comment '입사일',
  JOB_ID      CHAR(2)  comment '직급코드', 
  SALARY      INT  comment '급여',
  BONUS_PCT   DECIMAL(5,2) comment '보넌스포인트',
  MARRIAGE    CHAR(1) DEFAULT 'N'  comment '결혼여부',
  MGR_ID      CHAR(3) comment '관리자사번',
  DEPT_ID     CHAR(2) comment '부서코드',

  CONSTRAINT PK_EMPID   PRIMARY KEY (EMP_ID),                 
  CONSTRAINT FK_DEPTID  FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT (DEPT_ID),
  CONSTRAINT FK_JOBID   FOREIGN KEY (JOB_ID) REFERENCES JOB (JOB_ID),
  CONSTRAINT CHK_MRIG   CHECK (MARRIAGE IN ('Y','N')),
  CONSTRAINT UNI_EMPNO  UNIQUE (EMP_NO)
) ENGINE=InnoDB  comment='직원 정보 테이블';


-- 테이블에 데이터 기록 **************************************
INSERT into country values ('KO', '한국' );
INSERT into country values ('JP', '일본' );
INSERT into country values ('CH', '중국' );
INSERT into country values ('US', '미국' );
INSERT into country values ('ID', '인도' );


INSERT into location values ('A1', 'KO', '아시아지역1' );
INSERT into location values ('A2', 'JP', '아시아지역2' );
INSERT into location values ('A3', 'CH', '아시아지역3' );
INSERT into location values ('U1', 'US', '미주지역' );
INSERT into location values ('OT', 'ID', '기타지역' );


INSERT into job values ('J1', '대표이사', 200000000, 400000000 );
INSERT into job values ('J2', '부사장', 150000000, 300000000 );
INSERT into job values ('J3', '부장', 70000000, 100000000 );
INSERT into job values ('J4', '차장', 50000000, 80000000 );
INSERT into job values ('J5', '과장', 42000000, 60000000 );
INSERT into job values ('J6', '대리', 38000000, 56000000 );
INSERT into job values ('J7', '사원', 20000000, 40000000 );


INSERT into SAL_GRADE values ('A', 3000000, 9000000 );
INSERT into SAL_GRADE values ('B', 2500000, 2999999 );
INSERT into SAL_GRADE values ('C', 2000000, 2499999 );
INSERT into SAL_GRADE values ('D', 1500000, 1999999 );
INSERT into SAL_GRADE values ('E', 1000000, 1499999 );


INSERT into department values ('20', '회계팀', 'A1' );
INSERT into department values ('10', '본사 인사팀', 'A1' );
INSERT into department values ('50', '해외영업1팀', 'U1' );
INSERT into department values ('60', '기술지원팀', 'OT' );
INSERT into department values ('80', '해외영업2팀', 'A2' );
INSERT into department values ('90', '해외영업3팀', 'A3' );
INSERT into department values ('30', '마케팅팀', 'A1' );


INSERT INTO EMPLOYEE VALUES ('100', '한선기', '621133-1483658', 'sg_ahn@kkk.com', '0199949999', STR_TO_DATE('90/04/01 13:30:30', '%y/%m/%d %H:%i:%s'), 'J1', 9000000, 0.2, 'Y', null, '90');
INSERT INTO EMPLOYEE VALUES ('101', '강중훈', '621136-1006405', 'jh_park@kkk.com', '0193334433', '04/04/30', 'J2', 5500000,null , 'Y', '100', '90' );
INSERT INTO EMPLOYEE VALUES ('102', '최만식', '861011-1940062', 'ms_choi@kkk.com', '0198879908', '95/12/30', 'J2', 3600000,null , 'Y', '101', '90' );
INSERT INTO EMPLOYEE VALUES ('103', '정도연', '631127-2519077', 'sy_kang@kkk.com', '0196654436', '97/06/03', 'J4', 2600000,null , 'Y', '104', '60' );
INSERT INTO EMPLOYEE VALUES ('104', '안석규', '651031-1962810', 'sg_han@kkk.com', '0192347654', '98/07/01', 'J3', 3500000, .25, 'Y', '100', '60' );
INSERT INTO EMPLOYEE VALUES ('107', '조재형', '721128-1732822', 'jh_jo@kkk.com', '0193325548', '98/11/23', 'J3', 3800000,null , 'Y', '104', '60' );
INSERT INTO EMPLOYEE VALUES ('124', '정지현', '641231-2269080', 'jih_jeon@kkk.com', '01922976129', '04/07/15', 'J7', 1500000,null , 'N', '141', '50' );
INSERT INTO EMPLOYEE VALUES ('141', '김예수', '651122-2592930', 'hs_kim@kkk.com', '0194087600', '01/03/20', 'J5', 2100000, .1, 'Y', '100', '50' );
INSERT INTO EMPLOYEE VALUES ('143', '나승원', '871024-1945881', 'sw_cha@kkk.com', '0197243979', '01/03/20', 'J5', 2300000,null , 'Y', '141', '50' );
INSERT INTO EMPLOYEE VALUES ('144', '김순이', '741122-2515789', 'sm_kim@kkk.com', '0192213306', '99/10/20', 'J3', 3400000, .1, 'Y', '141', '50' );
INSERT INTO EMPLOYEE VALUES ('149', '성해교', '640524-2148639', 'hg_song@kkk.com', '01992882295', '03/08/16', 'J7', 1900000,null , 'N', '141', '50' );
INSERT INTO EMPLOYEE VALUES ('174', '전우성', '821121-1660412', 'ws_jeong@kkk.com', '0193243388', '02/07/14', 'J6', 2090000,null , 'Y', '100', '80' );
INSERT INTO EMPLOYEE VALUES ('176', '엄정하', '791217-2230420', 'jh_um@kkk.com', '0194769665', '04/07/21', 'J6', 2420000, .2, 'Y', '174', '80' );
INSERT INTO EMPLOYEE VALUES ('178', '심하균', '611121-1673370', 'hk_shin@kkk.com', '0197122111', STR_TO_DATE('04/09/30', '%y/%m/%d'), null, 2300000, 0.3, 'Y', null, null);
INSERT INTO EMPLOYEE VALUES ('200', '고승우', '840217-1776881', 'sw_jo@kkk.com', '0193475512', '03/04/11', 'J7', 1500000,null , 'Y', '100', '10' );
INSERT INTO EMPLOYEE VALUES ('201', '박하일', '891225-1069101', 'hi_park@kkk.com', '01951564413', '04/11/10', 'J5', 2600000,null , 'Y', null, '50' );
INSERT INTO EMPLOYEE VALUES ('202', '권상후', '790331-1662986', 'sw_kwon@kkk.com', '0196640090', '01/05/20', 'J6', 3410000, .2, 'Y', '200', '10' );
INSERT INTO EMPLOYEE VALUES ('205', '임영애', '790833-2105839', 'jangum_lee@kkk.com', '0191132477', '00/01/31', 'J6', 2640000, .15, 'N', '200', '10' );
INSERT INTO EMPLOYEE VALUES ('206', '염정하', '860122-2785746', 'jh_yeum@kkk.com', '01997546623', STR_TO_DATE('03/09/17', '%y/%m/%d'), 'J7',1500000, NULL, 'Y', null, null);
INSERT INTO EMPLOYEE VALUES ('207', '김술오', '640226-1358242', 'so_kim@kkk.com', '', '96/10/01', 'J4', 2500000,null , 'Y', null, '20' );
INSERT INTO EMPLOYEE VALUES ('208', '이중기', '790411-1452247', 'jk_lee@kkk.com', '', '04/10/01', 'J4', 2500000,null , 'Y', null, '20' );
INSERT INTO EMPLOYEE VALUES ('210', '감우섭', '700813-1766819', 'manofking@kkk.com', '', '05/07/31', 'J4', 2500000,null , 'Y', null, '20' );

ALTER TABLE EMPLOYEE
ADD CONSTRAINT FK_MGRID FOREIGN KEY (MGR_ID) REFERENCES EMPLOYEE (EMP_ID);

COMMIT;

-- 날짜 데이터 업데이트
UPDATE EMPLOYEE
SET 
    HIRE_DATE = DATE_ADD(HIRE_DATE, INTERVAL 120 MONTH),
    SALARY = SALARY + 1000000,
    EMP_NO = CONCAT(CAST(SUBSTRING(EMP_NO, 1, 2) AS UNSIGNED) + 10, SUBSTRING(EMP_NO, 3));



SELECT * FROM EMPLOYEE;

UPDATE SAL_GRADE
SET LOWEST = LOWEST + 1000000, HIGHEST = HIGHEST + 1000000;

COMMIT;

-- 확인
SELECT * FROM EMPLOYEE;
select * from job;
select * from department;
select * from location;
select * from country;
select * from sal_grade;

-- ROLE 관련 테이블 추가 ********************************************************
CREATE TABLE EMPLOYEE_ROLE
(EMP_ID      CHAR(3),
 EMP_NAME    VARCHAR(20), 
 EMP_NO      CHAR(14), 
 EMAIL       VARCHAR(25),
 PHONE       VARCHAR(12),
 HIRE_DATE   DATE,
 JOB_ID      CHAR(2), 
 SALARY      int,
 BONUS_PCT   decimal(5, 2),
 MARRIAGE    CHAR(1),
 MGR_ID      CHAR(3),
 DEPT_ID     CHAR(2),
 ROLE_NAME   VARCHAR(50)
);

CREATE TABLE ROLE_HISTORY
(EMP_ID CHAR(3), 
 START_DATE DATE,
 END_DATE DATE,
 ROLE_NAME VARCHAR(30),
 DEPT_ID CHAR(2)
 );



INSERT INTO EMPLOYEE_ROLE VALUES ('100', '한선기', '621133-1483658', 'sg_ahn@kkk.com', '0199949999', '90/04/01', 'J1', 9000000, 0.2, 'Y', null, '90', 'SALES' );
INSERT INTO EMPLOYEE_ROLE VALUES ('101', '강중훈', '621136-1006405', 'jh_park@kkk.com', '0193334433', '04/04/30', 'J2', 5500000, null , 'Y', '100', '90', 'SALES' );
INSERT INTO EMPLOYEE_ROLE VALUES ('102', '최만식', '861011-1940062', 'ms_choi@kkk.com', '0198879908', '95/12/30', 'J2', 3600000,null , 'Y', '101', '90', 'SALES' );
INSERT INTO EMPLOYEE_ROLE VALUES ('103', '정도연', '631127-2519077', 'sy_kang@kkk.com', '0196654436', '97/06/03', 'J4', 2600000,null , 'Y', '104', '60', 'SE' );
INSERT into employee_role values ('104', '안석규', '651031-1962810', 'sg_han@kkk.com', '0192347654', '98/07/01', 'J3', 3500000, .25, 'Y', '100', '60','SE' );
INSERT INTO EMPLOYEE_ROLE VALUES ('107', '조재형', '721128-1732822', 'jh_jo@kkk.com', '0193325548', '98/11/23', 'J3', 3800000,null , 'Y', '104', '60', 'SE' );
INSERT INTO EMPLOYEE_ROLE VALUES ('124', '정지현', '641231-2269080', 'jih_jeon@kkk.com', '01922976129', '04/07/15', 'J7', 1500000,null , 'N', '141', '50', 'MKT' );
INSERT INTO EMPLOYEE_ROLE VALUES ('141', '김예수', '651122-2592930', 'hs_kim@kkk.com', '0194087600', '01/03/20', 'J5', 2100000, .1, 'Y', '100', '50', 'MKT' );
INSERT INTO EMPLOYEE_ROLE VALUES ('143', '나승원', '871024-1945881', 'sw_cha@kkk.com', '0197243979', '01/03/20', 'J5', 2300000,null , 'Y', '141', '50', 'MKT' );
INSERT INTO EMPLOYEE_ROLE VALUES ('144', '김순이', '741122-2515789', 'sm_kim@kkk.com', '0192213306', '99/10/20', 'J3', 3400000, .1, 'Y', '141', '50', 'MKT' );
INSERT INTO EMPLOYEE_ROLE VALUES ('149', '성해교', '640524-2148639', 'hg_song@kkk.com', '01992882295', '03/08/16', 'J7', 1900000,null , 'N', '141', '50', 'MKT' );
INSERT INTO EMPLOYEE_ROLE VALUES ('174', '전우성', '821121-1660412', 'ws_jeong@kkk.com', '0193243388', '02/07/14', 'J6', 2090000,null , 'Y', '100', '80', 'SALES-MKT' );
INSERT INTO EMPLOYEE_ROLE VALUES ('176', '엄정하', '791217-2230420', 'jh_um@kkk.com', '0194769665', '04/07/21', 'J6', 2420000, .2, 'Y', '174', '80', 'SALES-MKT' );
INSERT INTO EMPLOYEE_ROLE VALUES ('178', '심하균', '611121-1673370', 'hk_shin@kkk.com', '0197122111', '04/09/30', null, 2300000, .3, 'Y', null, null, null );
INSERT INTO EMPLOYEE_ROLE VALUES ('200', '고승우', '840217-1776881', 'sw_jo@kkk.com', '0193475512', '03/04/11', 'J7', 1500000,null , 'Y', '100', '10', 'HR' );
INSERT INTO EMPLOYEE_ROLE VALUES ('201', '박하일', '891225-1069101', 'hi_park@kkk.com', '01951564413', '04/11/10', 'J5', 2600000, null, 'Y', null, '50', 'MKT' );
INSERT INTO EMPLOYEE_ROLE VALUES ('202', '권상후', '790331-1662986', 'sw_kwon@kkk.com', '0196640090', '01/05/20', 'J6', 3410000, .2, 'Y', '200', '10', 'HR' );                                                                          
INSERT INTO EMPLOYEE_ROLE VALUES ('205', '임영애', '790833-2105839', 'jangum_lee@kkk.com', '0191132477', '00/01/31', 'J6', 2640000, .15, 'N', '200', '10', 'HR' );
INSERT INTO EMPLOYEE_ROLE VALUES ('206', '염정하', '860122-2785746', 'jh_yeum@kkk.com', '01997546623', '03/09/17', 'J7', 1500000,null , 'Y', null, null, null );
INSERT INTO EMPLOYEE_ROLE VALUES ('207', '김술오', '640226-1358242', 'so_kim@kkk.com', '', '96/10/01', 'J4', 2500000,null , 'Y', null, '20', 'FIN' );
INSERT INTO EMPLOYEE_ROLE VALUES ('208', '이중기', '790411-1452247', 'jk_lee@kkk.com', '', '04/10/01', 'J4', 2500000,null , 'Y', null, '20', 'FIN' );
INSERT INTO EMPLOYEE_ROLE VALUES ('210', '감우섭', '700813-1766819', 'manofking@kkk.com', '', '05/07/31', 'J4', 2500000,null , 'Y', null, '20', 'FIN' );


INSERT INTO ROLE_HISTORY VALUES ('104', '98/07/01', '01/12/31', 'SE-PKG', '90' );      
INSERT INTO ROLE_HISTORY VALUES ('176', '04/07/21', '04/12/31', 'MKT', '50' );         
INSERT INTO ROLE_HISTORY VALUES ('104', '02/01/01', '02/12/31', 'SE-ANLY', '90' );     
INSERT INTO ROLE_HISTORY VALUES ('104', '03/01/01', '03/12/31', 'SE', '60' );


SELECT * FROM EMPLOYEE_ROLE;
SELECT * FROM ROLE_HISTORY;

COMMIT;
