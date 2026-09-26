# Network Monitoring Tool

A simple **Python-based Network Monitoring Tool** that runs in the terminal and allows users to check their computer's network connection, IP address, network interfaces, packet information, network usage, and current network activity.

This project was created as a beginner-friendly Python project to practice functions, loops, conditional statements, dictionaries, lists, user input, file handling, and Python libraries.

## Features

* Connection Status

  * Checks if the computer is connected to the internet
  * Displays the computer name

* IP Address Information

  * Displays the computer name
  * Displays the local IP address
  * Performs a basic DNS connection test

* Ping Test

  * Tests a website or IP address
  * Displays the ping results
  * Shows whether the connection was successful

* Network Interface Information

  * Displays available network interfaces
  * Shows IPv4 addresses
  * Shows IPv6 addresses
  * Shows subnet masks
  * Shows MAC addresses

* Network Speed Activity

  * Measures current upload activity
  * Measures current download activity
  * Displays network activity in KB/s

* Packet Information

  * Displays bytes sent
  * Displays bytes received
  * Displays packets sent
  * Displays packets received
  * Displays network errors
  * Displays dropped packets

* Network Usage

  * Displays total uploaded data
  * Displays total downloaded data
  * Displays total network usage
  * Displays network errors and dropped packets

* Network Logs

  * Creates network connection logs
  * Records connection status
  * Records the date and time
  * Displays previously created logs

* Full Network Report

  * Displays multiple network statistics in one report

* Save Network Report

  * Saves network information to a `.txt` file

## Menu

```text
==========================================
        NETWORK MONITORING TOOL
==========================================
1.  Connection Status
2.  IP Address Information
3.  Ping Test
4.  Network Interface Information
5.  Network Speed Activity
6.  Packet Information
7.  Network Usage
8.  Create Network Log
9.  Show Network Logs
10. Full Network Report
11. Save Network Report
0.  Exit
==========================================
```

## Technologies Used

* Python
* `socket`
* `platform`
* `subprocess`
* `psutil`
* `time`
* `datetime`

## Requirements

Before running the program, make sure you have:

* Python 3.x
* PyCharm, VS Code, or another Python editor
* `psutil` library

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Network-Monitoring-Tool.git
```

### 2. Open the Project

Open the project folder in **PyCharm**, **VS Code**, or your preferred Python editor.

### 3. Install psutil

Open the terminal and run:

```bash
pip install psutil
```

### 4. Run the Program

Run:

```bash
python main.py
```

Or run `main.py` directly from PyCharm.

## Project Structure

```text
Network-Monitoring-Tool/
│
├── main.py
├── network_report.txt
└── README.md
```

The `network_report.txt` file is created automatically when the user selects **Save Network Report**.

## Example

When the program starts, it displays a menu:

```text
==========================================
        NETWORK MONITORING TOOL
==========================================
1.  Connection Status
2.  IP Address Information
3.  Ping Test
4.  Network Interface Information
5.  Network Speed Activity
6.  Packet Information
7.  Network Usage
8.  Create Network Log
9.  Show Network Logs
10. Full Network Report
11. Save Network Report
0.  Exit
==========================================

Enter your choice:
```

### Example Connection Status

```text
---------- CONNECTION STATUS ----------

Internet Status : Connected
Computer Name   : MY-COMPUTER
```

### Example Packet Information

```text
---------- PACKET INFORMATION ----------

Bytes Sent       : 245678
Bytes Received   : 1845678
Packets Sent     : 3521
Packets Received : 4820
Errors Sent      : 0
Errors Received  : 0
Dropped Sent     : 0
Dropped Received : 0
```

### Example Network Log

```text
---------- NETWORK LOG ----------

Network status recorded.
Time   : 2026-09-26 10:30:15
Status : Connected
```

## Learning Objectives

This project helps practice the following Python concepts:

* Functions
* `while` loops
* `for` loops
* `if`, `elif`, and `else`
* Lists
* Dictionaries
* User input using `input()`
* File handling
* Exception handling
* Python modules
* External libraries
* Working with network information
* Basic system monitoring

## Purpose

The purpose of this project is to create a simple command-line tool that allows users to monitor basic network information from their computer.

It is also a learning project for understanding how Python can interact with network information and operating system resources.

## Important Note

The **Network Speed Activity** feature measures the amount of data being transferred during the test. It is not a full internet speed test and does not measure your maximum internet connection speed.

Some network information may also be unavailable depending on the operating system, permissions, or network configuration.

## Future Improvements

Possible features that can be added in future versions:

* Continuous network monitoring
* Automatic connection alerts
* Network usage graphs
* Internet speed testing
* Website availability monitoring
* Port checking
* DNS lookup tool
* Network device discovery
* More detailed network statistics
* Export reports as CSV
* Automatic network reports
* Network history tracking
* Network interface selection
* Connection uptime tracking

## Disclaimer

This project is intended for **educational and personal use**. Network information and available features may vary depending on the computer, operating system, network configuration, and user permissions.

## Author

**Jose Navoa**

Aspiring Information Technology Student

Created as a Python learning project.
