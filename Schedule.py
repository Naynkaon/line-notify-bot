import re
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

def get_run_time(text):
    match = re.search(r'\b([01]?\d|2[0-3]):([0-5]\d)\b', text)
    if not match:
        return None

    hour, minute = int(match.group(1)), int(match.group(2))
    now = datetime.now()
    run_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    # If the time has already passed today, schedule for tomorrow
    if run_time < now:
        run_time += timedelta(days=1)

    return run_time

def set_scheduler(job,StartTime):
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'date', run_date=get_run_time(StartTime))
    scheduler.start()

    return "成功設定提醒"