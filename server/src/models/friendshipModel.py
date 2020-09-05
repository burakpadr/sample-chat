from .model import Model


class Friendship(Model):
    
    def __init__(self, **kwargs):
        super().__init__(self, kwargs)
    
    class Meta:
        fields = ["username", "friends", "incoming", "outgoing"]