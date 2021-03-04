from .user import User
from .playback import PlayBack
import textwrap
import json

class Chat(PlayBack):
    def __init__(self,arr=None):
        if arr:
            arr['message'] = json.loads(arr['message'])
            super().__init__(arr,prop='chat')
            super()._init_properties_custom(arr,prop='chat')

    def _init_properties_custom(self, arr,prop=None):
        chat_text = arr['message']['msg']
        chat_id = arr['message']['msgId']
        chat_time = int(int(arr['message']['time'])/1000)
        chat_time_offset = int(int(arr['time_offset_ms'])/1000)
        self.chat_text = chat_text
        self.chat_id = chat_id
        self.chat_time = chat_time
        self.chat_time_offset = chat_time_offset

    def __str__(self):
        string = f"""
        Chat info:
        ChatId: {self.chat_id if hasattr(self, 'chat_id') else '-'}
        ChatText: {self.chat_text if hasattr(self, 'chat_text') else '-'}
        ChatTime: {self.chat_time if hasattr(self, 'chat_time') else '-'}
        ChatTimeOffset: {self.chat_time_offset if hasattr(self, 'chat_time_offset') else '-'}
        Username: {self.username if hasattr(self, 'username') else '-'}
        UserId: {self.user_id if hasattr(self, 'user_id') else '-'}
        PlayBackId: {self.pbid if hasattr(self, 'pbid') else '-'}
        """
        return textwrap.dedent(string)

