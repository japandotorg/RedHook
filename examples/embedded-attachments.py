from RedWebhook import RedHook, DiscordEmbed

webhook = RedHook(
    url='<your_webhook_url_here>'
)

with open('path/to/image.jpg', 'rb') as f:
    webhook.add_file(file=f.read(), filename='attach.jpg')
    
embed = DiscordEmbed(
    title='<your_embed_title>',
    description='<your_embed_description>',
    color=0x2f3136
)

embed.set_thumbnail(url='attachment://attach.jpg')

webhook.add_embed(embed)

response = webhook.execute()