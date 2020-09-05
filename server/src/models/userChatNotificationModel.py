import random
from datetime import datetime
from .model import Model
from src.etc.constants import OtherConstants


class UserChatNotification(Model):

    def __init__(self, **kwargs):
        super().__init__(self, kwargs)

    class Meta:
        fields = ["username", "id", "date", "sender", "content", "isRead"]
        
    @staticmethod
    def createNotification(username, sender, content):
        notificationId = random.randint(0, pow(2, 32))
        date = datetime.now().strftime(OtherConstants.DATE_FORMAT)
        
        UserChatNotification(username=username, id=notificationId, date=date, sender=sender, content=content, isRead=True).create()
