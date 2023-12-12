from flask import Flask, render_template,jsonify
import random
import time
from threading import Thread
from get_cpu import get_cpu, get_number_cpu

app = Flask(__name__)

# Nombre maximum de points à afficher dans le graphique
max_points = 100

# Initialisation des données du graphique
usages = []
times = []

# url pour les requêtes ( à changer )
url_agent_cpu = "http://localhost:8000/usage" 
url_agent_core = "http://localhost:8000/core" 

def update_data():
    global usages, times
    while True:
        new_usage = get_cpu(url_agent_cpu, url_agent_core)
        usages.append(new_usage)
        times.append(time.time())
        

        if len(usages) > max_points:
            usages = usages[-max_points:]
            times = times[-max_points:]

        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/network.html')
def network():
    return render_template('/network.html')

@app.route('/system.html')
def system():
    nb_core = get_number_cpu(url_agent_core)
    return render_template('/system.html', max_points = max_points, nb_core = nb_core)

@app.route('/graph/data')
def get_graph_data():
    global usages, times
    return jsonify(usages=usages, times=times)

if __name__ == '__main__':
    update_thread = Thread(target=update_data)
    update_thread.daemon = True
    update_thread.start()
    app.run(debug=True)