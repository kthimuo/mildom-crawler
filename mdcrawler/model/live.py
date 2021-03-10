from .initializer_model import InitializerModel
from .user import User
import textwrap

class Live(User):
    def __init__(self,arr=None,prop=None):
        if not prop:
            prop = 'live'
        if arr:
            super().__init__(arr,prop=prop)
            super()._init_properties_custom(arr,prop=prop)


    def _init_properties_custom(self, arr, prop):
        if prop == 'live':
            start_timestamp = int(int(arr['live_start_ms'])/1000)
            intro = arr['live_intro']
            title = arr['anchor_intro']
            self.start_timestamp = start_timestamp
            self.title = title
            self.intro = intro

    def __str__(self):
        string = f"""
        Live info:
        Title: {self.title if hasattr(self, 'title') else '-'}
        Intro: {self.intro if hasattr(self, 'intro') else '-'}
        Start: {self.start_timestamp if hasattr(self, 'start_timestamp') else '-'}
        Username: {self.username if hasattr(self, 'username') else '-'}
        UserId: {self.user_id if hasattr(self, 'user_id') else '-'}
        Follower: {self.follower_count if hasattr(self, 'follower_count') else '-'}
        Country: {self.country if hasattr(self, 'country') else '-'}
        Level: {self.level if hasattr(self, 'level') else '-'}
        Exp: {self.exp if hasattr(self, 'exp') else '-'}
        GiftRevenue: {self.gift_revenue_history if hasattr(self, 'gift_revenue_history') else '-'}
        """
        return textwrap.dedent(string)
