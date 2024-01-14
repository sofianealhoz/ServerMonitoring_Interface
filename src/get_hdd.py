import requests

# Méthode pour récupérer l'espace occupé pour le hard drive
def get_hdd_used(url):
    response = requests.get(f"{url}/usageHdd")
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        return data['used']
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

# Méthode pour récupérer la taille total du hard drive
def get_hdd_total(url):
    response = requests.get(f"{url}/usageHdd")
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        return data['total']
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

# Méthode pour récupérer le pourcentage d'utilisation du hard drive
def get_hdd_percent(url):
    response = requests.get(f"{url}/usageHdd")
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        return data['percent']
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur
