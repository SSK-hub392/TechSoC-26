storage_capacity = int(input("Enter maximum storage capacity: "))
no_of_containers = int(input("Enter number of containers: "))
print()

i= 1
total_weight = 0
weights= []

while i <= no_of_containers:
     weight = float(input(f"Enter weight of container {i}: "))
     i += 1
     total_weight += weight 
     weights.append(weight)

avg_weight = total_weight/ no_of_containers

heaviest = max(weights)
lightest = min(weights)

def classification():
    if total_weight >= 200:
        return "Heavy"
    else:
        return "Light"

def status():
    if total_weight <= storage_capacity:
        return "Shipment can be unloaded"
    else:
        return "Shipment exceeds port capacity"
           

#output
print(f"\nTotal Shipment Weight: {total_weight}")
print(f"Average Container Weight: {avg_weight}")
print(f"Heaviest Container: {heaviest}")
print(f"Lightest Container: {lightest}")
print(f"Classification: {classification()}")
print(f"Port Capacity: {storage_capacity}")
print(f"Status: {status()}")



