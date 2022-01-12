from RedWebhook import RedHook

webhook = RedHook(
    url='<your_webhook_url_here>',
    rate_limit_retry=True,
    content='Example'
)

response = webhook.execute()