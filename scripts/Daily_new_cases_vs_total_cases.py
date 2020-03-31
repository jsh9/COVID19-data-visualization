# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import helper as hlp
import plot_utils as pu  # https://github.com/jsh9/python-plot-utilities
import matplotlib.pyplot as plt

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
hlp.exclude_overseas_territory_records(df)
trend_df = df.pivot(index='date', columns='state', values='positive')

today = hlp.get_today(trend_df)
n = 3  # time window (unit: days) to calculate new cases
linespecs = pu.get_linespecs(range_linewidth=[1,3,5])

plt.figure(figsize=(10, 4), dpi=120)
for j in range(len(trend_df.columns)):
    state = trend_df.columns[j]
    state_data = np.array(trend_df[state])
    total_cases = state_data[n:]
    new_cases_over_last_n_days = state_data[n:] - state_data[:-n]
    plt.loglog(
        total_cases,
        new_cases_over_last_n_days,
        label=state,
        alpha=0.7,
        **linespecs[j]
    )
# END FOR

plt.grid(ls=':', lw=0.5, which='both')
plt.xlabel('Total confirmed cases')
plt.ylabel(f'New confirmed cases\n(over the past {n} days)')
plt.title(f'New cases vs total cases, as of {today}', fontweight='bold')

bbox_anchor_loc = (0., 1.08, 1., .102)
plt.legend(bbox_to_anchor=bbox_anchor_loc, loc='lower center', ncol=10)

text = 'Using the method suggested in https://www.youtube.com/watch?v=54XLXg4fYsc'
text += '\n\n'
text += '(A downward dip from the main trend would indicate\nthat the '
text += 'situation is getting better.)'
plt.annotate(
    s=text,
    xy=(0.015, 0.97),
    xytext=(0.015, 0.97),
    xycoords='axes fraction',
    fontsize=11,
    fontweight='regular',
    va='top',
)

plt.savefig(
    f'../output_figures/Trend_11__new_cases_vs_total_cases__{today}.png',
    bbox_inches='tight',
)

