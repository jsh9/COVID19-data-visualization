# -*- coding: utf-8 -*-
import pandas as pd
import helper as hlp
import plot_utils as pu  # https://github.com/jsh9/python-plot-utilities

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)

#%%-------------- Load US population by state ---------------------------------
pop_fn = '../auxiliary_data/nst-est2019-alldata.csv'
pop_df = pd.read_csv(pop_fn)

pop_by_state = pop_df.iloc[5:,][['NAME', 'POPESTIMATE2019']].set_index('NAME')
state_name_to_pop = pop_by_state.to_dict()['POPESTIMATE2019']
state_abbrv_to_pop = pu._translate_state_abbrev(state_name_to_pop, abbrev_to_full=False)

#%%------------- Calculate number of tests per capita -------------------------
lookup_population = lambda x: state_abbrv_to_pop[x]
df['population'] = df['state'].apply(lookup_population)
df['tests_per_capita'] = df['total'] / df['population'] * 1e6

trend_df = df.pivot(index='date', columns='state', values='tests_per_capita')
trend_df = trend_df.iloc[40:, :]  # do not plot February data as it is sparse
today = hlp.get_today(trend_df)

#%%---------------- Plot figures ----------------------------------------------
ylabel = 'Tests per million people'

fig, _ = hlp.plot_lines(
    trend_df,
    'Trend (all US states), linear scale',
    ylabel=ylabel,
    logy=False,
)
fig.savefig(
    f'../output_figures/Trend_09__tests_per_capita_{today}.png',
    bbox_inches='tight',
)
