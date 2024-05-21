import requests

def Prayer_Times(city, country):
    url = f" http://api.aladhan.com/v1/timingsByCity?city={city}&country={country} Arab Emirates&method=5"

    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            timing = info["data"]["timings"]
            return timing
        else:
            return None
    except Exception as e:
        return f"unexpected error occurred {e}"

city = input("please enter the city name: ")
country = input("please enter the country name: ")

if city and country:
    final = Prayer_Times(city, country)
    for name, time in final.items():
        print(f"{name} : {time}")
    
else:
    print("unable to fetch prayer times!")
# this is my Prayer_Times_Project