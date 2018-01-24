/* https://leetcode.com/problems/not-boring-movies/description/ */
select * from cinema
where id mod 2 != 0 and description != 'boring'
order by rating desc;
