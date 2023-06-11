import discord
from discord import SyncWebhook

from config import settings


WEBHOOK_URL = settings.discord_webhook_url

def send_discord_notification(message):
    webhook = SyncWebhook.from_url(WEBHOOK_URL)
    webhook.send(message)

