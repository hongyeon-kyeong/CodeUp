h, b, c, s = map(int, input().split())

bit = h*b*c*s
byte = bit/8/1024/1024
print('%0.1f MB' % byte)