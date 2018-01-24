import pandas as pd

# data
Scores = pd.DataFrame({"Id": [1,2,3,4,5,6], "Score": [3.5, 3.65, 4.0, 3.85, 4.0, 3.65]})
print(Scores)

# using loops
results = []
for _, [_, outer_score] in Scores.iterrows():
    better_scores = []
    for _, [_, inner_score] in Scores.iterrows():
        if inner_score >= outer_score:
            better_scores.append(inner_score)
            rank = len(set(better_scores))
    results.append([outer_score, rank])

results = pd.DataFrame(results, columns = ["Score", "Rank"]).sort_values("Rank")
print(results)

# using rank function
Scores["Rank"] = Scores.Score.rank(method = "dense", ascending = False).astype(int)
print(Scores.sort_values("Rank")[["Score", "Rank"]])
