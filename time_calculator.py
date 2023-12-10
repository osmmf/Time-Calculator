def add_time(start_time, duration, start_day=None):
    start_time_parts = start_time.split()
    start_hour, start_minute = map(int, start_time_parts[0].split(':'))
    am_pm = start_time_parts[1]

    duration_hours, duration_minutes = map(int, duration.split(':'))

    if am_pm == "PM":
        start_hour += 12

    total_minutes = start_hour * 60 + start_minute + duration_hours * 60 + duration_minutes

    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    new_am_pm = "AM" if new_hour < 12 else "PM"

    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    new_time = f"{new_hour:02d}:{new_minute:02d} {new_am_pm}"

    days_later = total_minutes // 1440
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    if start_day:
        start_day = start_day.capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", ""]
        start_index = days_of_week.index(start_day)
        new_day_index = (start_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    return new_time
