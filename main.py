import collections
import urequest1
import urequests
import netman
import time
import utime
import ujson
from machine import Pin
import gc
import ubinascii
import hashlib

from urlencode import urlencode
from picochromecast import play_url

key = 'UkXp2s5v8y/B?D(G+KbPeShVmYq3t6w9'

def unixTimestamp():
    return round(time.time() * 1000)

timestamp = unixTimestamp()
# print('Unix Timestamp:', timestamp)  # 1685077947735
                                      # 1685077297474

encrypted = hashlib.sha256(str(timestamp).encode('utf-8')).digest()
encrypted_hex = ubinascii.hexlify(encrypted).decode('utf-8')
print(encrypted_hex)

def bartgpt(prompt):
    headers = {
            'Host': ' bratgpt.com',
            'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Accept': ' application/json, text/plain, */*',
            'Accept-Language': ' en-US,en;q=0.5',
            'X-Requested-With': ' XMLHttpRequest',
            'Content-Type': ' application/json',
            'Origin': ' https://bratgpt.com',
            'Connection': ' keep-alive',
            'Sec-Fetch-Dest': ' empty',
            'Sec-Fetch-Mode': ' cors',
            'Sec-Fetch-Site': ' same-origin',
            'token': encrypted_hex

        }
    
    payload = '{"prompt": [{"role": "user", "content": "' + prompt +'"}]}'
    #print(payload)
    
    response = urequest1.post('https://bratgpt.com/api/generate', data=payload, headers=headers)
    if response.status_code == 500:
        error_message = response.json()["error"]["message"]
        # Handle the error
        print("Error 500: ", error_message)
    else:
        print(response.text)
        response_content = response.content.decode('utf-8')
        response_text = response_content.replace('\n', '')
        print(response_text)

        url = 'https://translate.google.com/translate_tts?client=tw-ob&' + urlencode({'q': response_text, 'tl': 'en'})
        play_url(url, '192.168.50.23')
    
    response.close()
    return
        
country = 'SG'
ssid = ''
password = ''
wifi_connection = netman.connectWiFi(ssid,password,country)


while True:
    gc.collect()
    bartgpt("write a humor in english. Reply nicely in english in very short 2 sentences and translate to english")
    time.sleep(10) 
