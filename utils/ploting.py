import matplotlib.pyplot as plt
import pandas as pd

plt.close()
result = pd.read_csv('../baseline/results/23_4_enrichment_lincs_threshold100.csv')

plt.figure(figsize=(12,8))
plt.title("Folds of Enrichment in Top Connections")
plt.plot((1-result["percentile"])*100, result["ods_ratio"], marker="o", color="red")
plt.show()

result = pd.read_csv('../baseline/results/274_pr.csv')
# plt.figure(figsize=(12,8))
# plt.title("Average Precision - Top 25 Connections")
# plt.plot((result["k"]), result["precision"], marker="o", color="red")
# plt.show()

# plt.figure(figsize=(12,8))
# plt.title("Interpolated Recall-Precision Curve")
# plt.plot((result["recal"]), result["precision"], marker="o", color="red")
# plt.show()
