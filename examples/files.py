from RedWebhook import RedWebhook

webhook = RedWebhook(
    url='<your_webhook_url_here>',
    username='RedWebhook with files'
)

with open('path/to/first/image.jpg', 'rb') as f:
    webhook.add_file(file=f.read(), filename='image1.jpg')
with open("path/to/second/image.jpg", "rb") as f:
    webhook.add_file(file=f.read(), filename='image2.jpg')
    
response = webhook.execute()