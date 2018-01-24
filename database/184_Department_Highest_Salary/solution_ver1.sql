-- https://leetcode.com/problems/department-highest-salary/description/

select D.Name as "Department", E.Name as "Employee", E.Salary as "Salary"
from Employee E join Department D on D.Id = E.DepartmentId
where (E.DepartmentId, E.Salary) in
    (select DepartmentId, max(Salary)
     from Employee
     group by DepartmentId
    );
