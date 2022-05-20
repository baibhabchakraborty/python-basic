t = 20
d1 =240
d2 = 360
d3 = 480

s1 = d1/t
s2 = d2/t
s3 = d3/t

if max(s1,s2,s3) == s1:
    print(d1)
elif max(s1,s2,s2) == s2:
    print(d2)
else:
    print(d3)

    