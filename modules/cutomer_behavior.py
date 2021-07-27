import datetime
import logging

def get_season_df(df, season_col, season_val):
    data = df.copy()
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Retrieving season index...')
    season_idx = data[season_col] == season_val
    logging.info('Extracting season data...')
    season_df = data[season_idx]
    logging.info('Process completed data returned.')
    return season_df

def get_perod_bf_season(train_df, season_df, days_bf):
    train_cp = train_df.copy()
    season_cp = season_df.copy()
    season_cp['before'] = season_cp['Date'].apply(lambda x:x-datetime.timedelta(days=days_bf))
    bef_dates = list(set(season_cp['before']))
    bef_dates_idx = train_cp['Date'].apply(lambda x:x in bef_dates)
    bef_df = train_cp[bef_dates_idx]
    return bef_df

def get_perod_aft_season(train_df, season_df, days_aft):
    train_cp = train_df.copy()
    season_cp = season_df.copy()
    season_cp['after'] = season_cp['Date'].apply(lambda x:x+datetime.timedelta(days=days_aft))
    aft_dates = list(set(season_cp['after']))
    aft_dates_idx = train_cp['Date'].apply(lambda x:x in aft_dates)
    aft_df = train_cp[aft_dates_idx]
    return aft_df

def get_day_name(x):
    name_dict = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    return name_dict[x]