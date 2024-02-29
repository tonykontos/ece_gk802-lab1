#Αντώνης Κοντονάσιος
#Απάντηση της 1ης εργαστηριακής άσκησης

import requests

# Ask the user to input a URL
url = input('Enter the URL: ')

# Checking if URL starts with https 
if not url.startswith("https://"):
    url = "https://" + url

# Making an HTTP request to the URL
with requests.get(url) as response:
    # Print the HTTP response headers
    print(f"Website Headers are {url} \n , {response.headers} \n\n")

    # Print server software information and cookie information
    server = response.headers.get('Server')

    if server:
        print(f"Server is: {server}")
    else:
        print("Server information not available.")

    cookies = response.headers.get('Set-Cookie')
    if cookies:
        print(f"Cookies are: {cookies} ")
    else:
        print("No cookies used.")