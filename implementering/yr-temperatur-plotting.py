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
verdier = []

gjennomsnitt2 = []
verdier2 = []

for i in range(len(data["properties"]["timeseries"])):
    x.append(i)
    y.append(data["properties"]["timeseries"][i]["data"]["instant"]["details"]["air_temperature"])
    #print(data["properties"]["timeseries"][i]["data"]["instant"]["details"]["air_temperature"])

#print(y)
for i in range(1, len(y)):
    verdier.append(i-1)
    #print(str(y[i]) + " - " + str(y[i-1]) + " - " + str((y[i]+y[i-1])/2))
    gjennomsnitt.append((y[i]+y[i-1])/2)
#print(gjennomsnitt)

intervall = 10
start = -10
for i in range(8):
    start += intervall
    sum = 0
    for j in range(start, start+intervall):
        sum += y[j]
    sum = sum/intervall
    verdier2.append(start+intervall/2)
    gjennomsnitt2.append(sum)



plt.plot(verdier2, gjennomsnitt2)
plt.plot(verdier, gjennomsnitt)
plt.plot(x, y)
plt.xlabel("Timer fra nå")
plt.ylabel("Temperatur")
plt.show()