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

# יצירת ציון סיכון התחלתי
data["risk_score"] = 0.0

# סכום גבוה
data.loc[data["amount"] > 4000, "risk_score"] += 0.4
data.loc[(data["amount"] > 2500) & (data["amount"] <= 4000), "risk_score"] += 0.2

# הרבה עסקאות בזמן קצר
data.loc[data["transactions_last_10min"] > 7, "risk_score"] += 0.3
data.loc[(data["transactions_last_10min"] >= 5) & (data["transactions_last_10min"] <= 7), "risk_score"] += 0.15

# מדינה זרה
data.loc[data["country"] != "IL", "risk_score"] += 0.2

# שעה חריגה
data.loc[data["hour"] < 5, "risk_score"] += 0.2

# לוודא שהציון לא עובר 1
data["risk_score"] = data["risk_score"].clip(0, 1)

# החלטה סופית
data["is_fraud"] = (data["risk_score"] >= 0.5).astype(int)

print(data.head(10))