from requests.exceptions import Timeout
from RedWebhook import RedHook, DiscordEmbed

# we will set ridiculously low timeout threshold for testing purposes
webhook = RedHook(
    url='<your_webhook_url_here>',
    timeout=0.2,
)

# you can also set timeout later using
# webhook.timeout = 0.2

embed = DiscordEmbed(
    title='<embed_title>',
    description='<embed_description>',
    color=0x2f3136
)

webhook.add_embed(embed)

# handle timeout exceptions
try:
    response = webhook.execute()
except Timeout as err:
    print(f'Beep Boop, Connection to Discord timed out: \n{err}')