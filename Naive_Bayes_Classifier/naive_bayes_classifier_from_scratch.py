import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(file_path_):
    data_set_ = []
    data_frame = pd.read_csv(file_path_)
    for row in data_frame.iterrows():
        data_set_.append(row[1].tolist())
    return data_set_


# Split a data set into a train and test set
def split_data_set(data_set_):
    train_, test_ = train_test_split(data_set_, test_size=0.3)
    return train_, test_


def separate_by_class(data_set_):
    separated = {}
    for i in range(len(data_set_)):
        vector = data_set[i]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated




if __name__ == '__main__':
    file_path = 'data.csv'
    data_set = load_data(file_path)
    train, test = split_data_set(data_set)
