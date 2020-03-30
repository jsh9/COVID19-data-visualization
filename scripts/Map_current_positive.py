# -*- coding: utf-8 -*-
import datetime
import pandas as pd
import helper as hlp
import plot_utils as pu  # https://github.com/jsh9/python-plot-utilities
from collections import Counter

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_current.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)

time_stamps = df['checkTimeEt'].apply(lambda x: x.split()[0])
month, day = Counter(time_stamps).most_common(1)[0][0].split('/')
today = datetime.date(year=2020, month=int(month), day=int(day))

#%%
positive = df[['state', 'positive']].set_index('state').to_dict()['positive']
fig, _ = pu.choropleth_map_state(
    positive,
    map_title=f'Positive cases by state ({today})',
    unit='',
    vmax=8000,
    vmin=0,
    dpi=120,
    fontsize=16,
)
fig.savefig(f'../output_figures/Map_01__positive_cases_by_state_{today}.png')

df['pos_rate'] = df['positive'] / df['total'] * 100
pos_rate = df[['state', 'pos_rate']].set_index('state').to_dict()['pos_rate']
fig, _ = pu.choropleth_map_state(
    pos_rate,
    map_title=f'Positive rate by state ({today})',
    unit='[%]',
    vmax=100.0,
    vmin=0.0,
    dpi=120,
    fontsize=16,
)
fig.savefig(f'../output_figures/Map_02__Positive_rate_by_state_{today}.png')
