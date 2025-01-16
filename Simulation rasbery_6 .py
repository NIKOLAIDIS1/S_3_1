import random
import time
import threading
from influxdb import InfluxDBClient
from datetime import datetime  # Import datetime for timestamps

# InfluxDB Configuration
#INFLUXDB_ADDRESS and INFLUXDB_PORT: Specify the address (localhost) and port (8086)
#  of the InfluxDB server.
#INFLUXDB_DATABASE: Specifies the database name (KILKIS)

INFLUXDB_ADDRESS = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_DATABASE = 'KILKIS'
#Connects to the InfluxDB server.
#Creates the specified database if it does not already exist.
#Switches the client to the active database.
def setup_influxdb():
    """Setup the InfluxDB client."""
    client = InfluxDBClient(host=INFLUXDB_ADDRESS, port=INFLUXDB_PORT)
    client.create_database(INFLUXDB_DATABASE)  # Ensure database exists
    client.switch_database(INFLUXDB_DATABASE)
    return client

#---------------------------------------------------------------------------

#Writes a single measurement to InfluxDB with the following structure:

#   Measurement: Type of data being recorded (e.g., temperature, humidity, or light intensity).
#  Tags: Metadata associated with the measurement (e.g., greenhouse_id).
#  Fields: Contains the actual sensor data (value).
#Logs the written data to the console.

def write_to_influxdb(client, measurement, value, tags):
    """Write a single measurement to InfluxDB."""
    json_body = [
        {
            "measurement": measurement,
            "tags": tags,
            "fields": {
                "value": value
            }
        }
    ]
    client.write_points(json_body)
    # Include the current timestamp in the print output
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Measurement: {measurement}, Value: {value:.2f}, Tags: {tags}")
    print("------------------------------------")


#------------------------------------------------------------------------
#Each sensor runs in a loop, generating random 
#data at fixed intervals and writing it to InfluxDB:
#--------------------------------------------------------------
#Simulates temperatures between -10°C and 40°C.
#Writes data every 1 second with greenhouse_id set to "λαχανα".

def temperature_sensor(client):
    """Simulate temperature sensor data."""
    while True:
        temperature = random.uniform(-10, 40.0)  # Random temperature (-10 to 40°C)
        write_to_influxdb(client, "temperature", temperature, {"zarzabati_id": "λαχανα", "xorafi": "tyrnabos "})
        time.sleep(1)  # Collect data every 1 second

def humidity_sensor(client):
    """Simulate humidity sensor data."""
    while True:
        humidity = random.uniform(40, 100.0)  # Random humidity (30-90%)
        write_to_influxdb(client, "humidity", humidity, {"zarzabati_id": "μαρουλια","xorafi": "Agia" })
        time.sleep(2)  # Collect data every 2 seconds

def light_intensity_sensor(client):
    """Simulate light intensity sensor data."""
    while True:
        light_intensity = random.randint(500, 1000)  # Random light intensity (200-1000 lux)
        write_to_influxdb(client, "light_intensity", light_intensity, {"zarzabati_id": "ντοματες","xorafi": "belika"})
        time.sleep(3)  # Collect data every 3 seconds

#--------------------------------------------------------------
#Main Function (main):
#Sets up the InfluxDB client.
#Starts all sensor threads.
#Joins the threads to keep the main process 
#alive until all threads are completed (infinite loops in this case).

def main():
    client = setup_influxdb()
    print("Starting Multi-Greenhouse Simulation with Threads...")

    # Create threads for each sensor
    #Each sensor runs in its own thread to simulate concurrent data collection.
#Threads:

    #temperature_thread
    #humidity_thread
    #light_intensity_thread
    temperature_thread = threading.Thread(target=temperature_sensor, args=(client,))
    humidity_thread = threading.Thread(target=humidity_sensor, args=(client,))
    light_intensity_thread = threading.Thread(target=light_intensity_sensor, args=(client,))

    # Start the threads
    temperature_thread.start()
    humidity_thread.start()
    light_intensity_thread.start()

    # Keep the main thread alive
    temperature_thread.join()
    humidity_thread.join()
    light_intensity_thread.join()
#main() function runs only when the script is executed directly, 
# not when it's imported as a module in another script.
if __name__ == "__main__":
    main()
