-- https://leetcode.com/problems/combine-two-tables/description/
select FirstName, LastName, City, State
from Person left join Address on Person.PersonId = Address.PersonId;
