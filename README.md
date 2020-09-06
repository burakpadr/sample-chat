﻿# sample-chat

**sample-chat** is a chat application that works on cli (command line interface). created with the **python** programming language and basic client-server architecture. **sample-chat** application consists of two main parts as **Server** and **Client**.

# Properties

- Friendship structure
- Permanent messages with your friends
- Friendship structure notifications (friendship request notification, etc.)
- New incoming message notifications

# Supported Platforms

- Linux
- Mac Os
- Windows 10

**Note**:   **sample-chat** currently only works on **LAN (Local Area Network)**

# Server Setup

**Server** work on all computers in **LAN (Local Area Network)**

- **Prerequisites**
	- Python 3.6.x or greater
	See the [Python](https://www.python.org/) installation documents
	- MongoDB localhost
	See the [MongoDB](https://docs.mongodb.com/manual/installation/) installation documents

- **Python Requirements Installation**
	- Go into  **"server"** file and you run the following command   
		> $ `pip install -r requirements.txt`

- **Start The Server**
	- Go into **"server"** file and you run following command
		> $ `python app.py`
	- After running the above command, the server will be starting. Then the picture below will appear
	
		![enter image description here](https://raw.githubusercontent.com/burakpadr/sample-chat/master/server/media/server-started.png?token=AMDTI2RFJBD3OWHUS52PNZC7KT45M)	

# Client Setup

 **Client** works by connecting to a **server** running on the **LAN (Local Area Network)**

- **Prerequisites**
	- Python 3.6.x or greater
		See the [Python](https://www.python.org/) installation documents

- **Python Requirements Installation**
	- Go into  **"client-cli"** file and you run the following command   
		> $ `pip install -r requirements.txt`

- **Start The Client**
	- If the **client** is running for the first time, go to **"/client-cli/src/etc/settings.py"** and assign the running server's  **LAN** address to the **"__HOST"** variable in the file.
		- **Example**: `__HOST = "192.168.1.27"`
	
	- If the **client** is not running for the first time,  go into **"client-cli"** file and run the following code
		> $ `python app.py`
		
	- After running the above command, the **client** will be starting. Then the picture below will appear

		![enter image description here](https://raw.githubusercontent.com/burakpadr/sample-chat/master/client-cli/media/client-cli-access.png?token=AMDTI2WBCGD3DO7JUSTQ4GC7KUAJK)

# TODO

- Modern **GUI (Graphical User Interface)** will be created for **client** with **Electron.js**
- Group Structure will be created (Group Chat)
- Build your own server (Example: `www.example.com`)
- Connections will be with P2P Protocol

# Pictures
	
![enter image description here](https://raw.githubusercontent.com/burakpadr/sample-chat/master/client-cli/media/client-cli-request.png?token=AMDTI2Q6K7E7MXMD2SVEMGS7KUDOM)

![enter image description here](https://raw.githubusercontent.com/burakpadr/sample-chat/master/client-cli/media/client-cli-notification1.png?token=AMDTI2VVZBNHKCB5LB3IZOC7KUDRY)

![enter image description here](https://raw.githubusercontent.com/burakpadr/sample-chat/master/client-cli/media/client-cli-accept.png?token=AMDTI2UB4ZAGJ23M4GERU2S7KUDT4)

![enter image description here](https://raw.githubusercontent.com/burakpadr/sample-chat/master/client-cli/media/client-cli-notification2.png?token=AMDTI2WRJ6HXCQUSALAD4BS7KUDV4)

![enter image description here](https://raw.githubusercontent.com/burakpadr/sample-chat/master/client-cli/media/client-cli-chat1.png?token=AMDTI2RQ64L5WVNT6KYWXTS7KUDYK)

![enter image description here](https://raw.githubusercontent.com/burakpadr/sample-chat/master/client-cli/media/client-cli-chat2.png?token=AMDTI2WS6KCBNEMG4DRSWUC7KUDZY)
