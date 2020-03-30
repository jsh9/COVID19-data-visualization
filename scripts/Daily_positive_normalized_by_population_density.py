# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import helper as hlp
import plot_utils as pu  # https://github.com/jsh9/python-plot-utilities

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)
trend_df = df.pivot(index='date', columns='state', values='positive')
today = hlp.get_today(trend_df)

#%%---------------- Read population density data ------------------------------
pop_density_filename = 'https://github.com/jsh9/python-plot-utilities/raw/master/examples/datasets/DEC_10_SF1_GCTPH1.US05PR_with_ann.csv'

d0 = pd.read_csv(
    pop_density_filename,
    header=1,
    dtype={'Target Geo Id2': str},
    encoding='latin1'
)  # read raw data
USA_avg = d0.iloc[0,-2]  # national average population density
d1 = d0.iloc[1:,[4,-2]]  # only extract useful columns
d1.columns = ['FIPS_code','pop_density']  # rename columns

state_data  = d1.iloc[np.where(np.array(d1['FIPS_code'].astype(float)) <= 100)[0]]
state_data = state_data.iloc[:-1,:].set_index('FIPS_code') # exclude Puerto Rico
state_data = state_data.to_dict()['pop_density']
state_data = pu._convert_FIPS_to_state_name(state_data)
state_data = pu._translate_state_abbrev(state_data, abbrev_to_full=False)

#%%---------------- Normalize by population density ---------------------------
for state in trend_df:
    trend_df[state] = trend_df[state] / state_data[state]
# END FOR

#%%---------------- Plot figures ----------------------------------------------
ylabel = ''
title = 'Number of positive cases normalized by population density\n'
title += r'(Unit: $\frac{\mathrm{\# positive}}{\mathrm{\# residents\,/\,miles}^2}$)'

fig, ax = hlp.plot_lines(
    trend_df,
    title,
    ylabel,
    logy=False,
)
fig.savefig(
    f'../output_figures/Trend_10__positive_normalized_by_pop_density__linear__{today}.png',
    bbox_inches='tight',
)
