import requests as req
import geocoder
import matplotlib.pyplot as plt

url = "https://api.met.no/weatherapi/locationforecast/2.0/complete?lat=59.89&lon=10.52"
#yr = req.get(url)

res = req.get(url, headers = { 'User-Agent': 'Marius'})

data = res.json()

#print(len(data["properties"]["timeseries"]))
x = []
y = []
gjennomsnitt = []

for i in range(len(data["properties"]["timeseries"])):
    x.append(i)
    y.append(data["properties"]["timeseries"][i]["data"]["instant"]["details"]["air_temperature"])
    #print(data["properties"]["timeseries"][i]["data"]["instant"]["details"]["air_temperature"])

#print(y)
current = 1
for i in range(len(y)):
    gjennomsnitt.append((y[i]+y[current])/2)
    current += 1
print(gjennomsnitt)

#plt.plot(x, gjennomsnitt)
#plt.plot(x, y)
#plt.xlabel("Timer fra nå")
#plt.ylabel("Temperatur")
#plt.show()