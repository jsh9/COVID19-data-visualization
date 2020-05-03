# -*- coding: utf-8 -*-
import pandas as pd
import plot_utils as pu  # https://github.com/jsh9/python-plot-utilities

data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(data_url, dtype={'fips': str})

today = max(df['date'])
data_by_county = df.groupby('fips').sum()

fig, _ = pu.choropleth_map_county(
    data_by_county['cases'],
    map_title=f'Total confirmed cases per county, as of {today}',
    vmin=0,
    vmax=10000,
    cmap='GnBu',
    dpi=120,
)
fig.savefig(f'../output_figures/Map_county_01__Total_confirmed_cases_by_county_{today}.png')

fig, _ = pu.choropleth_map_county(
    data_by_county['deaths'],
    map_title=f'Total deaths per county, as of {today}',
    vmin=0,
    vmax=1000,
    cmap='GnBu',
    dpi=120,
)
fig.savefig(f'../output_figures/Map_county_02__Total_deaths_by_county_{today}.png')

fig, _ = pu.choropleth_map_county(
    data_by_county['deaths'] / data_by_county['cases'] * 100,
    map_title=f'Mortality rate per county, as of {today}',
    vmin=0,
    vmax=20,
    cmap='GnBu',
    dpi=120,
    unit='[%]'
)
fig.savefig(f'../output_figures/Map_county_03__Mortality_rate_by_county_{today}.png')
