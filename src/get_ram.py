import requests

# Méthode qui renvoie le total de la RAM
def get_ram_total(url):
    response = requests.get(f"{url}/usageRam")
    
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        return float(data[-1]['total'])
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

# Méthode qui renvoie le pourcentage d'utilisation de la ram
def get_ram_percent(url):
    response = requests.get(f"{url}/usageRam")
    if response.status_code == 200 : 
        data = response.json()  # Si la réponse est en format JSON
        return data[-1]['percent']
    else : 
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

# Méthode qui renvoie la fréquence de la RAM        
def get_ram_frequency(url):
    response = requests.get(f"{url}/usageRam")
    if response.status_code == 200 : 
        data = response.json()
        return float(data[0]['frequency'])  # Adjust the key accordingly

# Méthode qui renvoie l'utilisation de la RAM
def get_ram_used(url):
    response = requests.get(f"{url}/usageRam")
    if response.status_code == 200 : 
        data = response.json()  # Si la réponse est en format JSON
        return float(data[-1]['used'])
    else : 
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

