import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

expected_csv_loc = 'train.csv'
df = pd.read_csv(expected_csv_loc)

print(df.head())
