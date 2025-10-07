from datetime import datetime, date, timedelta
#task 1
x=date.today()
new=x-timedelta(days=5)
print(f"5 days from now: {new}")
#task 2
w=date.today()
print(f"Today: {w}")
y=date.today()
tommorow=y+timedelta(days=1)
print(f"Tomorrow: {tommorow}")
z=date.today()
yesterday=z-timedelta(days=1)
print(f"Yesterday: {yesterday}")
#task 3
gg=datetime.now()
micro=gg.replace(microsecond=0)
print(micro)
#task 4
date1=datetime(2025, 10, 7, 12, 0, 0)
date2=datetime(2025, 10, 5, 8, 30, 0)
diff=date1-date2
sec=diff.total_seconds()
print(f"Difference: {sec}")
