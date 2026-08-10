import requests
import pandas as pd

API_KEY = "9f1dc3509b8158c5fe94d39e98789d63"

url = (
    f"https://api.stlouisfed.org/fred/series/observations?"
    f"series_id=FEDFUNDS"
    f"&api_key={API_KEY}"
    f"&file_type=json"
)

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["observations"])

df = df.rename(columns={
    "date": "ObservationDate",
    "value": "InterestRate"
})

df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])
df["InterestRate"] = pd.to_numeric(df["InterestRate"], errors="coerce")

df.to_excel(
    r"E:\SynapseSCM\1-Datasets\Raw_Data\External_Live\InterestRates.xlsx",
    index=False
)

print("Interest Rates downloaded successfully.")