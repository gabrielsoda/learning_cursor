#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("penguins.csv")

df.head()

df.info()

df.describe()


df.columns

sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", data=df)
plt.show()

# %%
