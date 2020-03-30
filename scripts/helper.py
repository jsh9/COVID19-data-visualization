# -*- coding: utf-8 -*-
import datetime
import numpy as np
import pandas as pd
import plot_utils as pu  # https://github.com/jsh9/python-plot-utilities

def exclude_overseas_territory_records(df: pd.DataFrame):
    overseas_territory = {
        'AS',  # American Samoa
        'FM',  # Federated States of Micronesia
        'GU',  # Guam
        'MH',  # Marshall Islands
        'MP',  # Northern Mariana Islands
        'PW',  # Palau
        'PR',  # Puerto Rico
        'VI',  # Virgin Islands
    }
    df.drop(df[df['state'].isin(overseas_territory)].index, inplace=True)
    return None

def replace_NY_NJ_data_with_NaN_for_easier_plotting(trend_df: pd.DataFrame):
    new_df = trend_df.copy()
    new_df['NY'] = [np.nan] * trend_df.shape[0]
    new_df['NJ'] = [np.nan] * trend_df.shape[0]
    return new_df

def plot_lines(data: pd.DataFrame, title: str, ylabel: str, logy: bool = False):
    fig, ax = pu.plot_multiple_timeseries(
        data,
        ncol_legend=10,
        dpi=120,
    )
    ax.set_xlabel('Date')
    ax.set_ylabel(ylabel)
    if logy:
        ax.set_yscale('log')
    # END IF
    ax.annotate(
        s=title,
        xy=(0.02, 0.97),
        xytext=(0.02, 0.97),
        xycoords='axes fraction',
        fontsize=16,
        fontweight='bold',
        va='top',
    )
    return fig, ax

def get_today(trend_df: pd.DataFrame) -> datetime.date:
    return datetime.datetime.strptime(str(trend_df.index[-1]), '%Y%m%d').date()
