import requests


def get_all_exchange_rates(src):
    url = f'https://v6.exchangerate-api.com/v6/e201cf366e47566560750c68/latest/{src}'
    data = requests.get(url).json()
    if data["result"] == "success":
        exchange_rates = data["conversion_rates"]
        last_data_update = data["time_last_update_utc"]
        return last_data_update, exchange_rates


def convert_currency(src, dst, amount):
    last_data_update, exchange_rates = get_all_exchange_rates(src)
    return exchange_rates[dst] * float(amount), src, dst, amount

