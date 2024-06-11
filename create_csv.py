import csv
import random

# Define the header for the CSV file
header = [
    'Battery_ID', 'Temperature', 'Voltage', 'Current', 'Internal_Resistance',
    'Charge_Time', 'Discharge_Time', 'SOC', 'SOH', 'DOD',
    'Ambient_Humidity', 'RUL'
]

# Function to generate random data for one cycle without 'Cycle' and 'Capacity'
def generate_cycle_data(battery_id, cycle, initial_capacity=2.0, cycles_until_EOL=10000):
    temperature = round(random.uniform(20, 40), 2)  # Random temperature between 20 and 40°C
    voltage = round(random.uniform(3.0, 4.2), 2)  # Random voltage between 3.0 and 4.2V
    current = round(random.uniform(1.0, 2.0), 2)  # Random current between 1.0 and 2.0A
    internal_resistance = round(random.uniform(0.05, 0.15), 3)  # Random internal resistance between 0.05 and 0.15 Ohms
    charge_time = random.randint(50, 70)  # Random charge time between 50 and 70 minutes
    discharge_time = random.randint(110, 130)  # Random discharge time between 110 and 130 minutes
    soc = round(100 - (cycle / cycles_until_EOL) * 100, 2)  # Decreasing SOC
    soh = round(100 - (cycle / cycles_until_EOL) * 100, 2)  # Decreasing SOH
    dod = round((cycle / cycles_until_EOL) * 100, 2)  # Increasing DOD
    ambient_humidity = round(random.uniform(30, 60), 2)  # Random ambient humidity between 30 and 60%
    rul = cycles_until_EOL - cycle  # Remaining Useful Life

    return [
        battery_id, temperature, voltage, current, internal_resistance,
        charge_time, discharge_time, soc, soh, dod,
        ambient_humidity, rul
    ]

# Number of batteries
num_batteries = 10
num_cycles = 1000  # Number of cycles per battery

# Generate data for multiple batteries
data = []
for battery_id in range(1, num_batteries + 1):
    for cycle in range(1, num_cycles + 1):
        data.append(generate_cycle_data(battery_id, cycle))

# Specify the file name
file_name = '/mnt/data/battery_lifecycle_multiple_data.csv'

# Write the data to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(header)
    # Write the data rows
    writer.writerows(data)

file_name
