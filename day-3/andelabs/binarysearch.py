class BinarySearch(list):
  def __init__(self, integera, integerb):
    self.integera = integera
    self.integerb = integerb
    lst = [x for x in range (integerb, integera+1, integerb)]
    self.length = len(lst)
    
  def search(self,x):
    mylist = self.lst
    first = 0
    last = self.length -1
    diction = {}
    count =0
    while first<last:
      count = count+1
      if first == last:
        return -1
      middle =(first+last)//2
      middle_item = mylist[middle]
      if middle_item == x:
        diction ['count'] = count
        diction ['index'] = middle
        return diction
      else:  
        if middle_item < x:
          first = middle + 1
        else:
          last = middle
