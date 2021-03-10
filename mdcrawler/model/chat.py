from .user import User
from .playback import PlayBack
from .room import Room
import textwrap
import json

class PlayBackChat(PlayBack):
    def __init__(self,arr=None, prop=None):
        if not prop:
            prop = 'playback_chat'
        if arr:
            arr['message'] = json.loads(arr['message'])
            super(PlayBackChat,self).__init__(arr,prop=prop)
            super(PlayBackChat,self)._init_properties_custom(arr,prop=prop)

    def _init_properties_custom(self, arr,prop=None):
        if prop == 'playback_chat':
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
        PlayBackChat info:
        ChatId: {self.chat_id if hasattr(self, 'chat_id') else '-'}
        ChatText: {self.chat_text if hasattr(self, 'chat_text') else '-'}
        ChatTime: {self.chat_time if hasattr(self, 'chat_time') else '-'}
        ChatTimeOffset: {self.chat_time_offset if hasattr(self, 'chat_time_offset') else '-'}
        Username: {self.username if hasattr(self, 'username') else '-'}
        UserId: {self.user_id if hasattr(self, 'user_id') else '-'}
        PlayBackId: {self.pbid if hasattr(self, 'pbid') else '-'}
        """

        return textwrap.dedent(string)


class RoomChat(Room):
    def __init__(self,arr=None, prop=None):
        if not prop:
            prop = 'room_chat'
        if arr:
            super(RoomChat,self).__init__(arr,prop=prop)
            super(RoomChat,self)._init_properties_custom(arr,prop=prop)

    def _init_properties_custom(self, arr,prop=None):
        if prop == 'room_chat':
            chat_text = arr['msg']
            chat_id = arr['msgId']
            chat_time = int(int(arr['time'])/1000)
            self.chat_text = chat_text
            self.chat_id = chat_id
            self.chat_time = chat_time

    def __str__(self):
        string = f"""
        RoomChat info:
        ChatId: {self.chat_id if hasattr(self, 'chat_id') else '-'}
        ChatText: {self.chat_text if hasattr(self, 'chat_text') else '-'}
        ChatTime: {self.chat_time if hasattr(self, 'chat_time') else '-'}
        Username: {self.username if hasattr(self, 'username') else '-'}
        UserId: {self.user_id if hasattr(self, 'user_id') else '-'}
        RoomId: {self.room_id if hasattr(self, 'room_id') else '-'}
        """
        return textwrap.dedent(string)

