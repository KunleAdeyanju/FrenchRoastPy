import pandas as pd


class customer():
    def __init__(self,csv_file):
        self.csv_file = csv_file
        
    def create_dataframe(self):
        df = pd.read_csv(self.csv_file)
        return df