# Load pandas library- the common practice is to assign an alias pd
import numpy as np
import pandas as pd
# carete a Pandas series simply by passing a Python list to pd.Series()
s1 = pd.Series([11, 21, 31, 5, 6, 7, 7])

print(s1)


# Specify index
s3 = pd.Series([11, 21, 31],index=['March','April', 'May'])

print(s3)


# # One of the most commonly used methods to do so is with a Python dictionary.
# Create a dictionary
data = {'City': ['San Francisco', 'San Jose','Seattle'],
        'Population': [131000, 40000, 60000]}

print(data)

# We simply pass this dictionary to the DataFrame constructor
df = pd.DataFrame(data)

print(df)


# Create a DataFrame
data = {'Name': ['Lily', 'Emma', 'John'],
        'Age': [38, 15, 28],
        'Education': ['high school', 'phd', 'bachelor'],
        'Gender': [0, 0, 1]}

customer = pd.DataFrame(data)
print(customer)


# Let’s first use the `loc` method to select the first 2 rows and "Age", "Education" columns in the "customer" dataframe
# loc[row label, column label]
print("loc method")
print(customer.loc[ : 1, ["Age","Education"]])



# Let’s do the same operation using the `iloc` method.
# loc[row index, column index]
# start index(inclusive) : end index (exclusive)

print("iloc method")
print(customer.iloc[ : 2,  1 : 3])


# Select column "Education"
print(customer['Education'])


# Select column "Age", "Education"
print(customer[['Education', 'Age']])

# a specific cell by row and column labels
print(customer.at[0, 'Education'])



# Create a dictionary
data = {'Name': ['Lily', 'Emma', 'John'],
        'Age': [38, 15, 28],
        'Education': ['high school', 'phd', 'bachelor'],
        'SexCode': [0, 0, 1]}

# Now the row indexes are integers
df = pd.DataFrame(data)

print(df)


# based on a condition: Filter customers whose name is 'Lily'
filter = customer['Name'] == 'Lily'

customer_filtered1 = customer[filter]

print(customer_filtered1)



# The same as
customer_filtered2 = customer[customer['Name'] == 'Lily']

print(customer_filtered2)


# Age >= 18, and female
filter = (customer['Age'] >= 18) & (customer['Gender'] == 0)
customer_filtered = customer[filter]

print(customer_filtered)
# The Pandas library accepts both Python’s None and NumPy’s np.nan as missing values,
# so we can use both to indicate the missing values.

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan],
    "B": [2.4, 6.2, 5.1, np.nan],
    "C": ["foo","zoo","bar", None]
})


print(df)
# Find out what elemnt is missing
print( df.isna())

 # of missing values in each column
print(df.isna().sum())

# Get # of missing values in each row
print(df.isna().sum(axis=1))

# Get # of missing values in this DataFrame
print(df.isna().sum().sum())

# Find out what elemnt is missing
print(df.notna())


df = pd.DataFrame({
    "A": [1, 2, 3, 4, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": ["phd", "phd","high school","high school", np.nan],
    "D": [3, np.nan, None, None, None]
})

print(df)


# Drop rows that have at least one missing value
print(df.dropna(axis = 0, how = "any"))

# Drop columns that have at least one missing value
print(df.dropna(axis = 1, how = "any"))


# Keep rows that have at least 3 non-missing values
print(df.dropna(axis = 0, thresh = 3))


# Keep columns that have at least 4 non-missing values
print(df.dropna(axis = 1, thresh = 4))



df = pd.DataFrame({
    "account_length": [30, 20, 20, np.nan, 30],
    "gender": ['F', 'M', 'F', np.nan, 'F'],
    "education": ['high school', "high school","high school","high school", np.nan],
})

print(df)

# Replacing the Missing Values with the average value of the column "account_length"
value_to_replace = df["account_length"].mean()

print(value_to_replace)

# fill the missing value with the mean of column
df["account_length"].fillna(value_to_replace)
print(df)

# fill the missing value with the mean of column
df["account_length"].fillna(value_to_replace, inplace=True)
print(df)


# Replacing the Missing Values with the most frequent value in the column "gender"
value_to_replace2 = df["gender"].mode()[0]

print(value_to_replace2)

# fill the missing value with the mode of column and change it inplace
df["gender"].fillna(value_to_replace2, inplace = True)

print(df)

# Let's say we know that last customer's education is "phd"
df["education"].fillna("phd", inplace = True)

print(df)


data = {
    'Date': ['2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04'],
    'Product': ['Product A', 'Product B', 'Product A', 'Product C'],
    'Quantity Sold': [100, 150, 120, 80],
    'Revenue': [5000, 7500, 6000, 4000]
}

# Create a DataFrame
df = pd.DataFrame(data)

print(df)


# We want to easily see proudct from highest revenue to the lowest
# Sort the DataFrame by 'Revenue' column in descending order
print(df.sort_values(by ='Revenue', ascending = False))


# Sample DataFrame
data = {
    'Student_Name': ['Alice', 'Bob', 'Eve', 'David', 'Carol'],
    'Age': [25, 30, 22, 24, 28],
    'Score': [95, 95, 92, 88, 88]
}

df = pd.DataFrame(data)

print(df)

# Sort Score from highest to lowest, we also want to sort the student age from smallest to largest
# Sort by 'Age' in ascending order and then by 'Score' in descending order
print(df.sort_values(by =['Score', 'Age'], ascending=[False, True]))


df = pd.DataFrame({
    "user_id": ["1232as", "1323wv", "134pdf", "342t6ff"],
    "account_length": [31, 0, 0, 23],
    "total_orders": [4, 2, 3, 4],
    "tenure": [np.nan, np.nan, np.nan, np.nan]
})

print(df)

# drop column "user_id" since this column does not have much info
print(df.drop(['user_id'], axis = 1))

# We want to drop two columns 'user_id' and 'tenure' since tenure has all missing values

print(df.drop(['user_id', 'tenure'], axis = 1))


# Note that the original df does not change
# we assign a new variable to `df.drop(['user_id'], axis = 1)`
# OR specify `inplace` to True
print(df)
# drop column "user_id" and made the change inplace

print(df.drop(['user_id'], axis = 1, inplace = True))

# replace 0 in "account_length" to 10
df['account_length'].replace(0, 10, inplace = True)
print(df)

df = pd.DataFrame({
    'product_category': ['baby', 'book', 'book', 'beauty', 'baby'],
    'product_price': [19.99, 12.49, 22, 49, 16],
    'rating': [5, 3, 3, 2, 4]
})

print(df)

# avg rating of amazon product review data
print(df.groupby('product_category')['rating'].mean())


# Use reset_index() to convert the grouped index back to columns
#* The `reset_index()` is used to remove the current index and restore grouped columns to
# a DataFrame,
# which can be particularly useful when you want to work with data in a more organized form.
print(df.groupby('product_category')['rating'].mean().reset_index())
avg_rating_summary = df.groupby('product_category')['rating'].mean().reset_index()

print(avg_rating_summary)


# Use rename function, we want to do it in the same dataframe
avg_rating_summary.rename(columns= {'rating': 'avg_rating'}, inplace = True)

print(avg_rating_summary)


# Select product_category == 'baby'
baby_category = df[df['product_category'] == 'baby']

print(baby_category)

print(baby_category['rating'].mean())


#Pandas-ff1
'''
Write a Python program using Pandas to create a DataFrame from the given data and calculate the average rating of movies directed by Christopher Nolan.





data = {

    'Title': ['Inception', 'Dunkirk', 'Interstellar', 'The Prestige', 'Memento'],

    'Director': ['Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan'],

    'Rating': [8.8, 7.9, 8.6, 8.5, 8.4]

}




'''

data = {

    'Title': ['Inception', 'Dunkirk', 'Interstellar', 'The Prestige', 'Memento'],

    'Director': ['Emma Nolan', 'Jack Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan'],

    'Rating': [8.8, 7.9, 8.6, 8.5, 8.4]

}

df = pd.DataFrame(data)
print(df)
nolan_movie = df[df['Director'] =='Christopher Nolan']
print(nolan_movie)

avg_rating = nolan_movie['Rating'].mean()
print(avg_rating)


#Pandas-FF2
'''
Given the following DataFrame, write a Python program using Pandas to
 extract all rows where the price is greater than or equal to 20,000 and 
 sort them in descending order by price.



data = {

    'Product': ['Laptop', 'Desktop', 'Tablet', 'Phone', 'Smartwatch'],

    'Price': [25000, 12000, 8000, 22000, 5000]

}



df = pd.DataFrame(data)
'''

data = {

    'Product': ['Laptop', 'Desktop', 'Tablet', 'Phone', 'Smartwatch'],

    'Price': [25000, 12000, 8000, 28000, 5000]

}



df = pd.DataFrame(data)
print(df)
filter_df = df[df['Price'] >=20000]
print(filter_df)
dd = filter_df.sort_values(by='Price',ascending=False)
print(dd)


#Pandas-FF3
'''
Write a Python program using Pandas to create a DataFrame from the given data and
 find the total revenue and average price of items sold in each store.

'''

data = {

    'Store': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],

    'Item': ['Apple', 'Banana', 'Orange', 'Grape', 'Apple', 'Banana', 'Orange', 'Grape'],

    'Price': [50, 20, 30, 60, 55, 22, 33, 65],

    'Quantity': [10, 12, 15, 16, 20, 25, 30, 35]

}

df = pd.DataFrame(data)
print(df)
# total revenue of each row
df['Revenue'] = df['Price'] * df['Quantity']

print(df)
store_summary = df.groupby('Store').agg({'Revenue':'sum','Price':'mean'}).reset_index()
print(store_summary)
store_summary.rename(columns={'Price':'Avg_price','Revenue':'Total_Revenue'},inplace=True)
print(store_summary)
'''
ff4
Write a Python program using Pandas to create a DataFrame 
from the given data and calculate the total amount spent by each customer.

'''

data = {

    'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],

    'Item': ['Pen', 'Pencil', 'Notebook', 'Eraser', 'Pen', 'Pencil', 'Notebook', 'Eraser'],

    'Price': [10, 5, 50, 20, 10, 5, 50, 20],

    'Quantity': [3, 4, 2, 5, 10, 6, 1, 2]

}

df = pd.DataFrame(data)
print(df)
df['Total_spent'] = df['Price']*df['Quantity']
print(df)

create_summary = df.groupby('Customer').agg({'Total_spent':'sum'}).reset_index()
print(create_summary)


'''
FF5
Write a Python program using Pandas to create a DataFrame from the given data and
 find the month with the highest average temperature.
'''

data = {

    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],

    'Avg_Temperature': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21]

}



df = pd.DataFrame(data)
print(df)
#loc(rowlable,collable)
highest_avg_temp_month = df.loc[df['Avg_Temperature'].idxmax(),'Month']
print(highest_avg_temp_month)

'''
ff6
Given the following DataFrame and code snippet, predict the output of the code.


'''

data = {

    'Category': ['Fruit', 'Vegetable', 'Fruit', 'Vegetable', 'Fruit', 'Vegetable'],

    'Name': ['Apple', 'Carrot', 'Banana', 'Potato', 'Grape', 'Onion'],

    'Price': [2, 1, 1.5, 0.5, 3, 1],

    'Quantity': [10, 20, 15, 30, 5, 40]

}

df = pd.DataFrame(data)

fruits = df[df['Category'] == 'Fruit']
print(fruits)

total_fruit_value = fruits['Price'].sum() * fruits['Quantity'].sum()

print(total_fruit_value)

'''
ff7
Given the following DataFrame and code snippet, predict the output of the code.


'''

data = {

    'Name': ['Alice', 'Bob', 'Charlie', 'David'],

    'Age': [25, 30, 35, 40],

    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']

}



df = pd.DataFrame(data)

print(df)
#iloc(rowinx,colinx
result = df[df['Age'] >= 30].sort_values(by='Age', ascending=False).iloc[0]['City']

print(result)

'''
ff8 out predict
'''

data = {

    'Product': ['A', 'B', 'C', 'A', 'B', 'C'],

    'Price': [100, 200, 300, 150, 250, 350],

    'Quantity': [10, 5, 7, 12, 8, 5]

}

df = pd.DataFrame(data)
print(df)

total_revenue = (df['Price'] * df['Quantity']).sum()

average_price = df['Price'].mean()

print(total_revenue, average_price)

'''Write a Python program using Pandas to create a DataFrame '
 'from the given data and find the total amount spent per item, '
 'as well as the total amount spent by all customers.')'
'''
data = {

    'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],

    'Item': ['Pen', 'Pencil', 'Notebook', 'Eraser', 'Pen', 'Pencil', 'Notebook', 'Eraser'],

    'Price': [10, 5, 50, 20, 10, 5, 50, 20],

    'Quantity': [3, 4, 2, 5, 10, 6, 1, 2]

}
df = pd.DataFrame(data)
print(df)
df['Total_spent'] = df['Price']*df['Quantity']
print(df)
item_summary =  df.groupby('Item').agg({'Total_spent':'sum'}).reset_index()
print(item_summary)
sum = item_summary['Total_spent'].sum()
print(sum)

'''
FF10
Write a Python program using Pandas to create a DataFrame from the given data and
 calculate the monthly average temperature difference between two cities.


'''

data = {

    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],

    'City_A_Temp': [11, 22, 25, 3, 28, 13, 9, 34, 30, 8, 14, 31],

    'City_B_Temp': [10, 12, 15, 17, 20, 22, 25, 24, 20, 18, 14, 11]

}



df = pd.DataFrame(data)
print(df)
df['Abs_Temp_diff'] = abs(df['City_A_Temp'] - df['City_B_Temp'])
print(df)
avg_diff = df['Abs_Temp_diff'].mean()
print(avg_diff)

