import yfinance as yf
import os

# Download 1 year of Crude Oil Futures data
oil = yf.download("CL=F", period="1y", interval="1d")

# Save location
output_folder = r"E:\SynapseSCM\01_Datasets\External_Live"

os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "CrudeOil.csv")

oil.to_csv(output_file)

print("CrudeOil.csv saved successfully!")
print(f"Location: {output_file}")