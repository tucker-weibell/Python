import requests

x = 2

while x != 1:
    string = input("Enter the IP of the website (ctrl C + Enter to exit): ")
    try:
        response = requests.get("https://" + string, verify=False)
        print(response.status_code)
    except:
        print("BAD IP")
