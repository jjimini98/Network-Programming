import json

dict_data = {'Name' : "Jimin", "Department": "Bigdata", "University":"SoonChunHyang"}

with open("data.json", 'w') as f:
    json.dump(dict_data, f)