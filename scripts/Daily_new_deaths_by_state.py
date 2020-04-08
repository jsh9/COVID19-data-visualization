# -*- coding: utf-8 -*-
import pandas as pd
import helper as hlp

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)
trend_df = df.pivot(index='date', columns='state', values='death').fillna(0)
today = hlp.get_today(trend_df)

#%%-------------- Calculate daily new cases -----------------------------------
previous_day_cases = trend_df.iloc[:-1, :].to_numpy()
present_day_cases = trend_df.iloc[1:, :].to_numpy()
daily_increase = present_day_cases - previous_day_cases

daily_increase_df = pd.DataFrame(
    daily_increase,
    index=trend_df.index[1:],
    columns=trend_df.columns,
)
daily_increase_df = daily_increase_df.iloc[-14:, :]  # only show last two weeks

#%%---------------- Plot figures ----------------------------------------------
ylabel = 'Daily new deaths'

fig, ax = hlp.plot_lines(
    daily_increase_df,
    'Trend (all US states), linear scale',
    ylabel=ylabel,
    logy=False,
    alpha=0.8,
)
fig.savefig(
    f'../output_figures/Trend_14__daily_new_deaths_all_states_{today}.png',
    bbox_inches='tight',
)

fig, ax = hlp.plot_lines(
    hlp.replace_NY_NJ_data_with_NaN_for_easier_plotting(daily_increase_df),
    'Trend (US states, except NY and NJ), linear scale',
    ylabel=ylabel,
    logy=False,
    alpha=0.8,
)
fig.savefig(
    f'../output_figures/Trend_15__daily_new_deaths_all_states_excl_NY_NJ_{today}.png',
    bbox_inches='tight',
)
