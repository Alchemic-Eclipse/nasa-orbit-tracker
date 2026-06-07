# ☄️ NASA Orbit Tracker

A terminal-based astrophysics tracking matrix that queries live data streams from NASA's Near-Earth Object (NEO) REST API. 

## 🛠️ Features
* **Live Telemetry Connection:** Establishes direct connection to NASA's automated asteroid tracking systems.
* **Dynamic Date Parsing:** Automatically analyzes local calendar metrics to scan tonight's specific sky coordinates.
* **Kinetic Energy Engine:** Approximates object volume and mass to solve for kinetic impact energy.
* **Tactical Metrics:** Translates raw scientific notation Joules into human readable Hiroshima Atomic Bomb equivalents. (Using Approximations ofcourse)

## 🚀 Installation & Setup
1. **Clone** the repository: ``git clone [https://github.com/Alchemic-Eclipse/nasa-orbit-tracker.git](https://github.com/Alchemic-Eclipse/nasa-orbit-tracker.git)``

2. **Navigate** into the project directory: ``cd nasa-orbit-tracker.``

3. Install **dependencies*:* ``pip install requests.``

4. **Run** the tracking matrix: ``python main.py``

## 🛠️ Built With

* **Python 3** - Primary execution environment.
* **NASA NeoWS API** - Live Near-Earth Object Web Service database.
* **Requests** - For asynchronous HTTP handling and JSON payload extraction.
* **Math & Datetime** - Native calculation libraries for hyper-velocity physics.



