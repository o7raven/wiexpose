import subprocess

data = subprocess.run('netsh wlan show profile', shell=True, capture_output = True).stdout.decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.run(f'netsh wlan show profile {i} key=clear', shell=True, capture_output=True).stdout.decode('utf-8').split('\n')
    results = [b.split(':')[1][1:-1] for b in results if "Key Content" in b]


    try:
        print (f"{i}| {results[0]}")
    except IndexError:
        print (f"{i}|  ' ' ")