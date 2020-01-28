import requests
import pytest # have to install via command "pip3 install -U pytest"

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

def test_status_check():
    r = requests.get('http://localhost:8085/hello-world')
    assert(r.status_code == 200)

# 1. Add two more tests here of your choice. I will explain the API.
#    Make sure to verify the necessary info, e.g., status code, response data.
# 2. Add "pytest" as integration testing script as part of Github Actions CI workflow (you've done this before!)

def test_name_response():
    r = requests.get('http://localhost:8085/hello-world?name=Colin')
    assert(r.json()['content'] == "Hello, Colin!")

def test_request_increment():
    r = requests.get('http://localhost:8085/hello-world')
    r1 = requests.get('http://localhost:8085/hello-world')
    assert(r.json()['id'] + 1 == r1.json()['id'])

