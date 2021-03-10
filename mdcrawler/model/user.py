from .initializer_model import InitializerModel
import textwrap

class User(InitializerModel):
    def __init__(self,arr=None,prop=None):
        if not prop:
            prop = 'user'
        if arr :
            super(User,self).__init__(arr,prop=prop)
                

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
            
        elif prop == 'playback_chat' :
            username = arr['message']['userName']
            user_id = arr['message']['userId']

            self.username = username
            self.user_id = user_id

        elif prop == 'room' :
            username = arr['loginname']
            user_id = arr['user_id']
            profile_pic_url = arr['avatar']
            intro = arr['intro']
            follower_count = int(arr['fans'])
            country = arr['country']
            level = int(int(arr['level']))
            exp = int(int(arr['exp']))
            gift_revenue_history = int(int(arr['gift_revenue_history']))

            self.username = username
            self.user_id = user_id
            self.profile_pic_url = profile_pic_url
            self.follower_count = follower_count
            self.country = country
            self.level = level
            self.exp = exp
            self.gift_revenue_history = gift_revenue_history

        elif prop == 'room_chat' :
            username = arr['userName']
            user_id = arr['userId']
            profile_pic_url = arr['userImg']
            level = arr['level']
            fans_level = arr['fansLevel']

            self.username = username
            self.user_id = user_id
            self.profile_pic_url = profile_pic_url
            self.level = level
            self.fans_level = fans_level
            

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

