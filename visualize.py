import pandas as pd
import matplotlib.pyplot as plt


# Step 1: Load CSV
df = pd.read_csv("subnet_report.csv")

df["CIDR"] = pd.Categorical(df["CIDR"], categories=df["CIDR"].unique(), ordered=True)
grouped = grouped = df.groupby("CIDR", sort=False, observed=False)["Usable Hosts"].sum().reset_index()



plt.figure(figsize=(10, 5))
bars = plt.bar(grouped["CIDR"].astype(str), grouped["Usable Hosts"], color="pink")
plt.xlabel("Subnet (CIDR)", fontsize=10, fontweight='bold', color="#333")
plt.ylabel("Total Usable Hosts", fontsize=10, fontweight='bold', color="#333")
plt.title("Usable Hosts per Subnet", fontsize=14, fontweight='bold', color="#333")
plt.xticks(rotation=90)


plt.tight_layout()
plt.savefig("network_plot.png")
plt.show()