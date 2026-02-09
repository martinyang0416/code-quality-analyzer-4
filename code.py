from datetime import date

day, month, year = map(int, input().split())
d = date(year, month, day)
print(d.strftime("%A"))