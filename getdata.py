
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
url_drawings = "https://powerball.p.rapidapi.com/"
headers_drawings = {
    "X-RapidAPI-Key": os.getenv("YOUR_API_KEY"),
    "X-RapidAPI-Host": "powerball.p.rapidapi.com"
}

response_drawings = requests.get(url_drawings, headers=headers_drawings)
data_drawings = response_drawings.json()

drawings = data_drawings["drawings"]

drawing_dates = []
winning_numbers = []
jackpots = []

for drawing in drawings:
    drawing_date = drawing["DrawingDate"]
    numbers = drawing["NumberSet"].split(" ")
    jackpot = drawing["Jackpot"]
    
    drawing_dates.append(drawing_date)
    winning_numbers.append(numbers)
    jackpots.append(jackpot)

df_drawings = pd.DataFrame({
    "Drawing Date": drawing_dates,
    "Winning Numbers": winning_numbers,
    "Jackpot": jackpots
})
df_drawings ["Jackpot"] = df_drawings["Jackpot"].str.replace("$", "", regex=True).astype(float)
df_drawings["Drawing Date"] = pd.to_datetime(df_drawings["Drawing Date"])

print(df_drawings.head(5))

url_stats = "https://powerball.p.rapidapi.com/stats"
headers_stats = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "powerball.p.rapidapi.com"
}

response_stats = requests.get(url_stats, headers=headers_stats)
data_stats = response_stats.json()

stats = data_stats  # Use the entire stats response data as it is

df_stats = pd.DataFrame(stats, index=[0])  # Convert the stats dictionary to a DataFrame

print(df_stats.head(5))


