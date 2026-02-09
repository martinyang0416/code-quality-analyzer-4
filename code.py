# Cumulative distance for each IC (1-7)
cumulative_distance = [0, 5, 15, 17, 30, 45, 58]
# Cumulative fare for each IC (1-7)
cumulative_fare = [0, 250, 500, 700, 950, 1300, 2000]

while True:
    d_line = input().strip()
    if d_line == '0':
        break
    d = int(d_line) - 1  # Convert to 0-based index
    hd, md = map(int, input().split())
    a = int(input().strip()) - 1
    ha, ma = map(int, input().split())
    
    # Calculate distance and fare
    distance = abs(cumulative_distance[a]