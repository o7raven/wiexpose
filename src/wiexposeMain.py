import subprocess
from prettytable import PrettyTable
showProfiles = subprocess.run('netsh wlan show profiles', shell=True, capture_output = True).stdout.decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in showProfiles if "All User Profile" in i]

cmdTable = PrettyTable([f'SSID name', 'Authentication', 'Password'])
for profile in profiles:
    profileInfo = subprocess.run(f'netsh wlan show profile {profile} key=clear', shell=True, capture_output=True).stdout.decode('utf-8').split('\n')
  
    pwd = [i.split(':')[1][1:-1] for i in profileInfo if "Key Content" in i]
    authType = [i.split(':')[1][1:-1] for i in profileInfo if "Authentication" in i]
    cmdTable.add_row([profile, authType[0], pwd[0]])

print(cmdTable)
input("\nPress enter to exit\n")
