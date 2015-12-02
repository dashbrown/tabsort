from itertools import permutations

filename = "tabsort.txt"

def bubble(list,offset):
  lmin = min(list)
  imin = list.index(lmin)
  iters = 0
  while list[0] != lmin:  
    if imin+offset in list:
      i = list.index(imin+offset)
      iters += 1
      list[i],list[imin] = list[imin],list[i]
      imin = i
    else:
      for i in xrange(len(list)):
        if list[i]-offset >= imin:
          iters+=1
          list[i],list[imin] = list[imin],list[i]
          imin = i
          break
  return list,iters

def bubblesort(list):
  l = len(list)
  iters = 0
  with open(filename, 'a') as f:
    for i in xrange(l):
      f.write(to_lol(list) + "\n")
      bubbled = bubble(list[i:],i)
      list[i:] = bubbled[0]
      iters+=bubbled[1]
    f.write(to_lol(list) + "\n\n")
    return list,iters

def bubble_all():
  perms_tuple = permutations([0,1,2,3,4])
  perms = []
  for perm in perms_tuple:
    perms.append(list(perm))
  for perm in perms:
    bubble = bubblesort(perm[:])[1]
    print perm,bubble

def to_lol(list):
  string = str(list)
  string = string.replace("0","top")
  string = string.replace("1","jungle")
  string = string.replace("2","mid")
  string = string.replace("3","baby")
  string = string.replace("4","parent")
  return string + "\\newline"


if __name__ == '__main__':
  bubble_all()
  print to_lol("[1,2,3,4,0]")

