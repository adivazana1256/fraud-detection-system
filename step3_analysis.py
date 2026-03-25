import numpy as np
import pandas as pd

NUM_TRANSACTIONS = 1000

np.random.seed(42)

data = pd.DataFrame({
    "user_id": np.random.randint(1, 50, NUM_TRANSACTIONS),
    "amount": np.random.randint(10, 5000, NUM_TRANSACTIONS),
    "hour": np.random.randint(0, 24, NUM_TRANSACTIONS),
    "country": np.random.choice(["IL", "US", "UK", "FR"], NUM_TRANSACTIONS),
    "transactions_last_10min": np.random.randint(1, 10, NUM_TRANSACTIONS)
})

# risk score
data["risk_score"] = 0.0

data.loc[data["amount"] > 4000, "risk_score"] += 0.4
data.loc[(data["amount"] > 2500) & (data["amount"] <= 4000), "risk_score"] += 0.2

data.loc[data["transactions_last_10min"] > 7, "risk_score"] += 0.3
data.loc[(data["transactions_last_10min"] >= 5) & (data["transactions_last_10min"] <= 7), "risk_score"] += 0.15

data.loc[data["country"] != "IL", "risk_score"] += 0.2
data.loc[data["hour"] < 5, "risk_score"] += 0.2

data["risk_score"] = data["risk_score"].clip(0, 1)
data["is_fraud"] = (data["risk_score"] >= 0.5).astype(int)

# --------------------------
# analysis
# --------------------------

fraud_count = data["is_fraud"].sum()
non_fraud_count = len(data) - fraud_count

avg_amount_fraud = data[data["is_fraud"] == 1]["amount"].mean()
avg_amount_non_fraud = data[data["is_fraud"] == 0]["amount"].mean()

fraud_by_country = data.groupby("country")["is_fraud"].sum()
fraud_by_hour = data.groupby("hour")["is_fraud"].sum()

print("Total transactions:", len(data))
print("Fraud transactions:", fraud_count)
print("Non-fraud transactions:", non_fraud_count)
print("Average fraud amount:", round(avg_amount_fraud, 2))
print("Average non-fraud amount:", round(avg_amount_non_fraud, 2))

print("\nFraud by country:")
print(fraud_by_country)

print("\nFraud by hour:")
print(fraud_by_hour)