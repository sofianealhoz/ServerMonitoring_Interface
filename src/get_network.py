import requests 


url  = "http://localhost:8000/usageNetwork"

def get_network_info(url):
    response = requests.get(url)
   
    name = []
    bytes_sent = []
    bytes_received = []

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            name.append(data[i]['name'])
            bytes_sent.append(data[i]['bytes_sent'])
            bytes_received.append(data[i]['bytes_recv'])
        return name[1],bytes_sent[1],bytes_received[1]
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur


print(get_network_info(url))