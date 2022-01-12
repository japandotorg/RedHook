# RedHook

[![GitHub license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/japandotorg/RedHook/blob/main/LICENSE)

# Install

Install using pip:

` - ` `pip install RedHook`
` - ` `pip install -U RedHook`
` - ` `python -m pip install -U RedHook`

## Examples

* [Basic Webhook](#basic-webhook)
* [Manage Discord Rate Limit](#manage-discord-rate-limit)
* [Multiple Webhook Urls](#multiple-webhook-urls)
* [Embedded Webhook](#embedded-webhook)
* [Edit Webhook Message](#edit-webhook-messages)
* [Delete Webhook Message](#delete-webhook-messages)
* [Send Files](#send-files)
* [Remove Embeds and Files](#remove-embeds-and-files)
* [Allowed Mentions](#allowed-mentions)
* [Use Proxies](#use-proxies)
* [Timeout](#timeout)

### basic webhook
```py
from RedWebhook import RedHook

webhook = RedHook(url="", content="Webhook Message")
response = webhook.execute()
```

### manage discord rate limit
```py
from RedWebhook import RedHook

webhook = RedHook(
    url='<your_webhook_url_here>',
    rate_limit_retry=True,
    content='Example'
)

response = webhook.execute()
```

### multiple webhook urls
```py
from RedWebhook import RedHook

webhooks = ['<webhook_url_1>', '<webhook_url_2>']

webhook = RedHook(
    url=webhooks,
    content='Webhook'
)

response = webhook.execute()
```

### embedded webhook
```py
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
```

By default, the embed fields are placed side by side. We can arrange them in a new line by setting `inline=False` as follows:
```py
from RedWebhook import RedHook, DiscordEmbed

webhook = RedHook(url='<your_webhook_url_here>')

embed = DiscordEmbed(
    title='<your_title>',
    description='<your_description>',
    color='<your_color>'
)
embed.set_footer(
    text='<your_footer>'
)
embed.set_timestamp()
# set `inline=False` for the embed field to come in the whole line
embed.add_embed_field(
    name='<field_1>',
    value='<field_description>',
    inline=False
)
embed.add_embed_field(
    name='<field_2>',
    value='<field_description>',
    inline=False
)
embed.add_embed_field(
    name='<field_3>',
    value='<field_description>'
)
embed.add_embed_field(
    name='<field_3>',
    value='<field_description>'
)
```

### edit webhook message
```py
from RedWebhook import RedHook
from time import sleep

webhook = RedHook(
    url='<your_webhook_url_here>',
    content='Before edit'
)

sent_webhook = webhook.execute()

webhook.content = 'After edit'

sleep(10)

sent_webhook = webhook.edit(sent_webhook)
```

### delete webhook messages
```py
from RedWebhook import RedHook
from time import sleep

webhook = RedHook(
    url='<your_webhook_url_here>',
    content='Before edit'
)

sent_webhook = webhook.execute()

sleep(10)

webhook.delete(sent_webhook)
```

### send files
```py
from RedWebhook import RedHook

webhook = RedHook(
    url='<your_webhook_url_here>',
    username='RedHook with files'
)

with open('path/to/first/image.jpg', 'rb') as f:
    webhook.add_file(file=f.read(), filename='image1.jpg')
with open("path/to/second/image.jpg", "rb") as f:
    webhook.add_file(file=f.read(), filename='image2.jpg')
    
response = webhook.execute()
```

You can also upload embedded attachments:
```py
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
```

### remove embeds and files
```py
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

response = webhook.execute(remove_embeds=True, remove_files=True)
# webhook.files and webhook.embeds will be empty after webhook is executed
# You could also manually call the functions webhook.remove_files() and webhook.remove_embeds()
```

`.remove_file()` removes the given file:
```py
from RedWebhook import RedHook

webhook = RedHook(
    url='<your_webhook_url_here>',
    username='Webhook files'
)

# send two images
with open('path/to/first/image.jpg', 'rb') as f:
    webhook.add_file(file=f.read(), filename='image1.jpg')
with open("path/to/second/image.jpg", "rb") as f:
    webhook.add_file(file=f.read(), filename='image2.jpg')

# remove 'image1.jpg'
webhook.remove_file('image1.jpg')

# only 'image2.jpg' is sent to the webhook
response = webhook.execute()
```

### allowed mentions

Look into the [Discord Documentation](https://discord.com/developers/docs/resources/channel#allowed-mentions-object) for examples and explanation

This example will only ping `user_id_1` and `user_id_2`, no one else
```py
from RedWebhook import RedHook

content = '@everyone say hello to our friends <@user_id_1> and <@user_id_2>'

allowed_mentions = {
    'users': ['user_id_1', 'user_id_2]
}

webhook = RedHook(
    url='<your_webhook_url_here>',
    content=content,
    allowed_mentions=allowed_mentions
)

response = webhook.execute()
```

### use proxies
```py
from RedWebhook import RedHook

proxies = {
    'http': 'http://11.11.1.11:6969',
    'https': 'https://11.11.1.11:0420'
}

webhook = RedHook(
    url='<your_webhook_url_here>',
    content='Webhook',
    proxies=proxies
)

response = webhook.execute()
```
or
```py
from RedWebhook import RedHook

proxies = {
    'http': 'http://11.11.1.11:6969',
    'https': 'https://11.11.1.11:0420'
}

webhook = RedHook(
    url='<your_webhook_url_here>',
    content='Webhook'
)

webhook.set_proxies(proxies)

response = webhook.execute()
```

### use cli
```bash
usage: RedHook [-h] -u URL [URL ...] -c CONTENT [--username USERNAME] [--avatar_url AVATAR_URL]

Trigger Red Webhooks

optional arguments:
    -h, --help                                  show this help message and exit
    -u URL [URL ...], --url URL [URL ...]       webhook url/urls
    -c CONTENT, --content CONTENT               message content
    --username USERNAME                         override the default username of the webhook
    --avatar_url AVATAR_URL                     override the default avatar of the webhook
```

### timeout
```py
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
```