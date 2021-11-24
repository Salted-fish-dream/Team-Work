from Birds import settings
import requests




def get_login_info(code):
    code_url = settings.code2Session.format(settings.AppId, settings.AppSecret, code)
    response = requests.get(code_url)
    json_response = response.json()  # 把它变成json的字典
    if json_response.get("session_key"):
        return json_response
    else:
        return False
