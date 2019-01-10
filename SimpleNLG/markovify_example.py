import pandas as pd
import markovify

data_frame = pd.read_csv('abcnews-date-text.csv')

nlg_model = markovify.NewlineText(data_frame.headline_text, state_size=2)

for i in range(5):
    print(nlg_model.make_sentence())