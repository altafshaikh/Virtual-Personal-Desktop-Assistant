import requests

r = requests.get('http://localhost:8000/commands/webapp/')
r.text
print(r.text)

r = requests.put('http://localhost:8000/commands/webapp/1/', json={"task":"hi","done":"true"})
r.status_code #200

r = requests.delete('http://localhost:8000/commands/webapp/1/')
r.status_code #204