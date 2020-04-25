import requests
files = {'upload_file': open('file.txt','rb')}

r = requests.post('https://reddit-flair-ind-det-anj.herokuapp.com/automated_testing', files=files)
print(r.json())