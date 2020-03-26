# -*- coding: utf-8 -*-
import pandas as pd
import helper as hlp

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)
trend_df = df.pivot(index='date', columns='state', values='total')
today = hlp.get_today(trend_df)

#%%---------------- Plot figures ----------------------------------------------
ylabel = 'Number of tests performed'

fig, ax = hlp.plot_lines(
    trend_df,
    'Trend (all US states), linear scale',
    ylabel=ylabel,
    logy=False,
)
fig.savefig(
    f'../output_figures/Trend_05__number_of_tests_all_US_states__linear__{today}.png',
    bbox_inches='tight',
)

fig, ax = hlp.plot_lines(
    trend_df,
    'Trend (all US states), log scale',
    ylabel=ylabel,
    logy=True,
)
fig.savefig(
    f'../output_figures/Trend_06__number_of_tests_all_US_states__log__{today}.png',
    bbox_inches='tight',
)
