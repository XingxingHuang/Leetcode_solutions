-- https://leetcode.com/problems/customers-who-never-order/description/
select Name as 'Customers'
from Customers
where Customers.Id not in (select CustomerId from Orders);
