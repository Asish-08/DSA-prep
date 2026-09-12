# Last updated: 9/12/2026, 12:02:32 PM
x, r = divmod(x, 10)
if x > int_max // 10 or (x == int_max // 10 and r > 7):
    return 0