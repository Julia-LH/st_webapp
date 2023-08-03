import streamlit as st


class TableView:
    def __init__(self, df):
        self.df = df

    def show_table(self):
        st.table(self.df)
