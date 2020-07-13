"""
Implementation in Python using an OOP approach
"""

import os
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

FILE_PATH = '../resources'


class DNet(object):

    def __init__(self):
        self._ctg_file = os.path.join(FILE_PATH, "Categorisation.csv")
        self._lst_file = os.path.join(FILE_PATH, "Listings.csv")
        self._opioids_df = pd.DataFrame(columns=["date", "Opioids"])

        self._read_csv()

    def _read_csv(self):
        #  read Listings.csv into a dataframe
        self._lst_df = pd.read_csv(self._lst_file, sep=',')
        #  convert the date column from object to datetime format
        self._lst_df['date'] = pd.to_datetime(self._lst_df['date'], format='%Y/%m/%d')

        #  read Categorisation.csv into a dataframe
        self._ctg_df = pd.read_csv(self._ctg_file, sep=',')

    def update_listing(self):
        #  we can simply use pandas Timedelta method and passing the desired # of 'month' argument to change the date
        print("===========")
        print("Question 1:")
        print("")
        print("Listings date BEFORE update: (showing head only)")
        print(self._lst_df["date"].head())

        self._lst_df["date"] = self._lst_df["date"].apply(lambda x: x - pd.Timedelta(1, unit='M'))
        self._lst_df["date"] = self._lst_df["date"].dt.strftime('%d/%m/%Y')
        self._lst_df['date'] = pd.to_datetime(self._lst_df['date'], format='%d/%m/%Y')

        print("")
        print("Listings date AFTER update: (showing head only)")
        print(self._lst_df["date"].head())

    def create_broader_class_column(self):
        #  creating the empty column first
        self._lst_df["Broader class"] = ""

        #  we can iterate over the Listings' Level 1 column and pass the matched value from 'Broadest class' in
        #  Categorisation dataframe to our new column
        for index, item in enumerate(self._lst_df["Level 1"]):
            broader_class = self._ctg_df.loc[self._ctg_df['Level 1'] == item]["Broadest class"]
            self._lst_df["Broader class"].loc[index] = broader_class.values[0]

        print("===========")
        print("Question 2:")
        print("Listings with Broader class added: (showing head only)")
        print(self._lst_df.head())

    def generate_new_df(self):
        #  we need to copy the unique dates from the Listing dataframe to our new dataframe
        self._opioids_df["date"] = self._lst_df["date"].unique()
        #  then, we need to find the number of opioids classes for every unique dates. This can be achieved by
        #  simply using groupby() and count() methods id pandas.DataFrame
        opioids_count = self._lst_df[self._lst_df["Broader class"] == 'Opioids'].groupby(['date'])['date'].count()

        #  we now have to loop through the unique dates and check how many opioids there are in the corresponding field
        #  save in the opioids_count. That value will be assigned to the respective index. Otherwise a zero value will
        #  be assigned
        for index, item in enumerate(self._opioids_df["date"]):
            if item in list(opioids_count.keys()):
                count = opioids_count[opioids_count.keys() == item].values[0]
                self._opioids_df["Opioids"].loc[index] = count
            else:
                self._opioids_df["Opioids"].loc[index] = 0

        print("===========")
        print("Question 3:")
        print("Opioids dataframe: (showing head only)")
        print(self._opioids_df)

        self._export_to_csv()
        print("")
        print("opioids.csv is saved in the resources directory.")

    def _export_to_csv(self):
        self._opioids_df.to_csv(os.path.join(FILE_PATH, "opioids.csv"), sep=',')


if __name__ == '__main__':
    dnet = DNet()

    #  Q1:
    dnet.update_listing()

    #  Q2:
    dnet.create_broader_class_column()

    #  Q3:
    dnet.generate_new_df()
