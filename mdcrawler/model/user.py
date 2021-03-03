from .initializer_model import InitializerModel
import textwrap

class User(InitializerModel):
    def __init__(self,arr=None):
        self.username = None
        self.user_id = None
        self.profile_pic_url = None
        self.intro = None
        self.follower_count = None
        self.follow_count = None
        self.country = None
        self.level = None
        self.exp = None
        self.gift_revenue_history = None
        super(User, self).__init__(arr)

    def _init_properties_custom(self, arr):
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
        self.intro = intro
        self.follower_count = follower_count
        self.follow_count = follow_count
        self.country = country
        self.level = level
        self.exp = exp
        self.gift_revenue_history = gift_revenue_history

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

