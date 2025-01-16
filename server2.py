from influxdb import InfluxDBClient

# InfluxDB Configuration
INFLUXDB_ADDRESS = "localhost"
INFLUXDB_PORT = 8086
INFLUXDB_DATABASE = "KILKIS"

def fetch_data():
    # Connect to the InfluxDB server
    client = InfluxDBClient(host=INFLUXDB_ADDRESS, port=INFLUXDB_PORT)
    client.switch_database(INFLUXDB_DATABASE)

    # Query for the latest temperature, humidity, and light intensity
    query = """
    SELECT * FROM temperature WHERE time > now() - 1h;
    """
    result = client.query(query)

    # Process and display the results
    print("Collected Sensor Data:")
    for point in result.get_points():
        print(f"Time: {point['time']}, Measurement: temperature, Value: {point['value']}")

    client.close()

if __name__ == "__main__":
    print("Starting InfluxDB Data Collection...")
    fetch_data()
