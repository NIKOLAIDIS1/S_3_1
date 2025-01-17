# Multi-Greenhouse Sensor Data Simulation and Visualization

## Overview
This project simulates a multi-greenhouse environment with three sensors:
1. **Temperature Sensor**
2. **Humidity Sensor**
3. **Light Intensity Sensor**

The data collected from these sensors is stored in an **InfluxDB** database and visualized using **Grafana** dashboards. Each sensor collects data at different intervals and is associated with specific greenhouses and locations.

---

## Project Components

### 1. **InfluxDB Setup**
- Database Name: `KILKIS`
- Connection details:
  - Host: `localhost`
  - Port: `8086`

The InfluxDB database stores sensor data in measurements with associated tags (metadata) and fields (sensor values).

### 2. **Sensor Simulation Script**
The script (`Multi-Greenhouse Sensor Data Simulation.py`) uses Python to simulate sensor readings and write them to the InfluxDB database.

#### Features:
- **Temperature Sensor**: Simulates values between −10°C and 40°C every second.
- **Humidity Sensor**: Simulates values between 40% and 100% every 2 seconds.
- **Light Intensity Sensor**: Simulates values between 500 and 1000 lux every 3 seconds.

#### How It Works:
- The script uses Python’s `threading` module to simulate concurrent sensor operations.
- Each sensor writes data to InfluxDB with specific tags for `greenhouse_id` and `location`.
- Logs each measurement with a timestamp.

### 3. **Grafana Dashboards**
The project includes Grafana dashboards for visualizing the collected data.

#### Key Panels:
- **Temperature Panel**: Displays temperature data over the last 24 hours.
- **Humidity Panel**: Shows humidity levels.
- **Light Intensity Panel**: Illustrates light intensity trends.

Each panel allows time range selection and provides insights into the sensor readings for specific greenhouses and locations.

---

## Setup Instructions

### Step 1: Configure InfluxDB
1. Install InfluxDB on your local machine or server.
2. Create a database named `KILKIS`.
3. Ensure InfluxDB is accessible at `localhost:8086`.

### Step 2: Run the Sensor Simulation Script
1. Install Python dependencies:
   ```bash
   pip install influxdb
   ```
2. Execute the script:
   ```bash
   python Multi-Greenhouse Sensor Data Simulation.py
   ```
3. Verify that data is being written to InfluxDB by checking the logs.

### Step 3: Set Up Grafana
1. Install Grafana.
2. Add InfluxDB as a data source:
   - URL: `http://localhost:8086`
   - Database: `KILKIS`
   - Method: `GET`
3. Create a dashboard with the following panels:
   - **Temperature**: Query `temperature` data grouped by time.
   - **Humidity**: Query `humidity` data grouped by time.
   - **Light Intensity**: Query `light_intensity` data grouped by time.

---

## Example Queries

### Temperature Panel
```sql
SELECT mean("value")
FROM "temperature"
WHERE time > now() - 24h
GROUP BY time(5m)
```

### Humidity Panel
```sql
SELECT mean("value")
FROM "humidity"
WHERE time > now() - 24h
GROUP BY time(5m)
```

### Light Intensity Panel
```sql
SELECT mean("value")
FROM "light_intensity"
WHERE time > now() - 24h
GROUP BY time(5m)
```

---

## Screenshots

1. **Grafana Dashboard**: Displays temperature, humidity, and light intensity.
2. **InfluxDB Connection**: Shows a working connection with the `KILKIS` database.

---

## Notes
- Ensure the InfluxDB and Grafana services are running before starting the simulation script.
- Adjust data collection intervals in the script as needed.
- Customize Grafana dashboards for specific user requirements.

---


