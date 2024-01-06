from flask import Flask, render_template,jsonify
import random
import time
from threading import Thread
from get_cpu import get_cpu, get_number_cpu
from get_network import get_network_dtr, get_network_utr, get_network_name
from get_ram import get_ram_total, get_ram_percent

app = Flask(__name__)

# Nombre maximum de points à afficher dans le graphique
max_points = 100

# Initialisation des données du graphique
usages = []
usagesRam = []
ramPercent = []
network_dtr = []
network_utr = []
times = []
network_names = []

# url pour les requêtes ( à changer )
url_agent_cpu = "http://localhost:8000/usage" 
url_agent_ram = "http://localhost:8000/usageRam" 
url_agent_core = "http://localhost:8000/core" 
url_agent_network = "http://localhost:8000/usageNetwork"

def update_data():
    global usages, times, network_dtr,network_utr, network_names,ramPercent
    while True:
        # Cpu info 
        new_usage = get_cpu(url_agent_cpu, url_agent_core)
        usages.append(new_usage)

        # RAm info 
        new_percent = get_ram_percent(url_agent_ram)
        ramPercent.append(new_percent)

        # Network info 
        new_data = get_network_dtr(url_agent_network)
        network_dtr.append(new_data)

        new_data = get_network_utr(url_agent_network)
        network_utr.append(new_data)

        new_data = get_network_name(url_agent_network)
        network_names.append(new_data)

        times.append(time.time())
        

        if len(usages) > max_points:
            usages = usages[-max_points:]
            times = times[-max_points:]

        if len(network_dtr) > max_points:
            network_dtr = network_dtr[-max_points:]
            times = times[-max_points:]

        if len(network_utr) > max_points:
            network_utr = network_utr[-max_points:]
            times = times[-max_points:]

        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/network.html')
def network():
    return render_template('/network.html',max_points = max_points)

@app.route('/system.html')
def system():
    nb_core = get_number_cpu(url_agent_core)
    total_ram = get_ram_total(url_agent_ram)
    return render_template('/system.html', max_points = max_points, nb_core = nb_core,total_ram = total_ram)

@app.route('/graph/data')
def get_graph_data():
    global usages, times, ramPercent
    return jsonify(usages=usages, times=times ,ramPercent= ramPercent)



@app.route('/graph/dataNetwork')
def get_network_graph_data():
    global network_dtr,times,network_utr,network_names
    return jsonify(network_dtr= network_dtr,network_utr=network_utr,times = times,network_names=network_names)

if __name__ == '__main__':
    update_thread = Thread(target=update_data)
    update_thread.daemon = True
    update_thread.start()
    app.run('0.0.0.0', port=5000, debug=True)