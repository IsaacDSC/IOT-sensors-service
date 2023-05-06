from watchdog.discord.discord_bot import DiscordAlert


def test_send_alert_to_discord():
    alert = DiscordAlert()
    sended = alert.send_alert("Testing alert")
    assert sended == True