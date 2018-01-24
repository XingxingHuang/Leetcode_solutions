-- https://leetcode.com/problems/rising-temperature/
select current_weather.id as 'Id'
from weather as current_weather join weather as prev_weaher
on DATEDIFF(current_weather.date, prev_weaher.date) = 1
    and current_weather.Temperature > prev_weaher.Temperature;
