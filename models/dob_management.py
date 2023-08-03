from config import dob_db
import pandas as pd


class DobModel:
    def __init__(self):
        self.dob_db = dob_db

    def get_data(self):
        df = pd.read_csv(self.dob_db)
        return df
