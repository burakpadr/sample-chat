import os
import sys
import socket
from subprocess import check_output


class Settings:
    
    # Fundamental Paths
    
    BASE_DIR = os.getcwd()
    
    # Server Properties
    
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 8080
    
    if sys.platform == "linux" or sys.platform == "darwin":
        HOST = check_output(['hostname', '--all-ip-addresses']).decode("utf-8")[:-1]
    
    # Database Properties
    
    MONGODB_URI = "mongodb://localhost:27017/"
    