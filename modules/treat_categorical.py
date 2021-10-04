import logging

class EncodeCategorical():
    def __init__(self, df) -> None:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('EncodeCategorical initialized...')
        self.df = df.copy()

    def get_cat_cols(self):
        logging.info('Retrieving categorical columns from Dataframe...')
        df = self.df.copy()
        cat_cols = list(df.select_dtypes(include=[object]).columns)
        self.cat_cols = cat_cols
        logging.info('Retrieval of categorical columns from Dataframe completed')

    def encode_cats(self):
        logging.info('Encoding categorical columns from Dataframe...')
        df = self.df.copy()
        cat_cols = self.cat_cols
        for col in cat_cols:
            if col != 'Date':
                logging.info('Encoding {} column...'.format(col))
                df[col] = df[col].astype('category')
                df[col] = df[col].cat.codes
        logging.info('Encoding categorical columns from Dataframe completed')
        return df
        