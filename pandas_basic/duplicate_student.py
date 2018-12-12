import pandas as pd


data_frame = pd.DataFrame({
    'name': ['A', 'B', 'C', 'A', 'D', 'C'],
    'roll': [1, 2, 3, 1, 4, 3],
    'status': ['Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Fail'],
    'ml_marks': [50, 55, 60, 65, 70, 75]
})

print(data_frame)
print('-'*25)
print(data_frame[data_frame[['name', 'roll']].duplicated(keep=False)])