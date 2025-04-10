# Import library
import pandas as pd
import numpy as np
import re
import requests as rs
from bs4 import BeautifulSoup as bs
import csv

url = 'https://api.divar.ir/v8/web-search/1/light'
json_data = {
    "page": 1,
    "json_schema": {
        "category": {"value": "light"},
        "brand_model": {"value": ["Peugeot 206 2"]},
        "cities": ["1"]
    },
    "last-post-date": 1688989212349260
}
headers = {"Content-Type": "application/json"}

res = rs.post(url, json=json_data, headers=headers)

if res.status_code == 200:
    data = res.json()
    last_post_date = data['last_post_date']
    list_of_tokens = []
    count = 0

    while count < 10000000:
        json_data['last-post-date'] = last_post_date
        res = rs.post(url, json=json_data, headers=headers)

        if res.status_code == 200:
            data = res.json()
            last_post_date = data['last_post_date']

            for widget in data['web_widgets']['post_list']:
                token = widget['data']['token']
                list_of_tokens.append(token)
                count += 1

            if count >= 10000000:
                break
        else:
            print(f"Error: {res.status_code}")
            break

    mileage = []
    model = []
    engine = []
    chassis = []
    price = []
    description = []

    for token in list_of_tokens:
        url = f"https://divar.ir/v/-/{token}"
        response = rs.get(url)
        soup = bs(response.text, 'html.parser')
        cars = soup.find_all('div', attrs={'class': 'kt-col-5'})

        for car in cars:
            mileage.append(re.findall('کارکرد(.+?)مدل', car.text))
            model.append(re.findall('\)(.{4})رنگ', car.text))
            engine.append(True if any(['سالم' in x for x in re.findall('وضعیت موتور(.+)وضعیت شاسی‌ها', car.text)]) else False)
            chassis.append(True if any(['سالم' in x or 'سالم و پلمپ' in x for x in re.findall('وضعیت شاسی‌ها(.+)وضعیت بدنه', car.text)]) else False)
            price.append(re.findall('قیمت پایه(.+) تومان', car.text))
            description.append(False if any(['بالاتری' in x for x in re.findall('فروشنده قیمت (.+) پیشنهاد', car.text)]) else True)

    data_df = {'Mileage(Kilometer)': mileage, 'Model(Year)': model, 'Engine(True=Healthy)': engine,
               'Chassis(True=Healthy)': chassis, 'Description(False=Expensive)': description, 'Price(Toman)': price}
    df = pd.DataFrame(data_df)
    df.to_csv('206_type_2.csv', index=False)
else:
    print(f"Error: {res.status_code}")
# end