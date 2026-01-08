import requests
import base64
import os

BASE_URL = "http://127.0.0.1:8000"

# Ensure charts folder exists
os.makedirs("charts", exist_ok=True)

# Ping endpoints
ping_endpoints = [
    "/stats/ping",
    "/ml_algos/ping",
    "/nn/ping",
    "/rl/ping",
    "/cnn/ping",
    "/nlp/ping",
    "/timeseries/ping",
    "/optimization/ping",
    "/simulation/ping",
    "/parallel/ping",
    "/security/ping",
    "/visualization/ping",
    "/dsa/stack/push?item=test",  # quick DS&A ping via push
]

# Functional test cases
functional_tests = [
    {
        "name": "Security Hash",
        "method": "POST",
        "endpoint": "/security/hash",
        "payload": {"text": "password123", "algo": "sha256"},
    },
    {
        "name": "Monte Carlo Pi",
        "method": "GET",
        "endpoint": "/simulation/pi?trials=5000",
        "payload": None,
    },
    {
        "name": "Gradient Descent",
        "method": "POST",
        "endpoint": "/optimization/gradient_descent",
        "payload": {"start": 5, "lr": 0.1, "epochs": 10},
    },
    {
        "name": "Time Series Moving Average",
        "method": "POST",
        "endpoint": "/timeseries/moving_average",
        "payload": {"values": [10, 20, 30, 40, 50], "window": 3},
    },
]

# Visualization test cases
visualization_tests = [
    {
        "name": "Line Chart",
        "method": "POST",
        "endpoint": "/visualization/line",
        "payload": {"x": [1, 2, 3, 4], "y": [10, 20, 15, 25]},
    },
    {
        "name": "Bar Chart",
        "method": "POST",
        "endpoint": "/visualization/bar",
        "payload": {"categories": ["A", "B", "C"], "values": [5, 10, 7]},
    },
    {
        "name": "Pie Chart",
        "method": "POST",
        "endpoint": "/visualization/pie",
        "payload": {"labels": ["X", "Y", "Z"], "sizes": [30, 50, 20]},
    },
]

# DS&A test cases
dsa_tests = [
    {
        "name": "Stack Push",
        "method": "POST",
        "endpoint": "/dsa/stack/push?item=A",
    },
    {
        "name": "Stack Pop",
        "method": "POST",
        "endpoint": "/dsa/stack/pop",
    },
    {
        "name": "Queue Enqueue",
        "method": "POST",
        "endpoint": "/dsa/queue/enqueue?item=Task1",
    },
    {
        "name": "Queue Dequeue",
        "method": "POST",
        "endpoint": "/dsa/queue/dequeue",
    },
    {
        "name": "LinkedList Insert",
        "method": "POST",
        "endpoint": "/dsa/linkedlist/insert?value=Node1",
    },
    {
        "name": "HashTable Put",
        "method": "POST",
        "endpoint": "/dsa/hashtable/put?key=user&value=Renzo",
    },
    {
        "name": "HashTable Get",
        "method": "GET",
        "endpoint": "/dsa/hashtable/get?key=user",
    },
    {
        "name": "HashTable Delete",
        "method": "DELETE",
        "endpoint": "/dsa/hashtable/delete?key=user",
    },
]

def save_base64_image(image_b64: str, filename: str):
    image_bytes = base64.b64decode(image_b64)
    with open(filename, "wb") as f:
        f.write(image_bytes)
    print(f"Saved image → {filename}")

def test_pings():
    print("\n=== Ping Endpoints ===")
    for ep in ping_endpoints:
        url = BASE_URL + ep
        try:
            resp = requests.get(url)
            print(f"[{resp.status_code}] {ep} → {resp.json()}")
        except Exception as e:
            print(f"[FAIL] {ep} → {e}")

def test_functionals():
    print("\n=== Functional Endpoints ===")
    for test in functional_tests:
        url = BASE_URL + test["endpoint"]
        try:
            if test["method"] == "GET":
                resp = requests.get(url)
            else:
                resp = requests.post(url, json=test["payload"])
            print(f"[{resp.status_code}] {test['name']} → {resp.json()}")
        except Exception as e:
            print(f"[FAIL] {test['name']} → {e}")

def test_visualizations():
    print("\n=== Visualization Endpoints ===")
    for test in visualization_tests:
        url = BASE_URL + test["endpoint"]
        try:
            resp = requests.post(url, json=test["payload"])
            if resp.status_code == 200:
                data = resp.json()
                filename = os.path.join("charts", f"{test['name'].replace(' ', '_').lower()}.png")
                save_base64_image(data["image_base64"], filename)
                print(f"[{resp.status_code}] {test['name']} → Chart type: {data['chart']}, Image length: {len(data['image_base64'])} chars")
            else:
                print(f"[ERROR] {test['name']} → Status {resp.status_code}")
        except Exception as e:
            print(f"[FAIL] {test['name']} → {e}")

def test_dsa():
    print("\n=== DS&A Endpoints ===")
    for test in dsa_tests:
        url = BASE_URL + test["endpoint"]
        try:
            if test["method"] == "GET":
                resp = requests.get(url)
            elif test["method"] == "DELETE":
                resp = requests.delete(url)
            else:
                resp = requests.post(url)
            print(f"[{resp.status_code}] {test['name']} → {resp.json()}")
        except Exception as e:
            print(f"[FAIL] {test['name']} → {e}")

if __name__ == "__main__":
    test_pings()
    test_functionals()
    test_visualizations()
    test_dsa()