import requests


# méthode qui renvoie les noms des top process
def get_process_name(url):
    response = requests.get(f"{url}/usageProcess")
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


# méthode qui renvoie la consommation CPU des top process
def get_process_cpu(url):
    response = requests.get(f"{url}/usageProcess")
    tabCPU = []
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            tabCPU.append(data[i]['cpu_percent'])
        return tabCPU
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

# méthode qui renvoie la consommation CPU des top process
def get_process_ram(url):
    response = requests.get(f"{url}/usageProcess")
    tabRAM= []
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            tabRAM.append(data[i]['rss'])
        return tabRAM
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

