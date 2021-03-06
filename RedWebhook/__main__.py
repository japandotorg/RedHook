""" Entry point to trigger webhook(s) """

import argparse
from RedWebhook import RedWebhook

def main():
    
    parser = argparse.ArgumentParser(
        prog="RedWebhook", description="Trigger discord Webhooks."
    )
    parser.add_argument(
        "-u", "--url", required=True, nargs="+", help="Webhook urls"
    )
    parser.add_argument("-c", "--content", required=True, help="Message content")
    parser.add_argument(
        "--username", default=None, help="override the default username of the webhook"
    )
    parser.add_argument(
        "--avatar_url", default=None, help="override the default avatar of the webhook"
    )
    
    args = parser.parse_args()
    
    webhook = RedWebhook(
        url=args.url,
        content=args.content,
        username=args.username,
        avatar_url=args.avatar_url,
    )
    
    webhook.execute()
    
if __name__ == '__main__':
    main()