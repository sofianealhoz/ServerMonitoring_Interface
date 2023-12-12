import requests

url = "http://localhost:8000/usage"  # Remplacez "votre_endpoint" par le chemin de l'API que vous souhaitez interroger



def get_cpu(url):
    # Exemple de requête GET
    response = requests.get(url)

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()  # Si la réponse est en format JSON
        return data
    else:
        print(f"Erreur lors de la requête GET. Code de statut : {response.status_code}")
        print(response.text)  # Affiche le contenu de la réponse en cas d'erreur

print(get_cpu(url))