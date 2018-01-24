import pandas as pd

Logs = pd.DataFrame({
    "Id": [1,2,3,4,5,6,7],
    "Num": [1,1,1,2,1,2,2]
})

def find_n_consecutive_repeats(df, col, n):
    assert n >= 2, "n need to be equal or greater than 2"
    original = df[col]
    shifted = df[col].shift()
    selector = original == shifted
    for i in range(2, n):
        original = shifted.copy()
        shifted = shifted.shift()
        selector = selector & (original == shifted)
    return df.loc[selector]

print(find_n_consecutive_repeats(Logs, "Num", 2))

print(find_n_consecutive_repeats(Logs, "Num", 3))
