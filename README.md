# Simple-Client-Server
This is a simple client server program in python. It can host as many clients as you like.

# Pre-set up:
1. Install python IDLE [here](https://www.python.org/downloads/).
2. Make sure you install it **with** path otherwise installing external modules will be very difficult.
3. run `pip install pygame` in cmd or powershell.
4. run `pip install rsa` in cmd or powershell.
5. run `pip instsall pycryptodome` in cmd or powershell.
6. Make sure that your filewall has enabled python for private and public so that other computers on your local network can join the server.

# Set up:
1. Download this repository.
2. Extract it all.
3. Make sure you edit the settings folder to be a port you want and the server ip you want.
4. If you are running the server application then you can keep `self.SERVER = gethostbyname(self.HOST_NAME)` otherwise change it to the hosts ip address.
5. To get your IP address run `ipconfig` on cmd or powershell under the `ipv4` section. Then give that ipv4 address to the clients. So `self.SERVER = "YOUR HOST IPV4"`

# How to run:
1. First run an instance of server.py with `py server.py` on cmd or powershell or python IDLE it doesn't really matter.
2. Now you can run as many instances of client.py with `py client.py` on cmd or powershell or python IDLE it doesn't really matter.
3. Now you can play with it and have fun!

# Notes
1. The code has been designed to be a bullet proof simple method to host as many players on a server as you would like.
2. The encryption does work but the key is sent through first to each client without any encryption. Other than that all the player objects are encrypted.
3. Finally, if you need any help feel free to message me if you find any errors or you are struggling to set this up. My Discord is @realdl

# Thank you. 🙏
Thank you for reading this. Feel free to check out my other repositories.
