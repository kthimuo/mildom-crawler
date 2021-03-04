from .user import User
import textwrap

class Chat(User):
    def __init__(self,arr):
        if arr:
            super()._init_properties_custom(arr,prop='chat')
            self._init_properties_custom(arr)

    def _init_properties_custom(self, arr):
        chat_text = arr['msg']
        chat_id = arr['msgId']
        chat_time = int(int(arr['time'])/1000)
        self.chat_text = chat_text
        self.chat_id = chat_id
        self.chat_time = chat_time

    def __str__(self):
        string = f"""
        Chat info:
        ChatId: {self.chat_id if hasattr(self, 'chat_id') else '-'}
        ChatText: {self.chat_text if hasattr(self, 'chat_text') else '-'}
        ChatTime: {self.chat_time if hasattr(self, 'chat_time') else '-'}
        Username: {self.username if hasattr(self, 'username') else '-'}
        UserId: {self.user_id if hasattr(self, 'user_id') else '-'}
        Level: {self.level if hasattr(self, 'level') else '-'}
        """
        return textwrap.dedent(string)

