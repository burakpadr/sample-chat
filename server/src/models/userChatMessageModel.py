from .model import Model


class UserChatMessage(Model):

    def __init__(self, **kwargs):
        super().__init__(self, kwargs)

    class Meta:
    
        fields = ["username", "chatWith", "newMessageSize", "stream"]
