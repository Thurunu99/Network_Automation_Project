import json

def load_inventory(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data['routers']

if __name__ == "__main__":
    # Loading the inventory data from the JSON file
    routers = load_inventory('inventory.json')
    
    print(f"--- Successfully loaded {len(routers)} devices ---")
    
    # Printing the device details
    for r in routers:
        print(f"Device Name: {r['name']} | IP Address: {r['ip']}")
        
    print("--------------------------------------------------")