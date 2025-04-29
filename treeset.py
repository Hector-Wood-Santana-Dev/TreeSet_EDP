# Implementación del nodo de un árbol rojo-negro en python 
class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color  # 'RED' or 'BLACK'
        self.left = left
        self.right = right
        self.parent = parent

class TreeSet:
    def __init__(self):
        self.TNULL = Node(None, 'BLACK') # Nodo Sentinela
        self.root = self.TNULL

    def insertar(self, key):
        

# Implementación del TreeSet usando un árbol rojo-negro en python
'''
class treeset:

    def __init__(self):
        self.lenght = 0

    def __len__(self):
        return self.lenght

    def add(self, e):
        return True

    def adAll(self, collection):
        return True

    def  ceiling(self):
        return True

    def clear(self):
        return True

    def clone(self):
        return True

    def contains(self):
        return True

    def descendingIterator(self):
        yield

    def firts(self):
        return value

    def floor(self,e):
        return vakye

    def higher(self,e):
        return value

    def isEmpty(self):
        return True

    def iterator(self):
        yield

    def last(self):
        return value

    def lower(self):
        return value

    def pollFirts(self):
        return value

    def pollLast(self):
        return value

    def remove(self, o):
        return True

    def size(self):
        return size
  
'''