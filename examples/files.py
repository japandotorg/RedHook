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