import requests

url = 'http://localhost:80'
response = requests.get(url)
csrftoken = response.headers['set-cookie'].split(';', 1)[0].split('=')[1]
print(csrftoken)
print(response.headers)

response = requests.post(
    url,
    data={
        'csrfmiddlewaretoken': csrftoken,
        'next': '/admin/',
        'password': 'password',
        'username': 'admin'
    },
    headers={
        'Referer': url
    })

print(response)
print(response.status_code)
print(response.headers)
print(response.text)
