import pandas as pd
sars_data = pd.read_csv("../data/sars_2003_complete_dataset.csv")
nan_count_per_column = sars_data.isna().sum()

#filtro multiple condition
sars_data['date'] = pd.to_datetime(sars_data['date'])

sars_data[(sars_data["country"]=="Singapore") & (sars_data["date"]==pd.to_datetime("2003-03-17"))]
