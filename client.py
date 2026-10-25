import requests

# запрос к /about
try:
    response = requests.get("http://127.0.0.1:5000/about", timeout=5)
    print(response.status_code)
    response.raise_for_status()
    print(response.text)


except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")





####################################################################
####################################################################





# запрос к /summ
try:
    response = requests.get("http://127.0.0.1:5000/add/summ", params={"one": 2, "two": 6}, timeout=5)
    print(response.status_code)
    response.raise_for_status()
    print(response.json())




except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")





####################################################################
####################################################################





# запрос к /summ
try:
    response = requests.get("http://127.0.0.1:5000/add/summ", params={"one": 2, "two": 4}, timeout=5)
    print(response.status_code)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.json()["error"])



except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")






