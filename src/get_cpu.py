import requests

# Méthode pour récupérer la moyenne d'utilisation des CPU
def get_cpu(url):
    response = requests.get(f"{url}/usage")
    usage_cpu = 0
    nb_cpu = 0  
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            usage_cpu += float(data[i]['usage']) # On somme les différents usage CPU
            nb_cpu +=1
        return usage_cpu / nb_cpu # On fait ensuite la moyenne
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur
        return 0
        

# Méthode pour récupérer le nombre de coeurs
def get_number_cpu(url):
    response = requests.get(f"{url}/core")
    if response.status_code == 200 : 
        data = response.json()
        return float(data['number']) # On récupère la donnée que l'on veut 
    else : 
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

# Méthode pour récupérer la fréquence du CPU
def get_cpu_frequency(url):
    response = requests.get(f"{url}/usage")
    if response.status_code == 200 : 
        data = response.json()
        # Assuming 'frequency' is a key in the response JSON
        return float(data[0]['frequency'])  # Adjust the key accordingly
    else : 
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur        
        return 0


