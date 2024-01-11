from flask import Flask, render_template,jsonify,request, redirect, url_for
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

url= "http://karadoc.telecomste.net:8080" 
urltest ="http://localhost:8000"
url_agent_ram = "http://karadoc.telecomste.net:8080/usageRam" 
url_agent_core = "http://karadoc.telecomste.net:8080/core" 
url_agent_network = "http://karadoc.telecomste.net:8080/usageNetwork"


def update_data():
    global usages, times, network_dtr,network_utr, network_names,ramPercent
    while True:
        for server in servers :
            # Cpu info 
            new_usage = get_cpu(server['url'])
            if new_usage:
                server.setdefault("usages", []).append(new_usage)

            # RAm info 
            new_percent = get_ram_percent(server['url'])
            if new_percent:
                server.setdefault("ramPercent", []).append(new_percent)

            # Network info 
            new_data_dtr = get_network_dtr(server['url'])
            if new_data_dtr:
                server.setdefault("network_dtr", []).append(new_data_dtr)

            new_data_utr = get_network_utr(server['url'])
            if new_data_utr:
                server.setdefault("network_utr", []).append(new_data_utr)

            new_data_name = get_network_name(server['url'])
            if new_data_name:
                server.setdefault("network_names", []).append(new_data_name)

            times= server.setdefault("times",[])
            times.append(time.time())
            

            if len(server["usages"]) > max_points:
                server["usages"] = server["usages"][-max_points:]
                server["times"] = times[-max_points:]

            if len(server["network_dtr"]) > max_points:
                server["network_dtr"] = server["network_dtr"][-max_points:]

            if len(server["network_utr"]) > max_points:
                server["network_utr"] = server["network_utr"][-max_points:]

        time.sleep(1)


# Liste pour stocker les infos des servers
servers= [
    {'url': urltest, 'id' : 1},
]

#Ajout d'un serveur
def add_server(url):
    servers.append({'url' : url,'id':len(servers)+1})

# Menu Principal
@app.route('/')
def index():
    return render_template('index.html',servers = servers)

# Menu d'ajout d'un serveur
@app.route('/add_server_route.html',methods=['GET','POST'])
def add_server_route():
    if request.method == 'POST':
        server_url = request.form.get('server_url')
        add_server(server_url)
        return redirect(url_for('index'))
    return render_template('add_server_route.html')


# Menu principal d'un serveur
@app.route('/server/<int:server_id>/infos.html')
def server_info(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if server:
        # Logique pour récupérer les informations du serveur
        return render_template('infos.html', server=server,server_id = server_id)
    else:
        return render_template('not_found.html')

# Menu des données réseaux
@app.route('/server/<int:server_id>/network.html')
def network(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if server:
        return render_template('/network.html',max_points = max_points,server=server,server_id = server_id)
    else:
        return render_template('not_found.html')

# Menu des données système
@app.route('/server/<int:server_id>/system.html')
def system(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if server:
        nb_core = get_number_cpu(server['url'])
        total_ram = get_ram_total(server['url'])
        return render_template('/system.html', max_points = max_points, nb_core = nb_core,total_ram = total_ram,server=server,server_id = server_id)
    else:
        return render_template('not_found.html')

# Endroit où sont stockés les données systèmes
@app.route('/server/<int:server_id>/graph/data')
def get_graph_data(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    global usages, times, ramPercent
    if server : 
        return jsonify(usages=server['usages'], times=times ,ramPercent= server['ramPercent'],server = server, server_id = server_id)
    else : 
        return render_template('not_found.html')


# Endroit où sont stockés les données réseaux
@app.route('/server/<int:server_id>/graph/dataNetwork')
def get_network_graph_data(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    global network_dtr,times,network_utr,network_names
    if server :
        return jsonify(network_dtr= server['network_dtr'],network_utr=server['network_utr'],times = times,network_names=server['network_names'],server=server,server_id=server_id)
    else : 
        return render_template('not_found.html')


if __name__ == '__main__':
    update_thread = Thread(target=update_data)
    update_thread.daemon = True
    update_thread.start()
    app.run(host='0.0.0.0', port=5000, debug=True)