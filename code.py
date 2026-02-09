vp = int(input())
vd = int(input())
t = int(input())
f = int(input())
c = int(input())

if vp >= vd:
    print(0)
else:
    current = vp * t
    if current >= c:
        print(0)
    else:
        bijous = 0
        while True:
            time_catch = current / (vd - vp)
            position_meet = current + vp * time_catch
            if position_meet >= c:
                break
            bijous += 1
            time_away = (position_meet / vd) + f
            current = position_meet + vp * 