import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

NUM_TRANSACTIONS = 1000

np.random.seed(42)

data = pd.DataFrame({
    "user_id": np.random.randint(1, 50, NUM_TRANSACTIONS),
    "amount": np.random.randint(10, 5000, NUM_TRANSACTIONS),
    "hour": np.random.randint(0, 24, NUM_TRANSACTIONS),
    "country": np.random.choice(["IL", "US", "UK", "FR"], NUM_TRANSACTIONS),
    "transactions_last_10min": np.random.randint(1, 10, NUM_TRANSACTIONS)
})

# --------------------------
# risk score
# --------------------------
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
# גרף 1 - fraud vs non-fraud
# --------------------------
fraud_counts = data["is_fraud"].value_counts()

plt.figure()
fraud_counts.plot(kind="bar")
plt.title("Fraud vs Non-Fraud")
plt.xticks([0, 1], ["Non-Fraud", "Fraud"])
plt.show()

# --------------------------
# גרף 2 - fraud לפי מדינה
# --------------------------
fraud_by_country = data.groupby("country")["is_fraud"].sum()

plt.figure()
fraud_by_country.plot(kind="bar")
plt.title("Fraud by Country")
plt.show()

# --------------------------
# גרף 3 - fraud לפי שעה
# --------------------------
fraud_by_hour = data.groupby("hour")["is_fraud"].sum()

plt.figure()
fraud_by_hour.plot(kind="line")
plt.title("Fraud by Hour")
plt.show()