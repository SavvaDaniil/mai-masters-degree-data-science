from datetime import datetime, timedelta

if __name__ == '__main__':
    now: datetime = datetime.now()
    print(f'Текущее дата и время: {now}')

    random_date: datetime = datetime.strptime("2024-12-12 23:59:59", "%Y-%m-%d %H:%M:%S")
    difference_between_dates: timedelta = random_date - now
    print(f"Разницу между датами составляет: {difference_between_dates.days} дней")