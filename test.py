
from SplayDataStructF import *

class splayNode:
    def __init__(self, key):
        self.key = key
        self.rc = None
        self.lc = None
        self.parent = None

    def toString(self):
        print("the node is " + str(self.key))
        if (self.lc is not None):
            print("the left child is " + str(self.lc.key))
        else:
            print("the left child is None")
        if (self.rc is not None):
            print("the right node is " + str(self.rc.key))
        else:
            print("the right node is None")
        if (self.parent is not None):
            print("the parent of this node is " + str(self.parent.key))
        else:
            print("the parent of this node is None")

            
def main ():
    
  d= SplayDataStruct()
  k=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
  for i in k:
      d.insert (splayNode(i))
  d.root.toString()
  d.find(1000).toString()
  d.find(6000).toString()
  d.findWithoutSplay(8000).toString()
  d.find(3000).toString()
  d.find (8000).toString()
  d.findWithoutSplay(6000).toString()
  d.findWithoutSplay(3000).toString()
  r=d.find(2500)
  if (r!=None):
      r.toString()
  d.root.toString()
  d.findWithoutSplay(8000).toString()
  d.delete(6000)
  d.findWithoutSplay(5000).toString()
  d.delete(3000)
  d.findWithoutSplay(5000).toString()
  d.delete(2000)
  d.root.toString()
if __name__=='__main__':
    main()
