import requests 

def get_nb_error404(url):
    response = requests.get(f"{url}/logMessage")
    if response.status_code == 200:
        data=response.json()
        return data[-1]['nb_error404']
    else:
        print(f"Error during GET request. Status code: {response.status_code}")
        print(response.text)  # Display the response content in case of an error

def get_nb_user(url): 
    response = requests.get(f"{url}/logMessage")
    if response.status_code == 200:
        data=response.json()
        return data[-1]['unique_users']
    else:
        print(f"Error during GET request. Status code: {response.status_code}")
        print(response.text)  # Display the response content in case of an error

def get_lasterror(url):
    response = requests.get(f"{url}/logMessage")
    if response.status_code == 200:
        data=response.json()
        return data[-1]['last_5_error_logs']
    else:
        print(f"Error during GET request. Status code: {response.status_code}")
        print(response.text)  # Display the response content in case of an error

