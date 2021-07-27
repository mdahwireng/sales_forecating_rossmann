import pandas as pd
import dvc.api

def get_csv_data(path, version):
    rev=version
    print('Reading data from dvc source....')
    data_url = dvc.api.get_url(path=path, rev=rev)
    df = pd.read_csv(data_url)
    print('Reading completed, data returned')
    return df

def save_csv(df, path):
    df.to_csv(path, index=False)
    print('Data saved as {}'.format(path))