# -*- coding: utf-8 -*-
import pandas as pd
import helper as hlp

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)

df['positive_rate'] = df['positive'] / df['total'] * 100
trend_df = df.pivot(index='date', columns='state', values='positive_rate')
today = hlp.get_today(trend_df)

#%%---------------- Plot figures ----------------------------------------------
ylabel = 'Positive rate [%]'

fig, ax = hlp.plot_lines(
    trend_df,
    'Trend (all US states), linear scale',
    ylabel=ylabel,
    logy=False,
)
ax.set_ylim(0, 30)
fig.savefig(
    f'../output_figures/Trend_07__positive_rate_all_states_{today}.png',
    bbox_inches='tight',
)

fig, ax = hlp.plot_lines(
    hlp.replace_NY_NJ_data_with_NaN_for_easier_plotting(trend_df),
    'Trend (US states, except NY and NJ), linear scale',
    ylabel=ylabel,
    logy=False,
)
ax.set_ylim(0, 30)
fig.savefig(
    f'../output_figures/Trend_08__positive_rate_all_states_excl_NY_NJ_{today}.png',
    bbox_inches='tight',
)
