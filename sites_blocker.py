import time
from datetime import datetime as dt


path_host = r"c:\Windows\System32\drivers\etc\hosts"
#path_host = "hosts"
redirect = "127.0.0.1"
websites = ["www.vk.com", "vk.com"]

count = 0
while True:
    if 8 < dt.now().hour < 16:
        with open(path_host, "r+") as myfile:
            content = myfile.read()
            for ws in websites:
                if ws in content:
                    pass
                else:
                    myfile.write(redirect + "       " + ws + "\n")
        print(1)
        time.sleep(5)
    else:
        with open(path_host, "r+") as myfile:
            content = myfile.readlines()
            myfile.seek(0)
            for line in content:
                if not any(ws in line for ws in websites):
                    myfile.write(line)
            myfile.truncate()

        print(2)
        time.sleep(5)
    