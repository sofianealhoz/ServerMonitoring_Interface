import requests 


url  = "http://localhost:8000/usageNetwork"

def get_network_dtr(url):
    response = requests.get(url)
    bytes_received = []

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            bytes_received.append(data[i]['bytes_recv'])
        return bytes_received
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur


def get_network_utr(url):
    response = requests.get(url)
    bytes_sent = []

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            bytes_sent.append(data[i]['bytes_sent'])
        return bytes_sent[1]
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

def get_network_name(url):
    response = requests.get(url)
    names = []

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            names.append(data[i]['name'])
        return names
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur



#print(get_network_info(url))