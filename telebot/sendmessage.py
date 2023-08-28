import requests
from .models import TeleSettings


def send_telegram(name, phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.token)
        chat_id = str(settings.chat)
        text = str(settings.message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}') + 1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]

            text_slise = part_1 + name + part_2 + phone + part_3
        else:
            text_slise = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Sending error')
            elif req.status_code == 500:
                print('500 ERROR!')
            else:
                print('OK. Message sent')
    else:
        pass
