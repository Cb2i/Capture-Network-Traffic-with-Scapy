# Network Traffic Capture with Scapy

<img src="https://www.kali.org/tools/scapy/images/scapy-logo.svg" width="48">

A Python-based network sniffer that captures and analyzes network packets in real-time using Scapy.

---

## 📖 Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Description
This project is a simple network sniffer built using Python and Scapy. It captures network packets, analyzes them, and displays key information such as source/destination IPs, ports, and protocols. It's a great tool for learning about network traffic and cybersecurity.

---

## ✨ Features
- Real-time packet capture.
- Supports TCP, UDP, and ICMP protocols.
- Displays packet summaries (source IP, destination IP, ports, flags).
- Optional: Save captured packets to a `.pcap` file for further analysis.

---

## 🛠️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Network-Traffic-Capture.git
---

  ## Install the required dependencies : 
1.  Install the required dependencies:
   ```bash
   pip install -r requirements.txt
```
---
## 🚦 Usage
Run the script to start capturing packets:
 ```bash
python network_sniffer.py
```
Optional Arguments
 - count: Number of packets to capture (default: 10).

 - filter: Apply a BPF filter (e.g., tcp, udp).

 - output: Save captured packets to a .pcap file.

- Example : 
python network_sniffer.py --count 20 --filter "tcp" --output captured_packets.pcap
