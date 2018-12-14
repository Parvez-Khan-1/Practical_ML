import pandas as pd

# Import dataset
data_frame = pd.read_table('data.csv')

# clean the item_price column and transform it in a float
data_frame.item_price = [float(value[1:-1]) for value in data_frame.item_price]

# deletes duplicates in item_name and quantity
duplicates_filtered = data_frame.drop_duplicates(['item_name', 'quantity'])

# Selects product quantity is 1
data_frame[data_frame.quantity == 1]

#  What is the price of each item?
data_frame[['item_name', 'item_price']]

# Sort by the name of the item
data_frame.sort_values(by=['item_name'], ascending=True)

# What was the quantity of the most expensive item ordered?
data_frame.groupby('quantity')['item_price'].max().idxmax()

# How many times were a Veggie Salad Bowl ordered?
len(data_frame[data_frame['item_name'] == 'Veggie Salad Bowl'])

len(data_frame[(data_frame.item_name == 'Canned Soda') & (data_frame.quantity > 1)])

