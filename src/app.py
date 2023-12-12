from flask import Flask, render_template,jsonify
import random
import time
from threading import Thread


app = Flask(__name__)

# Nombre maximum de points à afficher dans le graphique
max_points = 100

# Initialisation des données du graphique
usages = []
times = []

def update_data():
    global usages, times
    while True:
        new_usage = random.randint(40, 80)
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
    return render_template('/system.html', max_points = max_points)

@app.route('/graph/data')
def get_graph_data():
    global usages, times
    return jsonify(usages=usages, times=times)

if __name__ == '__main__':
    update_thread = Thread(target=update_data)
    update_thread.daemon = True
    update_thread.start()
    app.run(debug=True)