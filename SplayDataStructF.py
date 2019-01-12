class SplayDataStruct:
    def __init__(self):
        self.root = None
        self.lc = None
        self.rc = None
        self.parent = None

    def insert(self, newNode):
        if (self.root is None):
            self.root = newNode
        else:
            self.__insert(self.root, newNode)
            self.__splay(newNode)

    def __insert(self, x, newNode):
        if (newNode.key > x.key and x.rc != None):
            self.__insert(x.rc, newNode)
        elif (newNode.key < x.key and x.lc != None):
            self.__insert(x.lc, newNode)
        elif (newNode.key > x.key and x.rc == None):
            newNode.parent = x
            x.rc = newNode
        elif (newNode.key < x.key and x.lc == None):
            newNode.parent = x
            x.lc = newNode

    def __splay(self, node):
        while (True):
            p = node.parent
            gp = p.parent if p != None else None
            if (node.key == self.root.key):
                return
            elif (gp != None):
                if (node.key < p.key and p.key < gp.key):
                    self.__RR(node)
                elif (node.key > p.key and p.key > gp.key):
                    self.__LL(node)
                elif (node.key < p.key and p.key > gp.key):
                    self.__RL(node)
                elif (node.key > p.key and p.key < gp.key):
                    self.__LR(node)
            elif (p != None):
            #    print(self.root.key, node.key)
                if (node.key < p.key):
                    self.__R(node)
                elif (node.key > p.key):
                    self.__L(node)
            else:
                print("there is a problem here ")
                exit(1)

    def find(self, key):
        j = self.root
        if j == None:
            print("root is Null")
            return None
        if (j.key == key):
            return j
        else:
            while (j != None and j.key != key):
                p = j
                if (key < j.key):
                    j = j.lc
                elif (key > j.key):
                    j = j.rc
        if j == None:
            self.__splay(p)
            print("the element searched Does Not exist")
            return None
        else:
            self.__splay(j)
        return j

    def findWithoutSplay(self, key):
        j = self.root
        if j == None:
            print("root is Null")
            return None
        if (j.key == key):
            return j
        else:
            while (j != None and j.key != key):
                if (key < j.key):
                    j = j.lc
                elif (key > j.key):
                    j = j.rc
        if j == None:
            print("this element Does Not exist")
            return None
        return j

    def __LL(self, node):
        gp = node.parent.parent
        p = node.parent

        node.parent = (gp.parent if gp != None else None)
        if gp == self.root:
            self.root = node
        p.rc = node.lc
        node.lc = p
        p.parent = node
        if p.rc != None:
            p.rc.parent = p

        gp.rc = p.lc
        p.lc = gp
        gp.parent = p
        if gp.rc != None:
            gp.rc.parent = gp

    def __RR(self, node):
        gp = node.parent.parent
        p = node.parent
        node.parent = (gp.parent if gp != None else None)
        if gp == self.root:
            self.root = node
        p.lc = node.rc
        node.rc = p
        p.parent = node
        if p.lc != None:
            p.lc.parent = p
        gp.lc = p.rc
        p.rc = gp
        gp.parent = p
        if gp.lc != None:
            gp.lc.parent = gp

    def __L(self, node):
        p = node.parent
        node.parent = p.parent
        if (p == self.root):
            self.root = node

        p.rc = node.lc
        node.lc = p
        p.parent = node
        if p.rc != None:
            p.rc.parent = p

    def __R(self, node):
        p = node.parent
        node.parent = p.parent
        if (p == self.root):
            self.root = node
        p.lc = node.rc
        node.rc = p
        p.parent = node
        if p.lc != None:
            p.lc.parent = p

    def __LR(self, node):
        self.__L(node)
        self.__R(node)

    def __RL(self, node):
        self.__R(node)
        self.__L(node)

    def delete(self, key):
        j = self.findWithoutSplay(key)
        if (j.lc == j.rc == None):  # this is first case
            self.__firstCaseDeletion(j)
        elif (self.__hasOneChild(j)):
            self.__secondCaseDeletion(j)
        else:  # else it has two children the condition of two children will be checked in the has one child
            self.__thirdCaseDeletion(j)

    def __hasOneChild(self, j):
        if (j.lc == None and j.rc != None) or (j.rc == None and j.lc != None):
            return True
        else:
            return False

    def __firstCaseDeletion(self, j):
        p = j.parent
        if p != None:
            if j.key > p.key:
                p.rc = None
            else:
                p.lc = None
        else:
            if j == self.root:
                self.root = None

    def __secondCaseDeletion(self, j):
        p = j.parent
        if p != None:
            if (j.lc != None):
                if j.key > p.key:
                    p.rc = j.lc
                    p.rc.parent = p
                else:
                    p.lc = j.lc
                    p.lc.parent = p
            elif (j.rc != None):
                if j.key > p.key:
                    p.rc = j.rc
                    p.rc.parent = p
                else:
                    p.lc = j.rc
                    p.lc.parent = p
            else:
                print("there is a problem in Second Case of Splay Deletion")
                exit(2)
        else:
            if (j.lc != None):
                j.lc.parent = None
                self.root = j.lc
            else:
                j.rc.parent = None
                self.root = j.rc

    def __thirdCaseDeletion(self, j):
        temp = j.lc
        if temp.rc == None:
            temp.rc = j.rc
            temp.rc.parent = temp
            temp.parent = j.parent
        else:
            while (temp.rc != None):
                temp = temp.rc
            if (temp.lc != None):
                self.__secondCaseDeletion(temp)
            else:
                self.__firstCaseDeletion(temp)
            temp.lc = j.lc
            temp.lc.parent = temp
            temp.rc = j.rc
            temp.rc.parent = temp
            temp.parent = j.parent
            if j.parent != None:
                if j.key > j.parent.key:
                    j.parent.rc = temp
                else:
                    j.parent.lc = temp
        if j == self.root:
            self.root = temp
