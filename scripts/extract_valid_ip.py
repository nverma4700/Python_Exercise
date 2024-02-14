import re


def extract_ip(str):
    '''
    Extract the IP, use regex pattern to match the IP address and 
    find all the IP addresses in the given string
    '''
    pattern = '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
    match = re.findall(pattern, str)
    return match


def validate_ip(ip):
    '''
    Validate if the given IP is valid or not and return True or False:
    Condition: 
    0 > 1st octet >= 255
    0 >= 2nd octet >= 255
    '''
    invalid_octet = []
    ip_octet = ip.split('.')
    if int(ip_octet[0]) > 0 and int(ip_octet[0]) <= 255:
        for octet in ip_octet[1:]:
            if int(octet) < 0 or int(octet) > 255:
                invalid_octet.append(octet)
    else:
        invalid_octet.append(ip_octet[0])
    if invalid_octet:
        valid_ip = False
    else:
        valid_ip = True
    return valid_ip


def valid_ips(str):
    '''
    Extract and validate the IP in the list using the fucntions defined
    and return the list of all the valid IPs
    '''
    ip_list = extract_ip(str)
    extracted_ip = []
    for ips in ip_list:
        if validate_ip(ip=ips):
            extracted_ip.append(ips)
    return extracted_ip

    
# Testing:
# str = '''ip access-list 100 10 permit ip host 102.300.1.1 any
# ip access-list 100 20 permit ip host 102.100.1.2 any
# ip access-list 100 30 permit ip host 102.100.1.3 any'''

# print(valid_ips(str))




