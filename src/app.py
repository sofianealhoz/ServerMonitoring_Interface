from flask import Flask, render_template,jsonify,request, redirect, url_for
import random
import time
from threading import Thread
from get_cpu import get_cpu, get_number_cpu,get_cpu_frequency
import socket 
from urllib.parse import urlparse
import requests
from get_ram import get_ram_total, get_ram_percent,get_ram_frequency, get_ram_used
from get_hdd import get_hdd_percent, get_hdd_total, get_hdd_used
from get_process import get_process_cpu, get_process_name, get_process_ram
from get_user import get_user_info
from get_log import get_nb_error404, get_nb_user
import socket 
from urllib.parse import urlparse
import requests

app = Flask(__name__)

# Nombre maximum de points à afficher dans le graphique
max_points = 100

# Initialisation des données du graphique
usages = []
usagesRam = []
ramPercent = []
ramUsed = []
times = []
hddPercent = []
hddUsed=[]

# url pour les requêtes ( à changer )

url= "http://karadoc.telecomste.net:8080" 
url2= "http://mevanwi.telecomste.net:8080"

def is_server_reachable(url):
    try:
        response = requests.get(url, timeout=5)  # Réglage d'un délai d'attente
        # Vérifier si le code de réponse est OK (200)
        return response.status_code == 200
    except requests.RequestException:
        return False


def update_data():
    global usages, times,ramPercent, ramUsed
    while True:
        for server in servers :
            if is_server_reachable(server['url']):   
                #if server['server_status'] == "Functionnal":
                # Cpu info 
                new_usage = get_cpu(server['url'])
                if new_usage:
                    server.setdefault("usages", []).append(new_usage)

                # RAm info 
                new_percent = get_ram_percent(server['url'])
                if new_percent:
                    server.setdefault("ramPercent", []).append(new_percent)
                
                new_usageRam = get_ram_used(server['url'])
                if new_usageRam:
                    server.setdefault("ramUsed", []).append(new_usageRam)

                new_usageRam = get_ram_used(server['url'])
                if new_usageRam:
                    server.setdefault("ramUsed", []).append(new_usageRam)

                # Hard Drive infos
                new_percentHdd = get_hdd_percent(server['url'])
                if new_percentHdd:
                    server.setdefault("hddPercent", []).append(new_percentHdd)
                
                new_usageHdd = get_hdd_used(server['url'])
                if new_usageHdd:
                    server.setdefault("hddUsed", []).append(new_usageHdd)

                # Top process infos
                new_process_names = get_process_name(server['url'])
                if new_process_names:
                    server.setdefault("processNames", []).append(new_process_names)

                new_processRAM = get_process_ram(server['url'])
                if new_processRAM:
                    server.setdefault("processRAM", []).append(new_processRAM)

                new_processCPU = get_process_cpu(server['url'])
                if new_processCPU:
                    server.setdefault("processCPU", []).append(new_processCPU)

                # Logs Message
                new_log404 = get_nb_error404(server['url'])
                if new_log404:
                    #server.setdefault("nb404",[]).append(new_log404)
                    server['nb404'] = new_log404

                new_NbUser = get_nb_user(server['url'])
                if new_NbUser:
                    #server.setdefault("nbUser",[]).append(new_NbUser)
                    server['nbUser'] = new_NbUser

                # Récupération du temps pour tracer en temps réel
                times= server.setdefault("times",[])
                times.append(time.time())

                if len(server["usages"]) > max_points:
                    server["usages"] = server["usages"][-max_points:]
                    server["times"] = times[-max_points:]


            # Affichage du menu principal
                
            server_functionnal = is_server_reachable(server['url'])
            server['server_status'] = "Inconnu"
            if server_functionnal:
                server['server_status'] = "Functionnal"
                server['ram_average'] = get_ram_percent(url)
                server['cpu_average'] = get_cpu(url).__round__(2)
            else:
                server['server_status'] = "Unreachable"
                server['ram_average'] = "Server unreachable"
                server['cpu_average'] = "Server unreachable"
        
        time.sleep(1)




    

#Ajout d'un serveur
def add_server(url, server_nickname):
    
    server_functionnal = is_server_reachable(url)
    server_status = "Inconnu"
    if server_functionnal:
        server_status = "Functionnal"
        hostname = urlparse(url).hostname
        IP = socket.gethostbyname(urlparse(url).hostname)
        ram_average = get_ram_percent(url)
        cpu_average = get_cpu(url).__round__(2)
    else:
        server_status = "Unreachable"
        hostname = urlparse(url).hostname
        if hostname is None:
            hostname = url
        IP = "Server unreachable"
        ram_average = "Server unreachable"
        cpu_average = "Server unreachable"
    servers.append({'url' : url,'name':server_nickname, 'id': len(servers) + 1, 'hostname': hostname, 'IP': IP, 'server_status': server_status, 'ram_average': ram_average, 'cpu_average': cpu_average})

def reassign_server_ids():
    for i, server in enumerate(servers, start=1):
        server['id'] = i


# Menu Principal
@app.route('/')
def index():
    return render_template('index.html',servers = servers) 

# Menu d'ajout d'un serveur
@app.route('/add_server_route.html',methods=['GET','POST'])
def add_server_route():
    if request.method == 'POST':
        server_nickname = request.form.get('server_nickname')
        server_url = request.form.get('server_url')
        add_server(server_url, server_nickname)
        return redirect(url_for('index'))
    return render_template('add_server_route.html')

# Suppression d'un serveur
@app.route('/remove_server/<int:server_id>', methods=['POST'])
def remove_server_route(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if server:
        servers.remove(server)
        reassign_server_ids()  # Réattribuer les IDs après la suppression
        return redirect(url_for('index'))
    else:
        return render_template('not_found.html')

# Vérification de l'état du serveur

    
# Menu principal d'un serveur
@app.route('/server/<int:server_id>/infos.html')
def server_info(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if server:
        max_points = 100
        server_functionnal = is_server_reachable(server['url'])
        if server_functionnal:
            # Logique pour récupérer les informations du serveur
            server_name = server['name']
            server_hostname = server['hostname']
            server_ip = server['IP']
            server_status = "Functionnal"
        else:
            server_status = "Not functionnal"
            server_name = server['name']
            server_hostname = server['hostname']
            if server_hostname is None:
                server_hostname = server['url']
            server_ip = "Serveur non détectée"           
        return render_template('infos.html', server=server,server_id = server_id, server_name = server_name, server_hostname = server_hostname, server_ip = server_ip, server_status = server_status, max_points = max_points)
    else:
        return render_template('not_found.html')
    


# Menu des données système
@app.route('/server/<int:server_id>/system.html')
def system(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if server['server_status'] == "Functionnal":
        nb_core = get_number_cpu(server['url'])
        total_ram = get_ram_total(server['url'])
        total_hdd = get_hdd_total(server['url'])
        return render_template('/system.html', max_points = max_points, nb_core = nb_core,total_ram = total_ram,total_hdd=total_hdd,server=server,server_id = server_id)
    else:
        return render_template('not_found.html')

# Menu des données logs
@app.route('/server/<int:server_id>/logInfos.html')
def logsInfos(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)   # On cherche le serveur dont on a l'identifiant dans le path
    if server:
        return render_template('/logInfos.html',server=server,server_id = server_id)   # on affiche la template correspondante
    else:
        return render_template('not_found.html')

# Endroit où sont stockés les données logs
@app.route('/server/<int:server_id>/graph/dataLogs') 
def get_logs_graph_data(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)   # On cherche le serveur dont on a l'identifiant dans le path
    
    if server :
        return jsonify(nb404=server["nb404"],nbUser=server["nbUser"] ,server=server,server_id=server_id, times = times)   # On affiche la template correspondante
    else : 
        return render_template('not_found.html')


# Endroit où sont stockés les données systèmes
@app.route('/server/<int:server_id>/graph/data')
def get_graph_data(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)    # On cherche le serveur dont on a l'identifiant dans le path
    global usages, times, ramPercent, ramUsed,hddPercent,hddUsed, processNames, processCPU, processRAM    # On créé les variables qu'on a besoin d'importer
    if server : 
        return jsonify(usages=server['usages'], times=times ,ramPercent= server['ramPercent'],server = server, server_id = server_id, ramUsed = server.get('ramUsed', 'N/A'),hddPercent=server.get('hddPercent', 'N/A'),hddUsed = server.get('hddUsed', 'N/A'), processNames = server['processNames'], processCPU = server['processCPU'], processRAM = server['processRAM'])
    else : 
        return render_template('not_found.html')



        
# Endroit pour les static infos (user infos pour le moment)
@app.route('/server/<int:server_id>/static_infos.html')
def static_info(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if server['server_status'] == "Functionnal":
        user_info = get_user_info(server['url'])
        
        user_info = [
            {
                'nickname': server['name'],
                'hostname': server['hostname'],
                'ip': server['IP']
            }
        ]
        cpu_frequency = str((get_cpu_frequency(server['url'])).__round__(2)) + " MHz"
        nb_core = get_number_cpu(server['url'])
        ram_frequency = str((get_ram_frequency(server['url']) / 1000000000).__round__(2)) + " GHz"
        ram_total =str(get_ram_total(server['url'])) + " GB"
        return render_template('static_infos.html', server=server, user_info=user_info, server_id=server_id,cpu_frequency=cpu_frequency,nb_core=nb_core,ram_frequency=ram_frequency,ram_total=ram_total)
    else:
        return render_template('not_found.html')

# Liste pour stocker les infos des servers
servers= [
    {
        'url': url, 
        'name' : "karadoc",
        'id': 1, 
        'hostname': urlparse(url).hostname,
        'IP': socket.gethostbyname(urlparse(url).hostname),
        'server_status': "Fonctionnel" if is_server_reachable(url) else "Non fonctionnel",
        'ram_average': get_ram_percent(url),
        'cpu_average': get_cpu(url).__round__(2)
    },
    {
        'url': url2,
        'name' : "mevanwi",
        'id': 2, 
        'hostname': urlparse(url2).hostname,
        'IP': socket.gethostbyname(urlparse(url2).hostname),
        'server_status': "Fonctionnel" if is_server_reachable(url2) else "Non fonctionnel",
        'ram_average': get_ram_percent(url2),
        'cpu_average': get_cpu(url2).__round__(2)
    }
]

if __name__ == '__main__':
    update_thread = Thread(target=update_data)
    update_thread.daemon = True
    update_thread.start()
    app.run(host='0.0.0.0', port=5000, debug=True)