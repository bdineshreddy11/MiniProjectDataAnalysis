import requests
import pandas as pd
import os

# Exchange Rate API
url = "https://api.exchangerate-api.com/v4/latest/USD"

# Get data
response = requests.get(url, timeout=30)
response.raise_for_status()

data = response.json()

# Convert JSON to DataFrame
df = pd.DataFrame(data["rates"].items(), columns=["Currency", "Rate"])

# Output folder
output_folder = r"E:\SynapseSCM\01_Datasets\External_Live"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Output file
output_file = os.path.join(output_folder, "ExchangeRates.csv")

# Save CSV
df.to_csv(output_file, index=False)

print("ExchangeRates.csv saved successfully!")
print(f"Location: {output_file}")