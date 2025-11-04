# data_gen.py
import numpy as np
import pandas as pd

np.random.seed(42)
n = 1000

day_of_week = np.random.randint(0, 7, size=n)
is_weekend = (day_of_week >= 5).astype(int)
month = np.random.randint(1, 13, size=n)
store_area = np.random.uniform(50, 300, size=n)
promotion = np.random.binomial(1, 0.25, size=n)
holiday = np.random.binomial(1, 0.03, size=n)
price_index = np.random.normal(1.0, 0.06, size=n)
competitor_distance = np.random.exponential(2.0, size=n)
temperature = np.random.uniform(8, 36, size=n)

foot_traffic = (300 + store_area * 2 + (is_weekend * 200) - (price_index - 1)*1000 +
                np.random.normal(0, 120, size=n)).clip(30, None)
prev_day_sales = (0.6 * (100 + 2*store_area) + 0.2 * foot_traffic +
                  np.random.normal(0, 80, size=n)).clip(0, None)

base = 500
sales = (base +
         2.5 * store_area +
         0.8 * foot_traffic +
         400 * promotion +
         -900 * holiday +
         -500 * (price_index - 1) +
         50 * competitor_distance +
         0.3 * prev_day_sales +
         3 * temperature +
         np.random.normal(0, 350, size=n)).clip(0, None)

df = pd.DataFrame({
    "day_of_week": day_of_week,
    "is_weekend": is_weekend,
    "month": month,
    "store_area": store_area.round(1),
    "promotion": promotion,
    "holiday": holiday,
    "price_index": price_index.round(3),
    "competitor_distance_km": competitor_distance.round(2),
    "temperature_C": temperature.round(1),
    "foot_traffic": foot_traffic.round(0),
    "prev_day_sales": prev_day_sales.round(0),
    "sales": sales.round(2)
})

df.to_csv("store_sales.csv", index=False)
print("Guardado: store_sales.csv")
