from datetime import datetime

dt1 = datetime(2025, 1, 1)
dt2 = datetime(2025, 1, 31)

diff1 = dt2 - dt1
diff2 = dt1 - dt2
abs_diff = abs(dt1 - dt2)

print(f"dt2 - dt1: {diff1}")
print(f"dt1 - dt2: {diff2}")
print(f"abs(dt1 - dt2): {abs_diff}")