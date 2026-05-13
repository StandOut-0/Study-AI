use studentdb;


select * from employee;
select * from department;
select * from job;


select emp_id, emp_name, emp_no, salary*12 from employee;
select emp_id as 사번, emp_name 이름, substr(emp_no, 1, 6) 주민번호, salary*12 연봉 from employee;


alter table employee 
MODIFY marriage char(1) 
CHARACTER set utf8mb4 COLLATE utf8mb4_bin;

create DATABASE testdb CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
alter DATABASE scottdb CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

show variables like '%address%';
set sql_mode = 'ansi_quotes';
select "emp_id", "emp_name", "emp_no"from employee;
SET sql_mode = DEFAULT;
SELECT @@sql_mode;

-- join using 연결할 컬럼명 두케이블의 컬럼명 같을때
select emp_id 사번, `EMP_NAME` 이름, `JOB_ID` 직급코드 from employee
join job USING (job_id)
where `JOB_ID` = 'j4'


-- on 조건으로 연결
select e.emp_id 사번, e.`EMP_NAME` 이름, e.`JOB_ID` 직급코드 
from employee e
join job j on j.job_id = e.job_id
where j.`JOB_ID` = 'j4'

-- inner join 공통된것만
select e.emp_id 사번, e.`EMP_NAME` 이름, e.`JOB_ID` 직급코드 
from employee e
inner join job j on j.job_id = e.job_id
where j.`JOB_ID` = 'j4'

-- left join 왼쪽기준 매칭없으면 null
select e.emp_id 사번, e.`EMP_NAME` 이름, e.`JOB_ID` 직급코드 
from employee e
left join job j on j.job_id = e.job_id

-- right join 오른쪽기준 매칭없으면 null
select e.emp_id 사번, e.`EMP_NAME` 이름, e.`JOB_ID` 직급코드 
from employee e
right join job j on j.job_id = e.job_id

-- ifnull(null이있는 컬럼명, 바꿀값), coalesce(null이있는 컬럼명, 바꿀값)
select emp_id, salary, bonus_pct, 
round(salary + (salary *bonus_pct)) 
as salary_with_bonus
from employee;
select emp_id, salary, bonus_pct, 
round((salary + (salary * ifnull(bonus_pct, 0))) )
as salary_with_bonus
from employee;
select emp_id, salary, bonus_pct, 
round((salary + (salary * coalesce(bonus_pct, 0))) )
as salary_with_bonus
from employee;

select distinct marriage from employee;

select now() as '현재시각', CURRENT_TIMESTAMP as '시스템타임스탬프';

SELECT NOW() AS '오늘날짜',
       DATE_ADD(NOW(), INTERVAL 1000 DAY) AS '1000일 뒤';

SELECT NOW() AS '오늘날짜',
       DATE_sub(NOW(), INTERVAL 1000 DAY) AS '1000일 전';

select * from employee ;

SELECT *,
       CONCAT(EMP_NAME, '님')
FROM employee
WHERE HIRE_DATE BETWEEN '2015-01-01' AND '2021-12-31';

select emp_name 이름, concat(hire_date, '입사') 입사일,
job_id 직급코드, dept_id 전공코드
from employee
where `HIRE_DATE` >= '2015-01-01' and `HIRE_DATE` <= '2021-12-31'