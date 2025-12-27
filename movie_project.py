import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,'html.parser')

# print(response.status_code)
#
# print(response.text[:200])

movie_table = soup.find("table")

print(len(movie_table.find_all("tr")))

rows = movie_table.find_all("tr")

movie_data_list = []

for row in rows[1:]:
    cols = row.find_all(["td","th"])
    title = cols[2].text.strip()
    revenue = cols[3].text.strip()
    year = cols[4].text.strip()

    movie_data_list.append({"Title":title,"Revenue":revenue,"Year":year})


#print(movie_data_list[:5])

df = pd.DataFrame(movie_data_list)

# print(df.head())
# print(df.info())

#df['Revenue'] = df['Revenue'].str.replace("$","").str.replace(",","")
df["Revenue"] = df["Revenue"].str.replace(r"\D","",regex = True)

df["Revenue"] = pd.to_numeric(df["Revenue"],errors="coerce")
df["Year"] = pd.to_numeric(df["Year"])

# print(df.head())
# print(df.info())

# Filter out "The Fate of the Furious" outlier where a reference number merged with revenue (creating ~$81B)
df = df[df["Revenue"] < 10_000_000_000]

plt.figure(figsize=(12,6))

plt.scatter(df["Year"],df["Revenue"],alpha=0.7,color="green",s=100)

plt.title("Highest Grossing Films: Year vs. Revenue")

plt.xlabel("Year Released")

plt.ylabel("Revenue (USD Billions)")

plt.grid(True,alpha=0.3)

plt.show()

