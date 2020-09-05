from .model import Model


class UserLog(Model):
    
    def __init__(self, **kwargs):
        super().__init__(self, kwargs)
        
    class Meta:
        fields = ["username", "nextUsernameReplacementDate", "nextEmailReplacementDate"]