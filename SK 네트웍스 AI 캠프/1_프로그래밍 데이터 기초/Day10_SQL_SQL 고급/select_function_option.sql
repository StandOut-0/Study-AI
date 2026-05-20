
select email, upper(email) as upper_email, lower(email) as lower_email
from employee;

select AVG(salary) from employee;
select AVG(DISTINCT salary) from employee;
select AVG(ifnull(salary, 0)) from employee;


SELECT DISTINCT DEPT_ID FROM employee;

SELECT DISTINCT DEPT_ID FROM employee GROUP BY DEPT_ID;

use studentdb;
select case 
    when substr(emp_no, 8, 1) in ('1', '3') then '남'
    else '여'  
    end 성별, sum(salary) from employee 
group by case when substr(emp_no, 8, 1) in ('1', '3') then '남'
    else '여'  
    end;


select max(a.급여합계)
from (select sum(salary) 급여합계 from employee 
    group by dept_id) a;


select dept_id, sum(salary) as 총입사액
from employee
group by dept_id
HAVING sum(`SALARY`) = (select max(a.급여합계) 최대급여합계
from (select sum(salary) 급여합계 from employee 
    group by dept_id) a);