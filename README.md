# 🚀 Enterprise Network Automation Toolkit

A professional-grade Python framework designed for automated network infrastructure management. This project bridges the gap between manual network administration and modern automated infrastructure governance.

## 🌟 Key Features
*   **Data-Driven Architecture**: Decouples configuration data from core logic using JSON-based inventory management.
*   **Automated Auditing**: Utilizes the `Netmiko` library to establish secure SSH connections and retrieve real-time hardware/software status across network devices.
*   **Scalable Design**: Easily extendable to manage complex multi-vendor network environments.

## 📂 Project Structure
*   `inventory.json`: Centralized configuration storage for network devices (IP addresses, credentials).
*   `01_inventory_manager.py`: Utility script for loading and validating device inventory.
*   `02_network_auditor.py`: Core automation script for executing audit commands and retrieving device data.
*   `README.md`: Project documentation and configuration guide.
*   `.gitignore`: Prevents sensitive credentials from being uploaded to the repository.

## 🛠 Prerequisites
*   **Python 3.x**
*   **Netmiko Library**: Install via pip:
```bash
    pip install netmiko
    ```
*   **Network Lab Environment**: Access to Cisco IOS devices (GNS3, Cisco Modeling Labs, or physical lab).

## 🚀 Getting Started
1. **Clone the repository**:
```bash
   git clone <your-repository-url>
