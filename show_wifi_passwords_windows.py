import subprocess

result = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifi_entry_table = [line.split(':')[1][1:-1] for line in result if "All User Profile" in line]

for wifi_entry in wifi_entry_table:
    results = subprocess.check_output(['netsh','wlan','show','profile',wifi_entry,'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        print(f'Wireless Network Name: {wifi_entry}, Password: {results[0]}')
    except IndexError:
        print(f'Wireless Network Name: {wifi_entry}, Password Unreadable')
