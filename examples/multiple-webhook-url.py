from RedWebhook import RedWebhook

webhooks = ['<webhook_url_1>', '<webhook_url_2>']

webhook = RedWebhook(
    url=webhooks,
    content='Webhook'
)

response = webhook.execute()