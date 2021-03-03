import textwrap
class PlayBack:
    def __init__(self):
        self.live_id = None
        self.username = None
        self.user_id = None
        self.country = None
        self.publish_time = None
        self.title = None
        self.view_num = None
        self.length = None
    def __str__(self):
        string = f"""
        PlayBack info:
        Id: {self.live_id if hasattr(self, 'live_id') else '-'}
        Username: {self.username if hasattr(self, 'username') else '-'}
        UserId: {self.user_id if hasattr(self, 'user_id') else '-'}
        Country: {self.country if hasattr(self, 'country') else '-'}
        PublishTime: {self.publish_time if hasattr(self, 'publish_time') else '-'}
        Title: {self.title if hasattr(self, 'title') else '-'}
        ViewNum: {self.view_num if hasattr(self, 'view_num') else '-'}
        Length: {self.length  if hasattr(self, 'length') else '-'}
        """
        return textwrap.dedent(string)


if __name__ == '__main__':
    playback = PlayBack()
    print(playback)




		
	
	
	
