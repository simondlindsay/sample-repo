import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_link = "https://www.strava.com/oauth/token" 
activities_link = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "63295",
    'client_secret': "1f85787294f3846b9b5b16e54913aeff4919fade", 
    'refresh_token': "ecbb8e1b89a88c54a7498d6da63fbfabab854474",
    'grant_type': "refresh_token",
    'f': "json"
}

res = requests.post(auth_link, data=payload, verify=False)
access_token = res.json()["access_token"]

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activities_link, headers=header, params=param).json()

print(my_dataset[-1]["map"]["summary_polyline"])
