#!/usr/bin/env python3

def detect_ranges(L):
    x = len(L)
    Lsorted = L
    #sorting algorithm
    for i in range(x):
        for j in range(i, 0, -1):
            if Lsorted[j] <  Lsorted[j-1]: 
                Lsorted[j - 1], Lsorted[j] = Lsorted[j], Lsorted[j-1]

    final = []
    end = Lsorted[0]
    start = Lsorted[0]
    
    for i in range(1, x):
        if end + 1  == Lsorted[i]: 
            end = Lsorted[i]
        else:
            if start == end:
                final.append(start)
            else:
                final.append((start, end + 1))
            
            start = Lsorted[i]
            end = Lsorted[i]
        
    if start == end:
        final.append(start)
    else:
        final.append((start, end + 1))


    return final

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
