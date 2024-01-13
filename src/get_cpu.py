import requests

def get_cpu(url):
    # Exemple de requête GET
    response = requests.get(f"{url}/usage")
    usage_cpu = 0
    nb_cpu = 0  
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            usage_cpu += float(data[i]['usage'])
            nb_cpu +=1
        return usage_cpu / nb_cpu
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

def get_number_cpu(url):
    response = requests.get(f"{url}/core")
    if response.status_code == 200 : 
        data = response.json()
        return float(data['number'])
    else : 
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur
def get_cpu_frequency(url):
    response = requests.get(f"{url}/usage")
    if response.status_code == 200 : 
        data = response.json()
        # Assuming 'frequency' is a key in the response JSON
        return float(data[0]['frequency'])  # Adjust the key accordingly
    else : 
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur        


