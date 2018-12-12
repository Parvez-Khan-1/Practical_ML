import pandas as pd

# Create a Simple DataFrame with values

data_frame = pd.DataFrame(columns=['value', 'word'])

# Add data to the data_frame
data_frame = data_frame.append([{'value': 1, 'word': 'one'},
                                {'value': 2, 'word': 'two'},
                                {'value': 3, 'word': 'three'},
                                {'value': 4, 'word': 'four'}], ignore_index=True)


# Add a new column to data frame with values
data_frame['double'] = data_frame['value'] * 2

# get only even type rows based on value in double column
print(data_frame[data_frame['value'] % 2 == 0])