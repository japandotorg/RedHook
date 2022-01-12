from RedWebhook import RedHook

webhooks = ['<webhook_url_1>', '<webhook_url_2>']

webhook = RedHook(
    url=webhooks,
    content='Webhook'
)

response = webhook.execute()