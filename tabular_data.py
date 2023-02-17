import pandas as pd
import numpy as np
import plotly.express as px
import missingno as msno
from ast import literal_eval

class DataPreparation:


    def __init__(self) -> None:
            self.data_file_path = "tabular_data\listing.csv"
            self.df = pd.read_csv(self.data_file_path)

        
    def remove_rows_with_missing_ratings(self, ratings_columns = ["Description", "Cleanliness_rating", "Accuracy_rating", "Communication_rating", "Location_rating", "Check-in_rating", "Value_rating"]) -> pd.DataFrame:

        df = self.df.dropna(subset=ratings_columns)

        return df


    def combine_description_strings(self):
        
        #remove empty quotes
        #join the list elements
        literal_eval
        

        #remove 'about this space' prefix


        # for item in df["Description"]:
        #     item.remove('About this space')


        #df["Description"] = df["Description"].remove('About this space')
        #df['Description'] = df['Description'].apply(lambda x: ' '.join(x) if type(x)==list else x)
        
        #print(df["Description"].head())
    
        return df

    #combine_description_strings(df)



dataprep = DataPreparation()  
dataprep.remove_rows_with_missing_ratings()  