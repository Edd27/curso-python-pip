import requests as req

def get_categories():
  r = req.get('https://api.escuelajs.co/api/v1/categories')
  print(r.status_code)
  print(r.text)
  print(type(r.text))
  categories = r.json()
  for category in categories:
    print(category['name'])