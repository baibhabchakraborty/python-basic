s = "02:00:00PM"
t = s[:8]
dn = s[8:]
h, m, s = t.split(':')
h = int(h)
if dn == "PM":
    if h != 12:
        h += 12
    print(f"{h}:{m}:{s}")
else:
    if h == 12:
        h = "0"
    h = "0" + str(h)
    print(f"{h}:{m}:{s}")