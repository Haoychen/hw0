__author__ = 'voelunteer'
import pandas as pd

iowa_liquor_sale = pd.read_csv("iowa-liquor-sample.csv")
category_name = iowa_liquor_sale['CATEGORY NAME'].str.lower()
num_single_melt_scotch = 0
for row in category_name:
    if row == 'single malt scotch':
        num_single_melt_scotch += 1
print num_single_melt_scotch