# COVID19-data-visualization
_Data visualization of some COVID-19 data_

## Data source
The data comes from The COVID Tracking Project (https://github.com/COVID19Tracking/covid-tracking-data).

## Visualizations from the data
_(Will be updated daily, following the update of the data source.)_![](./output_figures/Map_01__positive_cases_by_state_2020-03-25.png)
![](./output_figures/Map_02__Positive_rate_by_state_2020-03-25.png)
![](./output_figures/Map_03__new_cases_from_2020-03-22_to_2020-03-25.png)
![](./output_figures/Trend_01__positive_cases_all_US_states__linear_scale__2020-03-25.png)
![](./output_figures/Trend_02__positive_cases_all_US_states__log_scale__2020-03-25.png)
![](./output_figures/Trend_03__positive_cases_all_states_excl_NY_NJ__linear_scale__2020-03-25.png)
![](./output_figures/Trend_04__positive_cases_all_states_excl_NY_NJ__log_scale__2020-03-25.png)
![](./output_figures/Trend_05__number_of_tests_all_US_states__linear__2020-03-25.png)
![](./output_figures/Trend_06__number_of_tests_all_US_states__log__2020-03-25.png)
![](./output_figures/Trend_07__positive_rate_all_states_2020-03-25.png)
![](./output_figures/Trend_08__positive_rate_all_states_excl_NY_NJ_2020-03-25.png)
![](./output_figures/Trend_09__tests_per_capita_2020-03-25.png)

## How to reproduce these figures
To reproduce the figures, run `./scripts/Run_all.py`, which runs all other scripts in the same folder. The output figures are saved in the `output_figures` folder.

The Python packages used to produce these figures:
  - numpy: 1.11.0+
  - pandas: 0.20.0+
  - matplotlib: 2.1.0+
  - basemap: 1.0.7+ (https://github.com/matplotlib/basemap)
  - plot-utils: 0.6.2+ (https://github.com/jsh9/python-plot-utilities)


## Terms and conditions
Reusing contents (such as figures or code) of this repository is permitted, provided that this repository is cited, AND all the terms and conditions outlined the `LICENSE` file are met.
