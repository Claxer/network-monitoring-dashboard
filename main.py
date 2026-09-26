import socket
import platform
import subprocess
import psutil
import time
from datetime import datetime


# ==========================================
# 1. CONNECTION STATUS
# ==========================================

def connection_status():
    print("\n---------- CONNECTION STATUS ----------")

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet Status : Connected")
    except OSError:
        print("Internet Status : Not Connected")

    print("Computer Name   :", socket.gethostname())


# ==========================================
# 2. IP ADDRESS INFORMATION
# ==========================================

def ip_information():
    print("\n---------- IP ADDRESS INFORMATION ----------")

    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.error:
        local_ip = "Unavailable"

    print("Computer Name :", hostname)
    print("Local IP     :", local_ip)

    try:
        public_ip = socket.gethostbyname("google.com")
        print("DNS Test     : Successful")
        print("Google DNS   :", public_ip)
    except socket.error:
        print("DNS Test     : Failed")


# ==========================================
# 3. PING TEST
# ==========================================

def ping_test():
    print("\n---------- PING TEST ----------")

    host = input("Enter website or IP address: ")

    print("\nTesting connection to", host)

    try:
        start_time = time.time()

        result = subprocess.run(
            ["ping", "-n", "4", host],
            capture_output=True,
            text=True
        )

        end_time = time.time()

        print("\n" + result.stdout)

        if result.returncode == 0:
            total_time = (end_time - start_time) * 1000
            print("Ping Test : Successful")
            print("Test Time :", round(total_time, 2), "ms")
        else:
            print("Ping Test : Failed")

    except Exception as error:
        print("Unable to perform ping test.")
        print("Error:", error)


# ==========================================
# 4. NETWORK INTERFACE INFORMATION
# ==========================================

def network_interfaces():
    print("\n---------- NETWORK INTERFACES ----------")

    interfaces = psutil.net_if_addrs()

    if not interfaces:
        print("No network interfaces found.")
        return

    for interface, addresses in interfaces.items():
        print("\nInterface:", interface)

        for address in addresses:
            if address.family == socket.AF_INET:
                print("IPv4 Address :", address.address)
                print("Subnet Mask  :", address.netmask)

            elif address.family == socket.AF_INET6:
                print("IPv6 Address :", address.address)

            elif address.family == psutil.AF_LINK:
                print("MAC Address  :", address.address)


# ==========================================
# 5. NETWORK SPEED
# ==========================================

def network_speed():
    print("\n---------- NETWORK SPEED ----------")

    print("Measuring network activity...")
    print("Please wait 3 seconds...")

    start = psutil.net_io_counters()

    start_sent = start.bytes_sent
    start_received = start.bytes_recv

    time.sleep(3)

    end = psutil.net_io_counters()

    end_sent = end.bytes_sent
    end_received = end.bytes_recv

    sent_bytes = end_sent - start_sent
    received_bytes = end_received - start_received

    sent_kb = sent_bytes / 1024
    received_kb = received_bytes / 1024

    sent_kbps = sent_kb / 3
    received_kbps = received_kb / 3

    print("\nUpload Activity   :", round(sent_kbps, 2), "KB/s")
    print("Download Activity :", round(received_kbps, 2), "KB/s")

    print("\nNote: This shows current network activity,")
    print("not your maximum internet speed.")


# ==========================================
# 6. PACKET INFORMATION
# ==========================================

def packet_information():
    print("\n---------- PACKET INFORMATION ----------")

    stats = psutil.net_io_counters()

    print("Bytes Sent       :", stats.bytes_sent)
    print("Bytes Received   :", stats.bytes_recv)
    print("Packets Sent     :", stats.packets_sent)
    print("Packets Received :", stats.packets_recv)
    print("Errors Sent      :", stats.errout)
    print("Errors Received  :", stats.errin)
    print("Dropped Sent     :", stats.dropout)
    print("Dropped Received :", stats.dropin)


# ==========================================
# 7. NETWORK USAGE
# ==========================================

def network_usage():
    print("\n---------- NETWORK USAGE ----------")

    stats = psutil.net_io_counters()

    sent_mb = stats.bytes_sent / (1024 ** 2)
    received_mb = stats.bytes_recv / (1024 ** 2)

    total_mb = sent_mb + received_mb

    print("Data Sent     :", round(sent_mb, 2), "MB")
    print("Data Received :", round(received_mb, 2), "MB")
    print("Total Usage   :", round(total_mb, 2), "MB")

    print("\nNetwork Errors")
    print("Sent Errors     :", stats.errout)
    print("Received Errors :", stats.errin)

    print("\nNetwork Drops")
    print("Sent Drops      :", stats.dropout)
    print("Received Drops  :", stats.dropin)


# ==========================================
# 8. NETWORK LOG
# ==========================================

network_logs = []


def create_network_log():
    print("\n---------- NETWORK LOG ----------")

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)

        status = "Connected"

    except OSError:
        status = "Disconnected"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = {
        "time": current_time,
        "status": status
    }

    network_logs.append(log)

    print("Network status recorded.")
    print("Time   :", current_time)
    print("Status :", status)


def show_network_logs():
    print("\n---------- NETWORK LOGS ----------")

    if not network_logs:
        print("No network logs available.")
        print("Use the network monitoring option to create a log.")
        return

    for log in network_logs:
        print("\nTime   :", log["time"])
        print("Status :", log["status"])


# ==========================================
# 9. FULL NETWORK REPORT
# ==========================================

def full_network_report():
    print("\n==========================================")
    print("          FULL NETWORK REPORT")
    print("==========================================")

    connection_status()
    ip_information()
    network_interfaces()
    packet_information()
    network_usage()

    print("\n==========================================")
    print("          REPORT COMPLETE")
    print("==========================================")


# ==========================================
# 10. SAVE NETWORK REPORT
# ==========================================

def save_network_report():
    print("\n---------- SAVE NETWORK REPORT ----------")

    filename = "network_report.txt"

    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.error:
        local_ip = "Unavailable"

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        connection = "Connected"
    except OSError:
        connection = "Disconnected"

    stats = psutil.net_io_counters()

    report = []

    report.append("==========================================")
    report.append("           NETWORK MONITORING REPORT")
    report.append("==========================================")
    report.append("")
    report.append("Computer Name : " + hostname)
    report.append("Local IP      : " + local_ip)
    report.append("Connection    : " + connection)
    report.append("")
    report.append("Network Statistics")
    report.append("------------------")
    report.append("Bytes Sent       : " + str(stats.bytes_sent))
    report.append("Bytes Received   : " + str(stats.bytes_recv))
    report.append("Packets Sent     : " + str(stats.packets_sent))
    report.append("Packets Received : " + str(stats.packets_recv))
    report.append("Errors Sent      : " + str(stats.errout))
    report.append("Errors Received  : " + str(stats.errin))
    report.append("Dropped Sent     : " + str(stats.dropout))
    report.append("Dropped Received : " + str(stats.dropin))
    report.append("")
    report.append(
        "Report Created  : " +
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    report.append("==========================================")

    with open(filename, "w") as file:
        for line in report:
            file.write(line + "\n")

    print("Network report saved as:", filename)


# ==========================================
# MENU
# ==========================================

def show_menu():
    print("\n==========================================")
    print("        NETWORK MONITORING TOOL")
    print("==========================================")
    print("1.  Connection Status")
    print("2.  IP Address Information")
    print("3.  Ping Test")
    print("4.  Network Interface Information")
    print("5.  Network Speed Activity")
    print("6.  Packet Information")
    print("7.  Network Usage")
    print("8.  Create Network Log")
    print("9.  Show Network Logs")
    print("10. Full Network Report")
    print("11. Save Network Report")
    print("0.  Exit")
    print("==========================================")


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            connection_status()

        elif choice == "2":
            ip_information()

        elif choice == "3":
            ping_test()

        elif choice == "4":
            network_interfaces()

        elif choice == "5":
            network_speed()

        elif choice == "6":
            packet_information()

        elif choice == "7":
            network_usage()

        elif choice == "8":
            create_network_log()

        elif choice == "9":
            show_network_logs()

        elif choice == "10":
            full_network_report()

        elif choice == "11":
            save_network_report()

        elif choice == "0":
            print("\nThank you for using Network Monitoring Tool!")
            break

        else:
            print("\nInvalid choice.")
            print("Please enter a number from 0 to 11.")


main()
