class BinarySearch(list):
    def _init_ (self,alist):
        self.len(alist)==0
        def binary_Search(item):
            if len(alist) == 0:
                return False
            else:
                midpoint = len(alist)//2
            if alist[midpoint]==item:
                return True
            else:
                if item<alist[midpoint]:
                    return binarySearch(alist[:midpoint],item)
                else:
                    return binarySearch(alist[midpoint+1:],item)
