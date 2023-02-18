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


    def clean_description_strings(self, x: str):
        
        try:
            cleaned_x = literal_eval(x)
            cleaned_x.remove("About this space")
            cleaned_x = "".join(cleaned_x)
            return cleaned_x

        except Exception as e:
            
            return x

    
    def combine_description_strings(self, df):
        
        '''This function takes in a dataframe and returns a dataframe with the "Description" column cleaned up
        
        Parameters
        ----------
        df
            the dataframe
        
        Returns
        -------
            A dataframe with the description column cleaned.
        '''
        
        df["Description"] = df["Description"].apply(self.clean_description_strings)
        df['Description'].replace([r"\\n", "\n", r"\'"], [" "," ",""], regex=True, inplace=True)
        #print(self.df['Description'][0])
        
        return df



dataprep = DataPreparation()  
dataprep.remove_rows_with_missing_ratings()
dataprep.combine_description_strings(dataprep.df)