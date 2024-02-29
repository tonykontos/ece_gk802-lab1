#Αντώνης Κοντονάσιος
#Απάντηση της 1ης εργαστηριακής άσκησης

import requests

# Αsk the user to input a URL
url = input("Please enter the URL: ")

# Checkin if URL starts with https or http, if not add https:// 
if not url.startswith("https://") or url.startswith("http://"):
    url = "https://" + url

# Μake an HTTP request to the URL
response = requests.get(url)

# Print the HTTP response headers
print("Response Headers:\n")
for header in response.headers:
    print(header + ":", response.headers[header])

# Print server software information and cookie information
server = response.headers.get('server')
cookies = response.cookies
if server:
    print("\nServer is: {server}")
else:
    print("\nServer information not available.")

if cookies:
    print("\nCookies:\n")
    for cookie in cookies:
        print("Name: {cookie.name}")
        print("Value: {cookie.value}")
        print("Expires: {cookie.expires}")
else:
    print("\nNo cookies used.")