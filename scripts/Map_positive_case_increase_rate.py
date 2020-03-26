# -*- coding: utf-8 -*-
import datetime
import pandas as pd
import helper as hlp
import plot_utils as pu  # https://github.com/jsh9/python-plot-utilities

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)
trend_df = df.pivot(index='date', columns='state', values='total')

today = hlp.get_today(trend_df)
three_days_ago = today - datetime.timedelta(days=3)
three_day_increase = trend_df.iloc[-1,:] - trend_df.iloc[-4,:]

fig, ax = pu.choropleth_map_state(
    three_day_increase,
    map_title=f'New cases, from {three_days_ago} to {today}',
    unit='',
    vmax=15000,
    vmin=0,
    dpi=120,
    fontsize=16,
)

fig_name = f'../output_figures/Map_03__new_cases_from_{three_days_ago}_to_{today}.png'
fig.savefig(fig_name)
