# Server Monitoring Interface

Web dashboard that visualizes the servers and metrics collected by the agent
(see Server Monitoring Agent). It supports adding and removing servers, a
health view, and history graphs.

## Features

- Dashboard navigation.
- Add and remove servers dynamically.
- Health view of monitored servers.
- History graphs for key metrics (CPU, RAM, and others).

## Stack

- Python 3
- Flask (`src/app.py`, templates and static assets under `src/`)
- Docker

## Architecture

The interface queries the agent through its API to retrieve and display data.
The structure is modular, with one module per metric (`get_cpu.py`,
`get_ram.py`, `get_hdd.py`, and so on).

## Install and run

    docker build -t monitoring-interface .
    docker run -d -p 5000:5000 monitoring-interface

Then open http://127.0.0.1:5000

## Note

Team project (Telecom Saint-Etienne). Interface component of the agent plus
interface monitoring pair.
