import json
import random
import uuid
from datetime import datetime, timedelta

# --------------------------
# TRUCKS AND DRIVERS
# --------------------------

trucks = [
    {"truck_id": "UP80AB1234", "driver": "Ramesh Yadav"},
    {"truck_id": "UP80CD5678", "driver": "Amit Sharma"},
    {"truck_id": "UP80EF9012", "driver": "Sandeep Singh"},
    {"truck_id": "UP80GH3456", "driver": "Vikram Chauhan"},
    {"truck_id": "UP80IJ7890", "driver": "Rahul Verma"},
    {"truck_id": "UP80KL2468", "driver": "Deepak Kumar"},
    {"truck_id": "UP80MN1357", "driver": "Pankaj Gupta"},
    {"truck_id": "UP80OP9753", "driver": "Anil Mishra"},
    {"truck_id": "UP80QR8642", "driver": "Manoj Tiwari"},
    {"truck_id": "UP80ST1122", "driver": "Arjun Pandey"}
]

# --------------------------
# GPS ROUTES (Uttar Pradesh)
# --------------------------

routes = [
    {"city": "Agra", "lat": 27.1767, "lon": 78.0081},
    {"city": "Etawah", "lat": 26.7767, "lon": 79.0210},
    {"city": "Kanpur", "lat": 26.4499, "lon": 80.3319},
    {"city": "Lucknow", "lat": 26.8467, "lon": 80.9462}
]

# --------------------------
# SETTINGS
# --------------------------

records_per_truck = 5000
start_time = datetime.now()

gps_data = []
sensor_data = []

# --------------------------
# DATA GENERATION
# --------------------------

for truck in trucks:

    fuel_level = random.uniform(200, 300)

    lat = routes[0]["lat"]
    lon = routes[0]["lon"]

    current_time = start_time

    for i in range(records_per_truck):

        # realistic movement
        lat += random.uniform(-0.01, 0.01)
        lon += random.uniform(-0.01, 0.01)

        speed = random.choice([
            random.uniform(0,5),     # idle
            random.uniform(20,40),   # city
            random.uniform(50,80)    # highway
        ])

        # occasional overspeed
        if random.random() < 0.05:
            speed = random.uniform(80,100)

        engine_temp = random.uniform(70,95)

        idle_time = 0
        if speed < 5:
            idle_time = random.uniform(1,5)

        fuel_level -= random.uniform(0.01,0.05)

        timestamp = current_time.isoformat()

        gps_record = {
            "truck_id": truck["truck_id"],
            "driver_name": truck["driver"],
            "event_time": timestamp,
            "latitude": lat,
            "longitude": lon,
            "speed": speed
        }

        sensor_record = {
            "truck_id": truck["truck_id"],
            "event_time": timestamp,
            "fuel_level": round(fuel_level,2),
            "engine_temp": round(engine_temp,2),
            "idle_time": round(idle_time,2)
        }

        gps_data.append(gps_record)
        sensor_data.append(sensor_record)

        current_time += timedelta(seconds=5)

# --------------------------
# SAVE FILES
# --------------------------

with open("gps_data.json", "w") as f:
    for r in gps_data:
        f.write(json.dumps(r) + "\n")

with open("sensor_data.json", "w") as f:
    for r in sensor_data:
        f.write(json.dumps(r) + "\n")

print("Data generation complete")
print("GPS records:", len(gps_data))
print("Sensor records:", len(sensor_data))