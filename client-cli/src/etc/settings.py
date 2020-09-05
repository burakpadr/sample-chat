import os


class Settings:

    # Fundamentals Paths

    BASE_DIR = os.getcwd()
    SOUNDS_DIR = BASE_DIR + "/src/sound_structure/sounds" 

    # Server Connection Properties

    __CONNECTION_PROTOCOL = "http"
    __HOST = "192.168.1.27"
    __PORT = 8080
    URL = f"{__CONNECTION_PROTOCOL}://{__HOST}:{__PORT}"
