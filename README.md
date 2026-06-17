# Enterprise Network Automation Toolkit
A Python framework for managing network infrastructure using data-driven principles.

## Structure
- inventory.json: Configuration data.
- 01_inventory_manager.py: Python script to load and manage network device inventory.

# Enterprise Network Automation Toolkit

A Python framework for managing network infrastructure using data-driven principles.

## Structure
- inventory.json: Configuration data for network devices (Separation of concerns).
- 01_inventory_manager.py: Python script to load and manage network device inventory.
- 02_network_auditor.py: Script to connect to routers and perform automated audits.

## How to Run
1. Ensure Python is installed.
2. Install dependencies:
   pip install netmiko
3. Run the auditor:
   python 02_network_auditor.py