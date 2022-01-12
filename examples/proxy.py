from RedWebhook import RedWebhook

proxies = {
    'http': 'http://11.11.1.11:6969',
    'https': 'https://11.11.1.11:0420'
}

webhook = RedWebhook(
    url='<your_webhook_url_here>',
    content='Webhook',
    proxies=proxies
)

response = webhook.execute()