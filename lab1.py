#Efthalia Liouta up1103875

import requests 

#Asks the user for a URL
url = input("Enter a URL: ")

#http request to the URL
if not url.startswith("http://"):
    url = "http://" + url

with requests.get(url) as response:  # το αντικείμενο response
    # html = response.text
    # more(html)

    #prints headers
    print(f"Website's headers are {url} \, {response.headers}\n\n")

    #server information
    server = response.headers.get('Server')

    if server:
        print(f"The server is {server}")
    else:
        print("No server was found")

    #coockies information
        
    cookies = response.headers.get('Set-Cookie')
    if cookies:
        print(f"The cookies are {cookies}")
    else:
        print("No cookie was found")