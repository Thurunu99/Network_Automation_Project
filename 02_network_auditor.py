from netmiko import ConnectHandler
import json

# Function to load inventory data from the JSON file
def load_inventory(filename):
    with open(filename, 'r') as file:
        return json.load(file)['routers']

# Function to connect to a specific router and run a command
def run_audit(router):
    # Device configuration dictionary for Netmiko
    device = {
        'device_type': 'cisco_ios',
        'host': router['ip'],
        'username': router['username'],
        'password': router['password'],
    }

    try:
        print(f"--- Connecting to {router['name']} ({router['ip']})... ---")
        
        # Establishing SSH connection
        connection = ConnectHandler(**device)
        
        # Sending the command to the router
        print(f"--- Sending command to {router['name']}... ---")
        output = connection.send_command('show version')
        
        # Displaying the output
        print(f"\n--- Output from {router['name']} ---")
        print(output)
        print("------------------------------------------\n")
        
        # Closing the connection
        connection.disconnect()
        
    except Exception as e:
        print(f"Failed to connect to {router['name']}: {e}")

if __name__ == "__main__":
    # Load the router list
    routers = load_inventory('inventory.json')
    
    # Process each router in the list
    for router in routers:
        run_audit(router)