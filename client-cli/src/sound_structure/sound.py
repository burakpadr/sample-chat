from playsound import playsound
from .soundConfig import SoundConfig


class Sound:

    @staticmethod
    def playNotificationSound():
        if SoundConfig.getGeneralSoundStatus() and SoundConfig.getNotificationSoundStatus():
            playsound(SoundConfig.getNotificationSoundPath())

    @staticmethod
    def playChatSound():
        if SoundConfig.getGeneralSoundStatus() and SoundConfig.getNotificationSoundStatus():
            playsound(SoundConfig.getChatSoundPath())