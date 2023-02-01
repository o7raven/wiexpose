import subprocess

data = subprocess.run('netsh wlan show profiles', shell=True, capture_output = True).stdout.decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for profile in profiles:
    profileInfo = subprocess.run(f'netsh wlan show profile {profile} key=clear', shell=True, capture_output=True).stdout.decode('utf-8').split('\n')
    pwd = [i.split(':')[1][1:-1] for i in profileInfo if "Key Content" in i]


    try:
        print (f"{profile} -> {pwd[0]}")
    except IndexError:
        print (f"{profile}|  ' ' ")