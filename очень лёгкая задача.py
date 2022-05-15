import sys
N, x, y = input().split()
x, y, N = min(int(x), int(y)), max(int(x), int(y)), int(N) - 1 #x - всегда наименьшее время, y - всегда наибольшее.
time = x #первая необходимая копия сделана 
if x == y and N > 0:
    if N % 2 != 0:
        time += x
        N -= 1
    time += (N/2) * x
    print(int(time))
    sys.exit()
    
while N > 0:
    while N * x > y and N > 1: #в любом случае будет напечатана копия на y
        if y % x == 0:
            N = N - 1 - y // x 
            time += y
        else:
            rest = y % x 
            while rest > 0:
                if N > 0 and (x * N) + rest > y - rest:
                    time += y
                    N = N - 2
                    rest = y - (y % x)
                    if rest < x and N > 0:
                        rest = x - rest
                        N -= 1
                    elif rest >= x and N > 0:
                        rest -= (rest % x)
                        N -= rest // x
                else:
                    N -= 1
                    time += rest
                    break
                
        if N == 0:
            print(int(time))
            sys.exit()
    N -= 1
    time += x
print(int(time))
