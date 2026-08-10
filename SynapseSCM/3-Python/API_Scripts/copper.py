import yfinance as yf
import os

copper = yf.download("HG=F", period="1y", interval="1d")

output_folder = r"E:\SynapseSCM\01_Datasets\External_Live"

os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "Copper.csv")

copper.to_csv(output_file)

print(" Copper.csv saved successfully!")
print(f"Location: {output_file}")