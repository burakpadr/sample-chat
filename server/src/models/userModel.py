from .model import Model


class User(Model):
    
    def __init__(self, **kwargs):
        super().__init__(self, kwargs)
    
    class Meta:
        fields = ["username", "password", "email"]