# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:40:22 2016

@author: gus
"""

import pandas as pd


def get_sample_data(input_file):
	df = pd.read_csv(input_file)
	df_sample = df.head()
	return df_sample

def get_summary_stats(input_file):
	df = pd.read_csv(input_file)
	df_stats = df.describe()
	return df_stats




