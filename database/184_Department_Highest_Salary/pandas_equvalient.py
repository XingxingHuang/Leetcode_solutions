import pandas as pd

Employee = pd.DataFrame({
    "Id": [1,2,3,4],
    "Name": ["Joe", "Henry", "Sam", "Max", "Sara"],
    "Salary": [70000, 80000, 60000, 90000, 90000],
    "DepartmentId": [1,2,2,1]
})

Department = pd.DataFrame({
    "Id": [1,2],
    "Name": ["IT", "Sales"]
})

results = Employee.groupby("DepartmentId").agg({'Salary': max}).reset_index()
results = results.merge(right = Employee, how = "left")
results = results.merge(right = Department, how = "left")

print(results)
