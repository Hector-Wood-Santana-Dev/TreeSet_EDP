# Implementación del nodo de un árbol rojo-negro en python 
RED = True
BLACK = False

class RBNode:
    def __init__(self, key, color=RED, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class TreeSet:
    def __init__(self, collection=None):
        self.NIL = RBNode(None, color=BLACK)
        self.root = self.NIL
        self._size = 0
        if collection:
            for item in collection:
                self.add(item)

    # Rotación a la izquierda; Único del árbol Rojo-Negro
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Rotación a la derecha; Único del árbol Rojo-Negro
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    # Agrega un elemento al 'Tree-Set'
    def add(self, key):
        if self.contains(key):
            return False
        node = RBNode(key, left=self.NIL, right=self.NIL)
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.color = RED
        self._fix_insert(node)
        self._size += 1
        return True

    # Agrega todos los elementos de una colección al 'Tree-Set'
    def addAll(self, collection):
        changed = False
        for item in collection:
            changed |= self.add(item)
        return changed

    # Retorna el primer elemento
    def first(self):
        if self.isEmpty():
            raise ValueError("TreeSet is empty")
        node = self.root
        while node.left != self.NIL:
            node = node.left
        return node.key

    # Retorna el último elemento
    def last(self):
        if self.isEmpty():
            raise ValueError("TreeSet is empty")
        node = self.root
        while node.right != self.NIL:
            node = node.right
        return node.key

    def contains(self, node, key):
        if node is None:
            return false
        if key==node.key:
            return True
        if node.right is None or node.left is None:
            return False
        elif key < node.key:
            return self.contains(node.left, key)
        else:
            return self.contains(node.right, key)

# Implementación del TreeSet usando un árbol rojo-negro en python
'''


        def __len__(self):
            return self.lenght

        def  ceiling(self):
            return True

        def clear(self):
            return True

        def clone(self):
            return True

        def descendingIterator(self):
            yield

        def floor(self,e):
            return vakye

        def higher(self,e):
            return value

        def isEmpty(self):
            return True

        def iterator(self):
            yield

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
