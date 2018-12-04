#! python3
#scrapes a text file and saves as a txt file
import requests
#define the website to download
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.codes.ok
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))
    
len(res.text)
print(res.text[:500])
playFile = open('RomeoandJuliet.txt', 'wb')
for parts in res.iter_content(100000):
    playFile.write(parts)
playFile.close