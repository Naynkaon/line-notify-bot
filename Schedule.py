from apscheduler.schedulers.background import BackgroundScheduler
from linebot.models import TextSendMessage

from text_dectetion import replace_format

scheduler = BackgroundScheduler()
scheduler.start()


def send_reminder(line_bot_api, user_id, message):
    line_bot_api.push_message(user_id, TextSendMessage(text=message))


def set_schedule(line_bot_api, user_id, time_text):
    run_time = replace_format(time_text)

    if run_time is None:
        return False

    scheduler.add_job(
        send_reminder,
        'date',
        run_date=run_time,
        args=[line_bot_api, user_id, time_text],
    )
    return True