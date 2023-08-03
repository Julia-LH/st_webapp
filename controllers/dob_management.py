from models.dob_management import DobModel
from views.table import TableView


def app():
    dob_model = DobModel()
    df = dob_model.get_data()
    table_view = TableView(df)
    table_view.show_table()
