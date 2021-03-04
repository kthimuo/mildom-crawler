from .initializer_model import InitializerModel
import textwrap

class User(InitializerModel):
    def __init__(self,arr=None):
        if arr :
            super().__init__(arr,prop='user')

    def _init_properties_custom(self, arr, prop):
        if prop == 'user':
            username = arr['user_info']['loginname']
            user_id = arr['user_info']['user_id']
            profile_pic_url = arr['user_info']['avatar']
            intro = arr['user_info']['intro']
            follower_count = int(arr['user_info']['fans'])
            follow_count = int(arr['user_info']['following'])
            country = arr['user_info']['country']
            level = int(int(arr['user_info']['level']))
            exp = int(int(arr['user_info']['exp']))
            gift_revenue_history = int(int(arr['user_info']['gift_revenue_history']))
            self.username = username
            self.user_id = user_id
            self.profile_pic_url = profile_pic_url
            self.follower_count = follower_count
            self.follow_count = follow_count
            self.country = country
            self.level = level
            self.exp = exp
            self.gift_revenue_history = gift_revenue_history

        elif prop == 'playback' :
            username = arr['author_info']['login_name']
            user_id = arr['author_info']['user_id']
            profile_pic_url = arr['author_info']['pic']
            follower_count = int(arr['author_info']['fans'])

            self.username = username
            self.user_id = user_id
            self.profile_pic_url = profile_pic_url
            self.follower_count = follower_count
            
        elif prop == 'chat' :
            username = arr['userName']
            user_id = arr['userId']
            profile_pic_url = arr['userImg']
            level = arr['level']

            self.username = username
            self.user_id = user_id
            self.profile_pic_url = profile_pic_url
            self.level = level


    def __str__(self):
        string = f"""
        User info:
        Username: {self.username if hasattr(self, 'username') else '-'}
        UserId: {self.user_id if hasattr(self, 'user_id') else '-'}
        Follower: {self.follower_count if hasattr(self, 'follower_count') else '-'}
        Follow: {self.follow_count if hasattr(self, 'follower_count') else '-'}
        Country: {self.country if hasattr(self, 'country') else '-'}
        Level: {self.level if hasattr(self, 'level') else '-'}
        Exp: {self.exp if hasattr(self, 'exp') else '-'}
        GiftRevenue: {self.gift_revenue_history if hasattr(self, 'gift_revenue_history') else '-'}
        """
        return textwrap.dedent(string)

