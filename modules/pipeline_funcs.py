from sklearn.base import BaseEstimator, TransformerMixin
from date_handler import DateExtract
from treat_categorical import EncodeCategorical
from xgboost_modeller import XgModeller

class ExtractDateInfo(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        df = X.copy()
        date_obj = DateExtract(df=df)
        date_obj.get_year()
        date_obj.get_month()
        date_obj.get_week_month()
        date_obj.get_season()
        date_obj.get_day()
        date_obj.get_weekdays()
        date_obj.get_weekends()
        date_obj.get_month_begining()
        date_obj.get_month_mid()
        date_obj.get_month_end()
        ext_df = date_obj.return_df()
        return ext_df


class ConvertCategorical(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        pass

    def fit (self, X, y=None):
        df = X.copy()
        encode_cat  = EncodeCategorical(df=df)
        encode_cat.get_cat_cols()
        self.encode_cat = encode_cat
        return self

    def transform(self, X, y=None):
        encode_cat = self.encode_cat
        encoded_df = encode_cat.encode_cats()
        return encoded_df
