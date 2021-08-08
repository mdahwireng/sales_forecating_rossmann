import pandas as pd
import numpy as np
import logging


class DateExtract():
    def __init__(self, df) -> None:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('DateExtraction initialized...')
        self.df = df.copy()
        self.df['Date'] = pd.to_datetime(self.df["Date"])
    
    def get_year(self):
        logging.info('Retrieving year from date...')
        df = self.df.copy()
        df['Year'] = df["Date"].dt.year
        self.df = df
        logging.info('Retrieval of year completed')

    def get_month(self):
        logging.info('Retrieving month from date...')
        df = self.df.copy()
        df['Month'] = df["Date"].dt.month
        self.df = df
        logging.info('Retrieval of month completed')

    def get_day(self):
        logging.info('Retrieving day from date...')
        df = self.df.copy()
        df['Day'] = df["Date"].dt.day
        self.df = df
        logging.info('Retrieval of day completed')

    def get_week_month(self):
        logging.info('Retrieving week of the month from date...')
        df = self.df.copy()
        df['WeekOfMonth'] = df["Date"].dt.isocalendar().week%4
        self.df = df
        logging.info('Retrieval of week of the month completed')

    def get_season(self):
        logging.info('Retrieving seasons from date...')
        df = self.df.copy()
        df["Season"] = np.where(df["Month"].isin([3,4]),"Spring",
                                np.where(df["Month"].isin([5,6,7,8]),
                                "Summer",np.where(df["Month"].isin([9,10,11]),
                                "Fall",np.where(df["Month"].isin([12,1,2]),
                                "Winter","None"))))
        self.df = df
        logging.info('Retrieval of seasons from date completed')

    def get_weekends(self):
        logging.info('Retrieving weekends from date...')
        df = self.df.copy()
        df['IsWeekend'] = df["Day"].apply(lambda x: 1 if x>4 else 0)
        logging.info('Retrieval of weekends from date completed')

    def get_weekdays(self):
        logging.info('Retrieving weekdays from date...')
        df = self.df.copy()
        df['IsWeekday'] = df["Day"].apply(lambda x: 1 if x<5 else 0)
        logging.info('Retrieval of weekdays from date completed')

    def get_month_begining(self):
        logging.info('Retrieving begining of month from date...')
        df = self.df.copy()
        df['IsBeginOfMonth'] = df["Day"].apply(lambda x: 1 if x<7 else 0)
        logging.info('Retrieval of begining of month from date completed')

    def get_month_mid(self):
        logging.info('Retrieving middle of month from date...')
        df = self.df.copy()
        df['IsMiddleOfMonth'] = df["Day"].apply(lambda x: 1 if (x>12 & x<18) else 0)
        logging.info('Retrieval of middle of month from date completed')

    def get_month_end(self):
        logging.info('Retrieving end of month from date...')
        df = self.df.copy()
        df['IsMiddleOfMonth'] = df["Day"].apply(lambda x: 1 if x>24 else 0)
        logging.info('Retrieval of end of month from date completed')


    def return_df(self):
        logging.info('Command to return DataFrame issued...')
        df = self.df.copy()
        logging.info('DataFrame returned')
        return df

    def extract_all(self):
        self.get_year()
        self.get_month()
        self.get_day()
        self.get_month()
        self.get_season()
        self.get_weekends()
        self.get_weekdays()
        self.get_month_begining()
        self.get_month_mid()
        self.get_month_end()
        data_df = self.return_df()
        return data_df