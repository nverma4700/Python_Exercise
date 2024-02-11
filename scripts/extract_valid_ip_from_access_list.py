import re
def extract_ip(str):
    pattern = '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
    match = re.findall(pattern, str)
    return match


def validate_ip(ip):
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


str = '''ip access-list 100 10 permit ip host 102.300.1.1 any
ip access-list 100 20 permit ip host 102.100.1.2 any
ip access-list 100 30 permit ip host 102.100.1.3 any'''

ip_list = extract_ip(str)
extracted_ip = []

for ips in ip_list:
    if validate_ip(ips):
        extracted_ip.append(ips)
print(extracted_ip)

