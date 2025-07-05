import pandas as pd
import matplotlib.pyplot as plt

# Load subnet analysis data
df = pd.read_csv("subnet_report.csv")

# Plot bar chart
plt.figure(figsize=(10, 5))
bars = plt.bar(df["CIDR"].astype(str), df["Usable Hosts"], color="pink")

# Labels and title
plt.xlabel("Subnet (CIDR)", fontsize=10, fontweight='bold')
plt.ylabel("Total Usable Hosts", fontsize=10, fontweight='bold')
plt.title("Usable Hosts per Subnet", fontsize=14, fontweight='bold')
plt.xticks(rotation=90)

# Save and show
plt.tight_layout()
plt.savefig("network_plot.png")
plt.show()
