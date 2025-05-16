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


    # Arregla un posible incumplimiento de las propiedades del arbol
    def _fix_insert(self, node):
        if node.parent is None or node.parent.color == BLACK:       #Caso1, Caso2
            return
        if node.parent == self.root and node.parent.color == RED:      #Caso3
            self.root.color = BLACK
            return
        if node.parent != self.root:
            if node.parent.parent.right.color == RED:           #Caso4a, Caso4b
                self.recolor(node, "Case1")
                self._fix_insert(node.parent.parent)
                return
            else:
                if node == node.parent.left:                    #caso5
                    self._right_rotate(node)
                    self.recolor(node, "Case5")
                    return
                else:
                    self._left_rotate(node)                     #Caso 6
                    self._right_rotate(node)
                    self.recolor(node, "Case5")
                    return


    # Retorna un valor boleano dependiendo si el arbol está vacío
    def isEmpty(self):
        if self.root.key is None:
            return True
        return False

    # Realiza un recoloreado dependiendo de que caso sea
    def recolor(self, node, case):
        if case=="Case1":
            node.parent.parent.right.color = BLACK  # Tío
            node.parent.color = BLACK  # Padre
            node.parent.parent.color = RED  # abuelo
            return
        elif case=="Case5":
            node.parent.color=BLACK
            node.parent.right=RED
            return

    def size(self):
        return self._size


# Implementación del TreeSet usando un árbol rojo-negro en python
'''

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


'''
