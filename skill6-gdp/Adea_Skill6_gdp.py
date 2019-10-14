from matplotlib import pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/datasets/gdp/0be54c18d900edc37123f25b4eff014731c9e459/data/gdp.csv"

data = pd.read_csv(url)
#print(data.columns)
us = data[data['Country Name'] == 'United States']
china = data[data['Country Name'] == 'China']
eu = data[data['Country Name'] == 'European Union']

us_year = us['Year']
us_gdp = us['Value'] / (10**9)
china_year = china['Year']
china_gdp = china['Value'] / (10**9)
eu_year = eu['Year']
eu_gdp = eu['Value'] / (10**9)

plt.plot(us_year, us_gdp, '^', color='cornflowerblue')
plt.plot(china_year, china_gdp, 'o', color='tomato')
plt.plot(eu_year, eu_gdp, '--', color='limegreen')

plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend(["USA", "China", "EU"])
plt.title("Michelle Adea's GDP Plot")
plt.show()
