import os
from icalendar import Calendar

CALENDAR_PATH = os.getenv("CALENDAR_PATH")

with open(CALENDAR_PATH, "rb") as f:
    cal = Calendar.from_ical(f.read())

events = []
for event in cal.walk("vevent"):
    start = event.get("dtstart").dt
    end = event.get("dtend").dt
    summary = event.get("summary")
    events.append({
        "start_time": start.strftime("%H:%M"),
        "end_time": end.strftime("%H:%M"),
        "date": start.strftime("%Y-%m-%d"),
        "summary": summary
    })


def get_calendar_meetings():
    """
    Get my calendar meetings in a JSON format. Each meeting is an object inside the meetings array key.
    The events are displayed in the following format:
    {
        "meetings": [{
            "start_time": start time of the meeting,
            "end_time": end time of the meeting,
            "date": date of the meeting in the format year-month-day,
            "summary": summary
        }]
    }
    
    e.g.
    {
        "meetings": [{
            "start_time": "09:00",
            "end_time": "09:30",
            "date": "2025-10-17",
            "summary": "Daily Standup"
        }]
    }
    
    Args:
        None
    
    Returns:
        dict: Calendar events
    """

    return {
        "meetings": events
    }
