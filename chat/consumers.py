import json
from channels.generic.websocket import WebsocketConsumer
from .translation import translate_text

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)

        message = data['message']
        lang = data['lang']

        translated = translate_text(message, lang)

        self.send(text_data=json.dumps({
            'translated': translated
        }))