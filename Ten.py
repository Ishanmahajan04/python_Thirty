def overlapping(lst1, lst2):
  for i in lst1:
    for j in lst2:
      if i == j:
        return True
  return False


print(overlapping(['sad','sd','dfd','df','cv','we'], ['sad','sdf','cvcdf','dfre']))