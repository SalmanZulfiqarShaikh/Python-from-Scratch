import requests

url = "https://api.github.com/users/SalmanZulfiqarShaikh/followers"
response = requests.get(url)

if response.status_code == 200:
    followers = response.json()
    print("Follower usernames:")
    for f in followers:
        print(f["login"])  # Sirf username print hoga
else:
    print("Error:", response.status_code)
