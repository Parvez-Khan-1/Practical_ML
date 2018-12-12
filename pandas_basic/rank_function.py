import pandas as pd


def one_way():
    data_frame = pd.DataFrame(columns=['OrgName', 'Revenue'])

    data_frame = data_frame.append([{'OrgName': 'Synerzip', 'Revenue': 5555555555.63},
                                    {'OrgName': 'Persistent', 'Revenue': 1256.00},
                                    {'OrgName': 'Cognizant', 'Revenue': 2555555.12},
                                    {'OrgName': 'Accenture', 'Revenue': 55555.56},
                                    {'OrgName': 'ITC', 'Revenue': 355555555.88}], ignore_index=True)
    return data_frame


def second_way():
    data_frame = pd.DataFrame(
        {
            'OrgName': ['Synerzip', 'Persistent', 'Cognizant', 'Accenture', 'ITC'],
            'Revenue': [5555555555.63, 1256.00, 2555555.12, 55555.56, 355555555.88]
        }
    )

    return data_frame


def third_way():
    data_frame = pd.DataFrame(
        [['Synerzip'], ['Persistent'], ['Cognizant'], ['Accenture'], ['ITC']],
        columns=['OrgName'],
        index=pd.Index([5555555555.63, 1256.00, 2555555.12, 55555.56, 355555555.88], name='Revenue')
    )
    return data_frame


def using_rank_func(data_frame):
    data_frame['Top_Rank_Org'] = data_frame['Revenue'].rank(ascending=False)
    return data_frame


if __name__ == '__main__':
    data_frame = one_way()
    print(using_rank_func(data_frame))
