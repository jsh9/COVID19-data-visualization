# -*- coding: utf-8 -*-
import pandas as pd
import helper as hlp

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)
trend_df = df.pivot(index='date', columns='state', values='positive')
today = hlp.get_today(trend_df)

#%%---------------- Plot figures ----------------------------------------------
ylabel = 'Positive cases'

fig, ax = hlp.plot_lines(
    trend_df,
    'Trend (all US states), linear scale',
    ylabel,
    logy=False,
)
fig.savefig(
    f'../output_figures/Trend_01__positive_cases_all_US_states__linear_scale__{today}.png',
    bbox_inches='tight',
)

fig, ax = hlp.plot_lines(
    trend_df,
    'Trend (all US states), log scale',
    ylabel,
    logy=True,
)
fig.savefig(
    f'../output_figures/Trend_02__positive_cases_all_US_states__log_scale__{today}.png',
    bbox_inches='tight',
)

fig, ax = hlp.plot_lines(
    hlp.replace_NY_NJ_data_with_NaN_for_easier_plotting(trend_df),
    'Trend (US states, except NY and NJ), linear scale',
    ylabel,
    logy=False,
)
fig.savefig(
    f'../output_figures/Trend_03__positive_cases_all_states_excl_NY_NJ__linear_scale__{today}.png',
    bbox_inches='tight',
)

fig, ax = hlp.plot_lines(
    hlp.replace_NY_NJ_data_with_NaN_for_easier_plotting(trend_df),
    'Trend (US states, except NY and NJ), log scale',
    ylabel,
    logy=True,
)
fig.savefig(
    f'../output_figures/Trend_04__positive_cases_all_states_excl_NY_NJ__log_scale__{today}.png',
    bbox_inches='tight',
)
