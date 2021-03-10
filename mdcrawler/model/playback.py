from .initializer_model import InitializerModel
from .user import User
import textwrap

class PlayBack(User):
    def __init__(self,arr=None,prop=None):
        if not prop:
            prop = 'playback'
        if arr:
            super(PlayBack,self)._init_properties_custom(arr,prop=prop)
            super(PlayBack,self).__init__(arr,prop=prop)


    def _init_properties_custom(self, arr, prop):
        if prop == 'playback':
            pbid = arr['live_id']
            publish_time = int(int(arr['publish_time'])/1000)
            title = arr['title']
            view_num = arr['view_num']
            length = arr['video_length']
            self.pbid = pbid
            self.publish_time = publish_time
            self.title = title
            self.view_num = view_num
            self.length = int(length)

        elif prop == 'playback_chat':
            pbid = arr['pbid']
            self.pbid = pbid

        elif prop == 'live':
            pass
    def __str__(self):
        string = f"""
        PlayBack info:
        PlayBackId: {self.pbid if hasattr(self, 'pbid') else '-'}
        Username: {self.username if hasattr(self, 'username') else '-'}
        UserId: {self.user_id if hasattr(self, 'user_id') else '-'}
        PublishTime: {self.publish_time if hasattr(self, 'publish_time') else '-'}
        Title: {self.title if hasattr(self, 'title') else '-'}
        ViewNum: {self.view_num if hasattr(self, 'view_num') else '-'}
        Length: {self.length  if hasattr(self, 'length') else '-'}
        """
        return textwrap.dedent(string)





		
	
	
	
