import pandas as pd


# Read a CSV from URL
data_frame = pd.read_table('data.csv')

# Print first 10 rows
data_frame.head(n=10)

# Number of observations in the data set
data_frame.shape[0]
data_frame.info()

# Number of columns in the data set
data_frame.shape[1]

# Print Name of all the columns
data_frame.columns

# How is the data set indexed?
data_frame.index

# Which item was most ordered item
data_frame.groupby('item_name').quantity.sum().idxmax()

# For the most-ordered item, how many items were ordered?
data_frame.groupby('item_name').quantity.sum().max()

# What was the most ordered item in the choice_description column?
data_frame.groupby('choice_description').quantity.sum().idxmax()

# How many items were ordered in total?
data_frame.quantity.sum()

# Turn the item price into a float

# 1 - Check the item price type
data_frame.item_price.dtype

# 2 - Create a lambda function and change the type of item price
dollarizer = lambda x: float(x[1:-1])
data_frame.item_price = data_frame.item_price.apply(dollarizer)

# How much was the revenue for the period in the dataset?
revenue = (data_frame['quantity'] * data_frame['item_price']).sum()

# How many orders were made in the period?
tot_num_of_orders = data_frame['order_id'].value_counts().count()

# Average Revenue Amount Per Order
multiplier = lambda x: x * x
revenue_df = data_frame.groupby('order_id')['quantity', 'item_price'].sum()
print(revenue_df['quantity'] * revenue_df['item_price'])

# How many different items are sold?
print(data_frame.item_name.value_counts().count())