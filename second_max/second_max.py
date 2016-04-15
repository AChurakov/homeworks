def get_sec_max(arr):
  try:
      return max(a for a in arr if a !=max(arr))
  except:
      return 'NO'

get_data = [int(x) for x in input().split(',')]
print(get_sec_max(get_data))

