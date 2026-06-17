Enterprise Network Automation Toolkit
A professional-grade Python framework designed for automated network infrastructure management. This project demonstrates the ability to manage device inventories using data-driven principles and perform automated audits across network devices.

Features
Data-Driven Architecture: Uses JSON for inventory management to separate configuration data from logic.

Automated Auditing: Connects to network devices using Netmiko to retrieve hardware/software versions automatically.

Scalable Design: Easily extendable to manage hundreds of devices simultaneously.

Project Structure
inventory.json: Centralized configuration storage for network devices (IPs, Credentials).

01_inventory_manager.py: Utility script to manage and validate device inventory.

02_network_auditor.py: Core automation script that establishes SSH connections and runs audit commands.

.gitignore: Security configuration to prevent sensitive data from being uploaded to GitHub.

Prerequisites
Python 3.x

Netmiko Library: pip install netmiko

Access to Cisco IOS devices (or GNS3 lab environment)

How to Run
Clone the repository.

Install dependencies:

Bash
pip install netmiko
Update inventory.json with your router details.

Run the auditor script:

Bash
python 02_network_auditor.py
