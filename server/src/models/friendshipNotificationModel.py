import random
from datetime import datetime
from .model import Model
from src.etc.constants import OtherConstants



class FriendshipNotification(Model):
    
    def __init__(self, **kwargs):
        super().__init__(self, kwargs)
        
    class Meta:
        fields = ["username", "id", "date", "content", "isRead"]
        
    @staticmethod
    def createNotification(username, content):
        notificationId = random.randint(0, pow(2, 32))
        date = datetime.now().strftime(OtherConstants.DATE_FORMAT)
        
        FriendshipNotification(username=username, id=notificationId, date=date, content=content, isRead=False).create()
