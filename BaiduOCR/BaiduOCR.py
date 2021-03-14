import requests
import base64


def get_access_token(url, api_key, secret_key):
    url += "?grant_type=client_credentials&client_id={}&client_secret={}".format(api_key, secret_key)
    return requests.post(url).json()["access_token"]


def ocr(access_token, url, filename, img_type):
    with open(filename, mode="rb") as f:
        data = f.read()
        base64_code = "data:image/{};base64,{}".format(img_type, base64.b64encode(data).decode())

        url += "?access_token={}".format(access_token)

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data_json = {
            "image": base64_code,
            # "language_type": "ENG"
        }

        result = requests.post(url, data=data_json).json()

        final_result = ""

        for word in result["words_result"]:
            final_result += word["words"].replace(" ", "")

        return final_result


if __name__ == "__main__":
    url_auth = "https://aip.baidubce.com/oauth/2.0/token"
    url_ocr = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    api_key = "OqriWbs7YCc57oWPM2RTtTuw"
    secret_key = "P5L5Wz1k75SMgZOGqypNVANNWt4nibm4"

    access_token = get_access_token(url_auth, api_key, secret_key)

    final_str = ""
    for x in range(4):
        final_str += ocr(access_token, url_ocr, "img/{}.png".format(x + 1), "png")

    print(final_str)

    # with open("out.txt", "w", encoding="utf-8") as f:
    #     f.write(final_str)
