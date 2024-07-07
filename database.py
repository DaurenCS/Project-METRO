
import json
import requests
url = "https://metroalmaty.kz/_next/data/ytII1wyCinohRr4lU5bfD/ru/poor-vision/schedule.json"

def fetch_schedule(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            schedule = data["pageProps"]["schedule"]
            return schedule
        else:
            print("Failed to fetch data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def filter_schedule_by_station(station_name):
    schedule_data = fetch_schedule(url)
    
    data = [item for item in schedule_data if item['station'] == station_name][0]
    text = f"Станция: {data['station']}.\n\
В сторону станции Момышулы поезд прибудет в {data['way1_time']}\n\
В сторону станции Райымбек поезд прибудет в {data['way2_time']}"
    return text
    


def get_all_stations():
    schedule_data = fetch_schedule(url)
    return [item['station'] for item in schedule_data]
