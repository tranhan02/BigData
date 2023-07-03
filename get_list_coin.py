import csv
import requests

def get_all_coin_list():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    start = 1
    limit = 5000  # Giới hạn số lượng đồng coin lấy thông tin (tối đa 5000)
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '31d6e25f-c5e2-4c51-9a71-21c74d62e1f3',  
    }

    coin_data = []  # Danh sách chứa dữ liệu đồng coin

    while True:
        parameters = {
            'start': start,
            'limit': limit,
        }

        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        if 'data' in data:
            coin_list = data['data']
            for coin in coin_list:
                name = coin['name']
                symbol = coin['symbol']
                coin_data.append([name, symbol])
        else:
            print("Error: Unable to retrieve coin list.")

        total_count = data['status']['total_count']
        start += limit

        if start > total_count:
            break

    # Lưu dữ liệu vào file CSV
    with open('coin_data1.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Symbol'])  

        for coin in coin_data:
            writer.writerow(coin)

    print("Data has been saved to coin_data.csv")

get_all_coin_list()
