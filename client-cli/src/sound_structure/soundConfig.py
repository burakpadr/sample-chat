from src.etc.settings import Settings


class SoundConfig:
    
    # Sounds
    
    __NOTIFICATION_SOUND = Settings.SOUNDS_DIR + "/notification.mp3"
    __CHAT_SOUND = Settings.SOUNDS_DIR + "/chat.mp3"
    
    # General Sound Settings
    
    __GENERAL_SOUND_STATUS = True
    __NOTIFICATION_SOUND_STATUS = True
    
    @staticmethod
    def getNotificationSoundPath():
        return SoundConfig.__NOTIFICATION_SOUND
    
    @staticmethod
    def getChatSoundPath():
        return SoundConfig.__CHAT_SOUND

    @staticmethod
    def getGeneralSoundStatus():
        return SoundConfig.__GENERAL_SOUND_STATUS
    
    @staticmethod
    def getNotificationSoundStatus():
        return SoundConfig.__NOTIFICATION_SOUND_STATUS
    
    @staticmethod
    def setGeneralNotificationStatus(status):
        SoundConfig.__GENERAL_SOUND_STATUS = status
    
    @staticmethod
    def setNotificationSoundStatus(status):
        SoundConfig.__NOTIFICATION_SOUND_STATUS = status
    