-- https://leetcode.com/problems/exchange-seats/description/
select (
    case
        when id mod 2 != 0 and id != total
        then id + 1
        when id mod 2 != 0 and id = total
        then id
        else id -1
    end) as id, student
from seat, (select count(*) as total from seat) as seat_total
order by id asc;
