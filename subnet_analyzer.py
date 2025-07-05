import pandas as pd             #deals with the Excel file
import ipaddress                #deals with IPs 

import json
from collections import defaultdict

#_________________________________________________________
#_________________Read the Excel file_____________________
#_________________________________________________________

try:
    df = pd.read_excel("ip_data.xlsx")
except FileNotFoundError:
    print("File 'ip_data.xlsx' not found!")
    exit()
#_________________________________________________________
#__Convert IP + Mask in "ip_data.xlsx" to IPv4Interface___
#_________________________________________________________

def to_interface(ip, mask):
    try:
        return ipaddress.IPv4Interface(f"{ip}/{mask}")
    except Exception as e:
        print(f"Error in {ip}/{mask}: {e}")
        return None
#_________________________________________________________
#_____________________Apply conversion____________________
#_________________________________________________________

df["Interface"] = df.apply(lambda row: to_interface(row["IP Address"], row["Subnet Mask"]), axis=1)

#_________________________________________________________
#_______________Extract required fields___________________
#_________________________________________________________

df["CIDR"] = df["Interface"].apply(lambda x: x.with_prefixlen if x else None)
df["Network"] = df["Interface"].apply(lambda x: x.network.network_address if x else None)
df["Broadcast"] = df["Interface"].apply(lambda x: x.network.broadcast_address if x else None)
df["Usable Hosts"] = df["Interface"].apply(lambda x: x.network.num_addresses - 2 if x and x.network.prefixlen < 31 else 0)

# print(df.head())


df.drop(columns=["Interface"], inplace=True)      #Drop temporary Col.

#_________________________________________________________
#______________________Save to CSV________________________
#_________________________________________________________

df.to_csv("subnet_report.csv", index=False)

print("Subnet analysis complete. Output saved to 'subnet_report.csv'")

#_________________________________________________________
#_______________Group IPs by subnet/CIDR__________________
#_________________________________________________________


# Build nested dict: { Subnet Mask: { Network: IP } }
subnet_json = defaultdict(dict)

for _, row in df.iterrows():
    mask = str(row["Subnet Mask"])
    network = str(row["Network"])
    ip = str(row["IP Address"])
    if pd.notna(mask) and pd.notna(network) and pd.notna(ip):
        subnet_json[mask][network] = ip



#___________________Save to JSON file______________________
with open("subnet_grouped_ip.json", "w") as f:
    json.dump(subnet_json, f, indent=2)

print("Grouped data saved to 'mask_network_ip.json'")
