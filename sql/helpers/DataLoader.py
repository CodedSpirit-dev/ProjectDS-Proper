import pandas as pd


class DataLoader:
    """
    This class is used to load data from a csv file
    """

    def __init__(self, path):
        """
        Constructor for DataLoader class
        """
        self.path = path

    def preprocess_data(self):
        pass

    def load_data(self):
        """
        This method is used to load data from a csv file
        """
        data = pd.read_csv(self.path)
        return data
