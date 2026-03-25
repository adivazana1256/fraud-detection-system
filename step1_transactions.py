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

print(data.head())
# --------------------------
# יצירת fraud לפי חוקים
# --------------------------

data["is_fraud"] = 0

# סכום גבוה מאוד
data.loc[data["amount"] > 4000, "is_fraud"] = 1

# הרבה עסקאות בזמן קצר
data.loc[data["transactions_last_10min"] > 7, "is_fraud"] = 1

# מדינה זרה (לא ישראל)
data.loc[data["country"] != "IL", "is_fraud"] = 1

# שעה מוזרה (לילה)
data.loc[(data["hour"] < 5), "is_fraud"] = 1

print(data.head())