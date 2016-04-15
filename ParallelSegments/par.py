def angle(x1,x2,y1,y2):
    return (y2-y1)/(x1-x2)

def parallel(arr):
    if len(arr) > 8 or len(arr) < 8:
        return 'short 8 values'
    return 'Yes' if angle(arr[0],arr[1],arr[2],arr[3]) == angle(arr[4],arr[5],arr[6],arr[7]) else 'NO'


get_data = [int(x) for x in input().split(',')]
print(parallel(get_data))
