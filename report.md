
# 📊 Network Subnet Analysis Report

This report answers key network analysis questions based on an Excel dataset (`ip_data.xlsx`) that contains IP addresses and subnet masks. The analysis was performed using Python, and results were visualized and reported manually.

---

## 1. Which subnet has the most hosts?

✅ **Answer:**  
The subnet mask `/22` provides the largest number of usable hosts in this dataset.  
A `/22` subnet offers a total of **1,024 IP addresses**, out of which **1,022 are usable** (excluding network and broadcast addresses).

The following subnets in the dataset have **/22 masks** and hence provide the **maximum usable IPs (1,022 hosts each):**

- `10.15.4.0/22`  
- `10.2.0.0/22`  
- `10.20.4.0/22`  
- `10.3.0.0/22`  
- `172.16.48.0/22`  
- `172.16.60.0/22`  
- `192.168.100.0/22`  
- `192.168.20.0/22`  

All these subnets tie for the highest number of usable hosts.

---

## 2. Are there any overlapping subnets?

❌ **Answer:**  
After performing a full overlap check using Python's `ipaddress` module, there are **no overlapping subnets** in the provided dataset.



### 🧠 What is an overlapping subnet?

Two subnets are said to **overlap** if their IP address ranges intersect — meaning they share one or more common IP addresses.

For example:
- `192.168.1.0/24` → includes IPs from `192.168.1.0` to `192.168.1.255`
- `192.168.1.128/25` → includes IPs from `192.168.1.128` to `192.168.1.255`

➡️ These two subnets overlap because they share the range `192.168.1.128` to `192.168.1.255`.



### 🔍 How was the check performed?

The analysis was done programmatically using this logic:

```python
import ipaddress

# Convert all subnets to network objects
cidrs = df["CIDR"].dropna().unique()
networks = [ipaddress.ip_network(c, strict=False) for c in cidrs]

# Compare each pair to check for overlaps
for i in range(len(networks)):
    for j in range(i + 1, len(networks)):
        if networks[i].overlaps(networks[j]):
            print(f"{networks[i]} overlaps with {networks[j]}")
```

And manually, follow the steps:
1. Each IP address was mapped to its respective subnet using the associated subnet mask.
2. All network addresses were computed and compared using Python's `ipaddress` module.
3. Each resulting subnet range was evaluated against others to check for any overlaps.



### ✅ Findings:

- All subnets in the dataset have **unique network addresses**.
- No two subnets share common IP ranges.
- Each IP belongs to a **distinct and non-overlapping subnet block**.

This confirms the IP addressing scheme is well-structured and avoids routing conflicts or duplicate assignments.



### 📊 Subnet Distribution Summary:

| Subnet Mask | Number of Subnets | Usable Hosts/Subnet |
|-------------|--------------------|----------------------|
| `/24`       | 10                 | 254 hosts            |
| `/23`       | 7                  | 510 hosts            |
| `/22`       | 8                  | 1,022 hosts          |



### ✅ Conclusion:

> Based on both manual review and programmatic verification, **all 25 subnets are distinct and non-overlapping**.  
> The network design ensures each subnet is isolated, preventing address conflicts and supporting scalable IP management.

---
## 3. What is the smallest and largest subnet in terms of address space?

✅ **Answer:**

- **Largest subnets:**  
  Any subnet with a `/22` mask is the largest in the dataset in terms of usable address space.  
  Each `/22` subnet contains **1,022 usable IP addresses**.

  Examples:
  - `192.168.100.0/22`
  - `10.2.0.0/22`
  - `172.16.60.0/22`

- **Smallest subnet:**  
  The smallest subnet in this dataset has a `/24` mask.  
  A `/24` subnet contains **256 IPs**, of which **254 are usable**.

  Example:
  - `192.168.1.24/24` → 254 usable hosts

> Note: The dataset does not contain any small subnets such as `/30`, `/31`, or `/32`, which are typically used in point-to-point networks.

---

## 4. Suggest a subnetting strategy that could reduce wasted IPs in this network.

📌 **Answer:**

Many subnets in the dataset use `/22` and `/24` masks. While these offer large address spaces, they might be **wasteful** if only a few devices are active in each subnet.

To reduce IP wastage and improve address efficiency:

- **Use VLSM (Variable Length Subnet Masking)**:  
  Allocate subnets with sizes that match the actual number of devices.
  Instead of allocating large, fixed-size subnets like /22 or /23 for every device or group — which leads to excessive IP waste — a better approach is to customize the subnet size based on actual usage. This is exactly what **Variable Length Subnet Masking (VLSM)** offers.

To illustrate:

We currently have 25 active IP addresses across 25 different subnets, consuming a total of **14,336 IP addresses**. That’s an average of **573 addresses wasted per IP** — clearly inefficient.

By applying VLSM, we can reallocate those same 25 IPs into smaller, right-sized subnets as follows:

- **1 subnet** using `/24` (254 usable IPs) → reserved for future growth  
- **2 subnets** using `/25` (126 usable IPs each) → medium-sized segments  
- **4 subnets** using `/26` (62 usable IPs each) → small groups  
- **8 subnets** using `/27` (30 usable IPs each) → tiny departments  
- **Remaining IPs** can be grouped in shared `/28` or `/30` subnets  

With this strategy, the total IP space used drops from over **14,000** to just around **1,000 addresses**, while still covering all current devices and leaving expansion room.

This is not just a space-saving trick — it's a best practice that improves network clarity, efficiency, and scalability.


- **Avoid large subnets for small networks**:  
  Don’t assign `/22` or `/24` for networks with <10 hosts.

- **Use smaller subnets when appropriate**:  
  - `/29` → for 6 usable hosts  
  - `/30` → for 2 usable hosts (P2P)  
  - `/31` → for 2 addresses used in routing (RFC 3021)

- 🗂️ **Segment** subnets by department, service, or region — making IP planning more efficient and organized.

---

📁 *This report was prepared by Esraa as part of the Barq DevOps Internship Task.*
