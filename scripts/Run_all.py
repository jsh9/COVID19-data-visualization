# -*- coding: utf-8 -*-
import glob
import subprocess
import pandas as pd
import helper as hlp

data_url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

df = pd.read_csv(data_url)
trend_df = df.pivot(index='date', columns='state', values='total')
today = hlp.get_today(trend_df)

#%%--------------- Plot -------------------------------------------------------
daily_scripts = glob.glob(f'./Daily_*.py')
map_scripts = glob.glob(f'./Map_*.py')

for script in map_scripts:
    print(script)
    exec(open(script).read())
# END FOR

for script in daily_scripts:
    print(script)
    exec(open(script).read())
# END FOR

#%%-------------- Update README -----------------------------------------------
txt = '# COVID19-data-visualization\n'
txt += '_Data visualization of some COVID-19 data_\n\n'
txt += '## Data source\n'
txt += 'The data comes from The COVID Tracking Project '
txt += '(https://github.com/COVID19Tracking/covid-tracking-data).\n\n'
txt += '## Visualizations from the data\n'
txt += '_(Will be updated daily, following the update of the data source.)_'

fig_filenames = sorted(glob.glob(f'../output_figures/*_{today}.png'))
for fig_fn in fig_filenames:
    fig_fn_for_MD = fig_fn[1:].replace('\\', '/')
    txt += f'![]({fig_fn_for_MD})\n'
# END FOR

txt += '\n'
txt += '## How to reproduce these figures\n'
txt += 'To reproduce the figures, run `./scripts/Run_all.py`, which runs '
txt += 'all other scripts in the same folder. The output figures are '
txt += 'saved in the `output_figures` folder.\n\n'
txt += 'The Python packages used to produce these figures:\n'
txt += '  - numpy: 1.11.0+\n'
txt += '  - pandas: 0.20.0+\n'
txt += '  - matplotlib: 2.1.0+\n'
txt += '  - basemap: 1.0.7+ (https://github.com/matplotlib/basemap)\n'
txt += '  - plot-utils: 0.6.2+ (https://github.com/jsh9/python-plot-utilities)\n'
txt += '\n\n'
txt += '## Terms and conditions\n'
txt += 'Reusing contents (such as figures or code) of this repository is permitted, '
txt += 'provided that this repository is cited, AND all the terms and conditions '
txt += 'outlined the `LICENSE` file are met.'
txt += '\n'

with open('../README.md', 'w') as fp:
    fp.write(txt)
# END WITH
