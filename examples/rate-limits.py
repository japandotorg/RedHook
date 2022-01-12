from RedWebhook import RedWebhook

webhook = RedWebhook(
    url='<your_webhook_url_here>',
    rate_limit_retry=True,
    content='Example'
)

response = webhook.execute()