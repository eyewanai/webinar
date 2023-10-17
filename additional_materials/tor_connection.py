import random
import requests

tor_proxy = "socks5h://127.0.0.1:9150"


# выбирает случайный юзер-агент для избежания блокировок
def choose_random_user_agent(path_to_txt: str):
  with open(path_to_txt, "r") as f:
    user_agents = f.read().splitlines()

  idx = random.randint(1, len(user_agents) - 1)
  return user_agents[idx]


# проверяем есть ли подключение к tor
def check_tor_connection():
  proxies = {'http': tor_proxy,
             'https': tor_proxy}

  headers = {"User-Agent": choose_random_user_agent("user_agents.txt")}

  base_url = "https://check.torproject.org/api/ip"

  try:
    response = requests.get(base_url, proxies=proxies, headers=headers)
  except requests.exceptions.ConnectionError:
    raise ConnectionError("Connection error")

  json_response = response.json()

  if json_response.get("IsTor") is True:
    return True
  else:
    raise ConnectionError("You are not connected to TOR")


# делаем запрос к .onion ссылке и возвращаем объект класса requests.Response
def access_tor(onion_url: str):
  proxies = {'http': tor_proxy,
             'https': tor_proxy}

  headers = {"User-Agent": choose_random_user_agent("user_agents.txt")}

  try:
    response = requests.get(onion_url, proxies=proxies, headers=headers)
    return response
  except Exception as e:
    return e


# проверяем возвращает ли наша функция True, иначе вылезет ошибка
assert check_tor_connection()

# ссылка на данные, которые опубликовала группировка lockbit
url_onion = "http://lockbit7z6f3gu6rjvrysn5gjbsqj3hk3bvsg64ns6pjldqr2xhvhsyd.onion"

tor_response = access_tor(url_onion)

assert isinstance(tor_response, requests.Response)

# выводит статус код
print(tor_response.status_code)

# выводит html код, который можно парсить, используя beautifulsoup
print(tor_response.text[:1000])
