import os
import platform

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    """
    param = 'n' if platform.system().lower() == 'windows' else "-c"
    command = ["ping", param, "1", host]
    # join the string and creates a command. Out the command response
    command_response = os.system(' '.join(command))
    # For successful ping it will return 0 for unsuccessful will return random number
    return command_response == 0 # Bool logic to check if the response is 0 or not.


def ping_ip_addresses(ip_list):
    status = {}
    for ip in ip_list:
        if ping(ip):
            status[ip] = 'reachable'
        else:
            status[ip] = 'unreachable'
    return status

if __name__ == "__main__":
    ip_addresses = [
        "8.8.8.8",  # Google DNS
        "192.168.1.1",  # Router IP
        "127.0.0.1",  # Localhost
        "10.255.255.1"  # Non-existent IP
    ]
    result = ping_ip_addresses(ip_list=ip_addresses)
    for ip, status in result.items():
        print(f"{ip}:{status}")