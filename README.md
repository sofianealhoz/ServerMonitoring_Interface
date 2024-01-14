# Interface

## Introduction

Welcome to the documentation of our surveillance application's interface. This interface allows you to visualize and interact with the data collected by the Agent. This document provides comprehensive information to understand, install, and use the interface.

## Features

The interface offers a complete set of features to facilitate the management and visualization of surveillance data. The main features include:

- Intuitive navigation through dashboards.
- Dynamic addition and removal of servers.
- Integrated view of the health of monitored servers.
- Historical graphs for key metrics (CPU, RAM, etc.).

## Architecture

The interface architecture is designed to ensure a smooth user experience. It interacts with the Agent through an API to retrieve and display surveillance data. The modular structure allows easy extensibility for adding new features and accessing other servers.

## Installation

To install the interface on your computer, follow these steps:

1. Connect to the Telecom Saint-Etienne school's Docker: `docker login devops.telecomste.fr:5050`
2. Retrieve the Docker image: `docker pull devops.telecomste.fr:5050/printerfaceadmin/2023-24/group1/interface/mon_app:main`
3. Launch the container for this image: `docker run -d devops.telecomste.fr:5050/printerfaceadmin/2023-24/group1/interface/mon_app:main`
4. Access the website via the following IP address: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage

Once installed, the interface can be used by following these guidelines:

- Access the specific URL where the interface is deployed.
- Use the built-in features to explore different dashboards.
- Add servers as needed.

Adding a server is done via the complete server URL, in the form: "http://user.domain_name:PORT/"

## Configuration

The interface configuration can be adjusted by modifying the appropriate settings. These settings may include elements such as display preferences, etc. Refer to the detailed documentation for instructions on configuration.

## Missing Features

The features for retrieving logs, the number of 404 errors, and the last 5 error messages do not work. However, if you go to [http://127.0.0.1:5000/server/server_id/graph/dataLogs](http://127.0.0.1:5000/server/server_id/graph/dataLogs), you will be able to see the data that is supposed to be used for retrieving logs and the number of 404 errors.

## Contribute

If you want to contribute to the development of the interface, follow these steps:

1. Clone the repository on your machine.
2. Explore the source code and identify areas where you want to contribute.
3. Follow the specific instructions in the "Contribute" section of the Agent's README to submit changes.

## License

This project is released under the Apache License 2.0

---
