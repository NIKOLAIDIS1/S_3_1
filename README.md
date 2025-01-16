# Greenhouse Monitoring System

## Overview
This project simulates and monitors environmental conditions (temperature, humidity, and light intensity) in multiple greenhouses using Raspberry Pi, InfluxDB, and Grafana. The system:

1. Simulates real-time sensor data for temperature, humidity, and light intensity.
2. Stores the data in an InfluxDB time-series database.
3. Visualizes the collected data using a Grafana dashboard.

---

## Features
- **Sensor Simulation:** Simulates data collection from three sensors:
  - Temperature sensor (1-second intervals).
  - Humidity sensor (2-second intervals).
  - Light intensity sensor (3-second intervals).
- **Data Storage:** Efficiently stores sensor readings in an InfluxDB database.
- **Real-time Visualization:** Displays data using a Grafana dashboard, including detailed trends for the past 24 hours.

---

## Project Structure
1. **Simulation Script** (`Multi-Greenhouse Sensor Data Simulation.py`):
   - Simulates sensor data for multiple greenhouses.
   - Writes data to InfluxDB with appropriate tags and fields.

2. **Data Retrieval Script** (`Real-Time Sensor Data Collection with InfluxDB.py`):
   - Fetches sensor data from InfluxDB for analysis or display.
   - Demonstrates querying and processing the last hour’s temperature data.

3. **Grafana Dashboard Configuration** (`Greenhouse GRAFANA Monitoring Dashboard.json`):
   - Configures a Grafana dashboard for real-time visualization of sensor data.
   - Includes panels for temperature, humidity, and light intensity.

4. **Example Output** (`simulation output.png`):
   - Displays a snapshot of the simulation’s console logs or dashboard views.

---

## Installation & Setup
### Prerequisites
- **InfluxDB**:
  - Install and start an InfluxDB server (v1.0+).
- **Grafana**:
  - Install Grafana (v11.4.0 or compatible).
  - Import the provided Grafana dashboard JSON file.
- **Python Requirements**:
  - Install required Python libraries:
    ```bash
    pip install influxdb
    ```

### Steps
1. **Setup InfluxDB Database**:
   - Ensure InfluxDB is running on `localhost:8086`.
   - Create a database named `KILKIS`.

2. **Run the Simulation**:
   - Execute `Multi-Greenhouse Sensor Data Simulation.py` to start collecting and storing sensor data in InfluxDB.

3. **Query Data**:
   - Use `Real-Time Sensor Data Collection with InfluxDB.py` to fetch and display stored sensor data.

4. **Visualize Data**:
   - Import the `Greenhouse GRAFANA Monitoring Dashboard.json` file into Grafana.
   - Ensure the Grafana data source points to the `KILKIS` database in InfluxDB.

---

## How It Works
1. **Sensor Simulation**:
   - Each sensor operates in its thread, continuously generating and writing random data to InfluxDB.
   - Example measurement structure:
     ```json
     {
       "measurement": "temperature",
       "tags": {
         "zarzabati_id": "λαχανα",
         "xorafi": "tyrnabos"
       },
       "fields": {
         "value": 22.84
       }
     }
     ```

2. **Data Storage**:
   - Data is stored in InfluxDB with timestamps and metadata tags for easy querying.

3. **Visualization**:
   - Grafana visualizes the data using time-series panels.
   - Panels are configured for trends over time with thresholds for alerts.

---

## Example Output
Sample Console Log:
```
[2025-01-16 12:27:22] Measurement: temperature, Value: 22.84, Tags: {"zarzabati_id": "λαχανα", "xorafi": "tyrnabos"}
[2025-01-16 12:27:24] Measurement: humidity, Value: 75.86, Tags: {"zarzabati_id": "μαρουλια", "xorafi": "Agia"}
[2025-01-16 12:27:25] Measurement: light_intensity, Value: 753, Tags: {"zarzabati_id": "ντοματες", "xorafi": "

