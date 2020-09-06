from playsound import playsound
from .soundConfig import SoundConfig


class Sound:

    @staticmethod
    def playNotificationSound():
        playsound(SoundConfig.getNotificationSoundPath())

    @staticmethod
    def playChatSound():
        playsound(SoundConfig.getChatSoundPath())