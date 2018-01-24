-- https://leetcode.com/problems/rank-scores/description/
select Score, (
    select count(distinct inner_score.Score) from Scores inner_score
    where inner_score.Score > outer_score.Score
    ) as Rank
from Scores as outer_score
order by Score desc;
