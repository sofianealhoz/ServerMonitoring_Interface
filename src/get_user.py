import requests

url = "http://karadoc.telecomste.net:8080"

def get_user_info(url):
    # Example GET request
    response = requests.get(f"{url}/users")

    if response.status_code == 200:
        user_data = response.json()
        user_list = []

        for user_entry in user_data:
            nickname = user_entry.get('nickname')
            hostname = user_entry.get('hostname')
            ip = user_entry.get('ip')

            user_list.append({'nickname': nickname, 'hostname': hostname, 'ip': ip})

        return user_list
    else:
        print(f"Error during GET request. Status code: {response.status_code}")
        print(response.text)  # Display the response content in case of an error

# Example usage:
users_info = get_user_info(url)
print(users_info)
