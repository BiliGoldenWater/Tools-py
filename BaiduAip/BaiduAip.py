from aip import AipSpeech

app_id = ""
api_key = ""
secret_key = ""

client = AipSpeech(app_id, api_key, secret_key)

result = client.synthesis("测试", "zh", 1, {
    "vol": 5,
})

if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
else:
    print(result)
