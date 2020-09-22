# sample-chat

**sample-chat** is a chat application that works on cli (command line interface). created with the **python** programming language and basic client-server architecture. **sample-chat** application consists of two main parts as **Server** and **Client**.

# Properties

- Membership structure (permanent account)
- Friendship structure
- Sound notification structure
- Chat with your friends permanently

# Supported Platforms

- Linux
- Mac Os
- Windows 10

**Note**:   **sample-chat** currently only works on **LAN (Local Area Network)**

# Server Setup

The **server** works on all computers on the **LAN (Local Area Network)**

- **Prerequisites**
	- Python 3.6.x or greater
	See the [Python](https://www.python.org/) installation documents
	- MongoDB localhost
	See the [MongoDB](https://docs.mongodb.com/manual/installation/) installation documents

- **Python Requirements Installation**
	- Go into  **"server"** file and you run the following command   
		> `$ pip install -r requirements.txt`

- **Start The Server**
	- Go into **"server"** file and you run following command
		> `$ python app.py`
	- After running the above command, the server will be starting. Then the picture below will appear
	
		![alt text](https://github.com/burakpadr/sample-chat/blob/master/server/media/server-started.png)	

# Client Setup

 **Client** works by connecting to a **server** running on the **LAN (Local Area Network)**

- **Prerequisites**
	- Python 3.6.x or greater
		See the [Python](https://www.python.org/) installation documents

- **Python Requirements Installation**
	- Go into  **"client-cli"** file and you run the following command   
		> `$ pip install -r requirements.txt`

- **Start The Client**
	- If the **client** is running for the first time, go to **"/client-cli/src/etc/settings.py"** and assign the running server's  **LAN** address to the **"__HOST"** variable in the file.
		- **Example**: `__HOST = "192.168.1.27"`
	
	- If the **client** is not running for the first time,  go into **"client-cli"** file and run the following code
		> `$ python app.py`
		
	- After running the above command, the **client** will be starting. Then the picture below will appear

		![enter image description here](https://github.com/burakpadr/sample-chat/blob/master/client-cli/media/client-cli-access.png)

# Pictures
	
![enter image description here](https://github.com/burakpadr/sample-chat/blob/master/client-cli/media/client-cli-request.png)

![enter image description here](https://github.com/burakpadr/sample-chat/blob/master/client-cli/media/client-cli-notification1.png)

![enter image description here](https://github.com/burakpadr/sample-chat/blob/master/client-cli/media/client-cli-accept.png)

![enter image description here](https://github.com/burakpadr/sample-chat/blob/master/client-cli/media/client-cli-notification2.png)

![enter image description here](https://github.com/burakpadr/sample-chat/blob/master/client-cli/media/client-cli-chat1.png)

![enter image description here](https://github.com/burakpadr/sample-chat/blob/master/client-cli/media/client-cli-chat2.png)
