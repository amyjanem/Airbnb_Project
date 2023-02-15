import pandas as pd
import numpy as np
import plotly.express as px
import missingno as msno

#print(np.sort(df['beds'].unique()))

#print(df.iloc[1])
#print(df.info())

#df_null = df.isnull()
#print(df_null)
#print(df_null.sum())
#print(df_null.mean()*100)

#msno.matrix(df)


def remove_rows_with_missing_ratings(dataset = "tabular_data\listing.csv", ratings_columns = ("Cleanliness_rating", "Accuracy_rating", "Communication_rating", "Location_rating", "Check-in_rating", "Value_rating")):

    df = pd.read_csv(dataset)
    df_missing_ratings_removed = df.dropna(subset=[ratings_columns])

    return df_missing_ratings_removed

remove_rows_with_missing_ratings()