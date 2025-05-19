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

# Implementación del TreeSet usando un árbol rojo-negro en python
    def ceiling(self, e):
        node = self.root
        result = None
        while node != self.NIL:
            if e == node.key:
                return node.key
            if e < node.key:
                result = node
                node = node.left
            else:
                node = node.right
        return result.key if result else None

    def clear(self):
        return True

    def clone(self):
        return True

    def contains(self, o):
        node = self.root
        while node != self.NIL:
            if o == node.key:
                return True
            elif o < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def descendingIterator(self):
        stack = []
        node = self.root
        while stack or node != self.NIL:
            while node != self.NIL:
                stack.append(node)
                node = node.right
            node = stack.pop()
            yield node.key
            node = node.left

    def floor(self, e):
        node = self.root
        result = None
        while node != self.NIL:
            if e == node.key:
                return node.key
            if e > node.key:
                result = node
                node = node.right
            else:
                node = node.left
        return result.key if result else None

    def higher(self, e):
        node = self.root
        result = None
        while node != self.NIL:
            if e < node.key:
                result = node
                node = node.left
            else:
                node = node.right
        return result.key if result else None

    def isEmpty(self):
        return True

    def iterator(self):
        stack = []
        node = self.root
        while stack or node != self.NIL:
            while node != self.NIL:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.key
            node = node.right

    def lower(self, e):
        node = self.root
        result = None
        while node != self.NIL:
            if e > node.key:
                result = node
                node = node.right
            else:
                node = node.left
        return result.key if result else None

    def pollFirst(self):
        if self.isEmpty():
            return None
        node = self.root
        while node.left != self.NIL:
            node = node.left
        key = node.key
        self.remove(key)
        return key

    def pollLast(self):
        if self.isEmpty():
            return None
        node = self.root
        while node.right != self.NIL:
            node = node.right
        key = node.key
        self.remove(key)
        return key

    def remove(self, o):
        return True

    def size(self):
        return self._size