import pandas as pd  # type: ignore

#1 Series
data1 = [10, 20, 30]
series = pd.Series(data1)
print(series)

#2 Series with dictionary
data2 = {'a': 10, 'b': 20, 'c': 30}
series2 = pd.Series(data2)
print(series2)

#3 DataFrame with list
data3 = [
    [1,'Alice',30],
    [2,'Bob',35],
    [3,'Charlie',25]
    ]
df = pd.DataFrame(data3, columns=['ID','Name','Age'])
print(df)

#4 DataFrame with dictionary
data4 = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 35, 25]
    }
df2 = pd.DataFrame(data4,columns=['ID','Name','Age'])

#5 Add a new column
df2 = df2.sort_values('ID')
df2['Salary'] = [50000, 60000, 70000]
df2.loc[len(df2)] = [4, 'David', 40, 80000]
#df2=df2.drop(0)
print(df2)

print('-'* 30)

#6 Concatenate two DataFrames <행 병합>
data5 = {
    'ID': [5, 6],
    'Name': ['Eve', 'Frank'],
    'Age': [28, 33],
    'Salary': [90000, 100000]
    }   
df3 = pd.DataFrame(data5, columns=['ID','Name','Age','Salary'])
df3 = pd.concat([df2, df3])
print(df3)

#7 Merge two DataFrames <열 병합>
data6 = {
    'ID' : [1,2,3,4,5,6],
    'Dept' : ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT']
}

df4 = pd.DataFrame(data6)
merged = pd.merge(df3, df4)
print(merged)

print(df4.isnull().sum()) #결측값 확인
print(df4.duplicated()) #중복확인





