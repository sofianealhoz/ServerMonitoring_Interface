import requests

url = "http://localhost:8000/usage"
url_core = "http://localhost:8000/core" 

def get_cpu(url):
    # Exemple de requête GET
    response = requests.get(url)
    usage_cpu = 0
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        for i in range(len(data)):
            usage_cpu += float(data[i]['usage'])
        return usage_cpu
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

def get_number_cpu(url):
    response = requests.get(url)
    if response.status_code == 200 : 
        data = response.json()
        return int(data['number'])
    else : 
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur


print(get_cpu(url))
print(get_number_cpu(url_core))
