import requests

data_source = (
    "https://raw.githubusercontent.com/"
    "owid/covid-19-data/master/public/data/owid-covid-data.csv"
)

r = requests.get(data_source, allow_redirects=True)
open("covid-data.csv", "wb").write(r.content)