from src.etc.settings import Settings


class SoundConfig:
    
    # Sounds
    
    __NOTIFICATION_SOUND = Settings.SOUNDS_DIR + "/notification.mp3"
    __CHAT_SOUND = Settings.SOUNDS_DIR + "/chat.mp3"
    
    
    @staticmethod
    def getNotificationSoundPath():
        return SoundConfig.__NOTIFICATION_SOUND
    
    @staticmethod
    def getChatSoundPath():
        return SoundConfig.__CHAT_SOUND
