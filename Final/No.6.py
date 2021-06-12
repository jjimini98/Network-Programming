import requests
import cv2
import json

API_URL = "https://dapi.kakao.com/v2/vision/adult/detect"
REST_API_KEY = 'fd7dba8acafaa23e997bc055ba31530f'

def detect_adult(image_path):
    headers = {'Authorization' : 'KakaoAK {}'.format(REST_API_KEY)}
    resp = requests.post(API_URL, headers= headers, files = {'image':open(image_path, 'rb')})
    result = resp.json()['result']

    sorted_result = sorted(result.items(),reverse=True, key=lambda item:item[1])
    for key,value in sorted_result:
        print(key, ":", value)

detect_adult("./iot.png")