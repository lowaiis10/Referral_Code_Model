import numpy as np
import matplotlib.pyplot as plt

# Parameters (you can adjust these values)
x = 0.05       # Referral fee rate (e.g., 10%)
n = 100        # Number of people referred who have traded
f1 = 0.01     # Fee percentage on buy volume (e.g., 0.2%)
f2 = 0.02     # Fee percentage on sell volume (e.g., 0.2%)

# Expected trading volumes per person
# For variable trading volumes, we'll use a lognormal distribution

# Parameters for the lognormal distribution
mu_buy = np.log(100) - (sigma ** 2) / 2     # Mean of the log of buy volumes
sigma_buy = 1  # Standard deviation of the log of buy volumes

mu_sell = np.log(100) - (sigma ** 2) / 2  # Mean of the log of sell volumes
sigma_sell = 1 # Standard deviation of the log of sell volumes

# Generate random trading volumes for each person
np.random.seed(42)  # For reproducibility

# Buy volumes per person
v1 = np.random.lognormal(mean=mu_buy, sigma=sigma_buy, size=n)

# Sell volumes per person
v2 = np.random.lognormal(mean=mu_sell, sigma=sigma_sell, size=n)

# Calculate total fees per person
fees_per_person = (v1 * f1) + (v2 * f2)

# Calculate total referral earnings
R = x * np.sum(fees_per_person)

# Output the results
print(f"Total Referral Earnings (R): ${R:,.2f}")
print(f"Average Referral Earnings per Person: ${R/n:,.2f}")

# Optional: Detailed statistics
print("\nDetailed Statistics:")
print(f"Average Buy Volume per Person: ${np.mean(v1):,.2f}")
print(f"Average Sell Volume per Person: ${np.mean(v2):,.2f}")
print(f"Total Fees Collected: ${np.sum(fees_per_person)/x:,.2f}")

# Plot histogram of buy volumes
plt.hist(v1, bins=50, alpha=0.7, label='Buy Volumes')
plt.hist(v2, bins=50, alpha=0.7, label='Sell Volumes')
plt.legend()
plt.title('Distribution of Trading Volumes')
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.show()
