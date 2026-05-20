-- 실습 : 제약조건이 설정된 테이블 만들기
-- 테이블명 : PHONEBOOK
-- 컬럼명 :  ID  CHAR(3) 기본키(저장이름 : PK_PBID)
--         PNAME      VARCHAR(20)  널 사용못함.
--         PHONE      VARCHAR(15)  널 사용못함
--                                 중복값 입력못함
--                                 (UN_PBPHONE)
--         ADDRESS    VARCHAR(100) 기본값 지정함
--                                 '서울시 구로구'

-- NOT NULL을 제외하고, 모두 테이블 레벨에서 지정함.


create table PHONEBOOK (
    ID CHAR(3),
    PNAME VARCHAR(20) NOT NULL,
    PHONE VARCHAR(15) NOT NULL,
    ADDRESS VARCHAR(100) DEFAULT '서울시 구로구',

    CONSTRAINT PK_PBID PRIMARY KEY (ID),
    CONSTRAINT UN_PBNAME UNIQUE (PNAME)
)


create or REPLACE view v_emp
AS
select * from employee
where `SALARY`>1000;

select * from v_emp;


set autocommit=0;
alter table emp5
add constraint pk_eid PRIMARY KEY (emp_id);

SELECT * from emp5;

update emp5
set emp_id='777'
where emp_id='A10';

rollback;