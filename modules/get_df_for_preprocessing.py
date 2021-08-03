import pandas as pd
import numpy as np

class GetDfForPreprocessing:
    """
    this function will prepare data form dataframe for preprocessing
    
    Return
    ------
    dataframe
    """
    def __init__(self, df:pd.DataFrame):
        
        self.df = df.copy()
        
    def print_df_info(self) -> None:
        """
        this function will print the info of the datafame

        Return
        ------
        None
        """
        print('Retrieving info from data...')
        #save the number of columns and names
        col_info = 'The number of colum(s): {}.\nThe column(s) is/are : {} and {}\n'.format(len(self.df.columns),', '.join(self.df.columns[:-2]), self.df.columns[-1])  
        
        #save the number of rows
        num_rows = "\nThe total number of rows: {}".format(len(self.df))
        
        na_cols = list(self.df.columns[self.df.isnull().any()])
        
        #save the number of missing values
        num_na_cols = "\nThe number of columns having missing value(s): {}".format(len(na_cols))
        
        #save the columns with missing value and the num of values missing
        na_cols_num_na = ''
        
        na_col_val_dict = {}
        for col in na_cols:
            missing_vals = self.df[col].isnull().sum()
            na_col_val_dict[col] = missing_vals
            na_cols_num_na += "\nThe number of rows with missing value(s) in [{}]: {}".format(col, missing_vals)
        
        # save the total number of missing values
        tot_na = "\nThe total number of missing value(s): {}".format(self.df.isnull().sum().sum())
        
        self.na_cols = na_cols
        self.na_col_val_dict = na_col_val_dict
        
        print(col_info, num_rows, num_na_cols, na_cols_num_na)
        
        
    def drop_cols_abv_na_trshld(self, threshold:float, exclude=[], output=False) -> pd.DataFrame:
        """
        this function will drop columns with missing values above a specified threshold

        Return
        ------
        dataframe
        """
        print('\nComparing threshold with fraction of missing values ...')
        df = self.df.copy()
        try:
            if self.na_col_val_dict:
                na_col_val_dict = self.na_col_val_dict
                na_cols = self.na_cols
        except:
            na_cols = df.columns[df.isnull().any()]
            na_col_val_dict = {}
            for col in na_cols:
                missing_vals = df[col].isnull().sum()
                na_col_val_dict[col] = missing_vals
            
        tot_entries = len(df)
        above_treshold = []
        
        print('\nRetrieving columns to be dropped ...')
        for col in na_cols:
            if na_col_val_dict[col] > threshold * tot_entries:
                above_treshold.append(col)
                
        print('\nColumns to be dropped :', above_treshold)
        print('\nThe column(s) to be excluded is/are {}'.format([exclude]))
        if len(exclude)>0:
            for col in exclude:
                above_treshold.remove(col)
                
        print('\nDropping columns with missing values above the threshold ...') 
        df.drop(above_treshold, axis=1, inplace=True)
        print('\nDropping columns completed')

        print('\nRemoving dropped columns from memory...')
        for col in above_treshold:
            na_cols.remove(col)
            del na_col_val_dict[col]
        print('\nRemoval of dropped columns from memory completed')

        self.na_col_val_dict = na_col_val_dict
        self.na_cols = na_cols
        self.df = df.copy()
        if output:
            return df

    def fill_missing(self, exclude=['CompetitionOpenSinceMonth'], method={'num':'mean'}):
        df = self.df.copy()
        na_col_val_dict = self.na_col_val_dict
        na_cols = self.na_cols
        print('\nThe colums with missing values to be filled are {}'.format(na_cols))
        print('\nThe column(s) to be excluded is/are {}'.format(exclude))
        
        if len(exclude)>0:
            for col in exclude:
                na_cols.remove(col)

        for col in na_cols:
            print('\nFilling missing values in {}'.format(col))
            if(df[col].dtype == np.float64 or df[col].dtype == np.int64):
                if method['num'] == 'mean':
                    df[col].fillna(df[col].mean(), inplace=True)
                else:
                    df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)

        print('\nFilling missing values comppleted')
        return df
