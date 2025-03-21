import requests
import json 



API_KEY = "935b96a1-f17a-442c-9309-caff60715b38"



def holidays_info(country_index, year):
    url = f"https://holidayapi.com/v1/holidays?pretty&key={API_KEY}&country={country_index}&year={year}"

    response = requests.get(url)
    data = response.json()
    
    print(f'Всего в {data["holidays"][0]["country"]} {len(data["holidays"])} праздников в {year}:')
    for i in range(len(data["holidays"])):
        print(f'№{i+1} - "{data["holidays"][i]["name"]}"  \n        Дата - {data["holidays"][i]["date"]} ({data["holidays"][i] ["weekday"]["date"]["name"]})')
    


if __name__ == '__main__':
    country_index = input('Введите индекс страны: ')
    year = input('Введите желаемый год: ')
    
    holidays_info(country_index, year)
