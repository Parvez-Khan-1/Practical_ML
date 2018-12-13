import pandas as pd


# Assign it to a variable called users and use the 'user_id' as index
data_frame = pd.read_csv('data', sep='|', index_col='user_id')

# show first 25 records
data_frame.head(n=25)

# show last 10 records
data_frame.tail(n=10)

# Number of observations in the data set
data_frame.shape[0]

# Number of Columns in the dataset
data_frame.shape[1]

# Print Names of all columns
data_frame.columns.tolist()

# How is the dataset indexed?
data_frame.index

# What is the data type of each column
data_frame.dtypes

# Print only the occupation column
data_frame.occupation
#OR
data_frame['occupation']

# How many different occupations there are in this dataset?
data_frame.occupation.value_counts().count()
# OR
data_frame.occupation.nunique()

# What is the most frequent occupation?
data_frame.groupby('occupation')['occupation'].count().idxmax()
# OR
data_frame.occupation.value_counts().head()

# Summarize the DataFrame.
data_frame.describe()

# Summarize all the columns
data_frame.describe(include='all')

# Summarize only occupation column
data_frame.occupation.describe()

# What is the mean age of users?
round(data_frame.age.mean())

# What is the age with least occurrence?
data_frame.groupby('age')['age'].count().idxmin()
