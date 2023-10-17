import requests

base_url = "https://raw.githubusercontent.com/db1000n-coordinators/LoadTestConfig/main/config.v0.7.json"

try:
  response = requests.get(base_url)
except ConnectionError as e:
  raise ConnectionError(e)

# проверяем, прошел ли запрос успешно
assert response.ok

# здесь будем хранить полученные данные
addresses = set()

json_response = response.json()['jobs']
for line in json_response:
  # если заданных в методе get полей нет, то вернется None
  # во избежании ошибки в этом случае ставим блок try...except..
  try:
    address = line.get("args").get("connection").get("args").get("address")
    # проверяем вернулось ли значение или None
    if address:
      addresses.add(address)
  except AttributeError:
    pass

print(addresses)
