from RedWebhook import RedHook, DiscordEmbed

webhook = RedHook(url='<your_webhook_url_here>')

# create embed objects for webhook
embed = DiscordEmbed(
    title='<your_title>',
    description='<your_description>',
    color='<your_color>'
)

# set author
embed.set_author(
    name='<author>',
    url='<author_url>',
    icon_url='<author_icon_url>'
)

# set image
embed.set_image(
    url='<your_image_url>',
)

# set thumbnail
embed.set_thumbnail(
    url='<your_thumbnail_url>',
)

# set footer
embed.set_thumbnail(
    text='<your_footer>'
)

# set timestamp (default is now)
embed.set_timestamp()

# add fields to the embed
embed.add_embed_field(
    name='<field_1>',
    value='<field_description>'
)
embed.add_embed_field(
    name='<field_2>',
    value='<field_description>'
)

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()