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
    def _left_rotate(self, son):
        father = son.right
        son.right = father.left
        if father.left != self.NIL:
            father.left.parent = son
        father.parent = son.parent
        if son.parent is None:
            self.root = father
        elif son == son.parent.left:
            son.parent.left = father
        else:
            son.parent.right = father
        father.left = son
        son.parent = father

    # Rotación a la derecha; Único del árbol Rojo-Negro
    def _right_rotate(self, father):
        son = father.left
        father.left = son.right
        if son.right != self.NIL:
            son.right.parent = father
        son.parent = father.parent
        if father.parent is None:
            self.root = son
        elif father == father.parent.right:
            father.parent.right = son
        else:
            father.parent.left = son
        son.right = father
        father.parent = son

    # Agrega un elemento al 'Tree-Set'
    def add(self, key):
        if self.contains(key):
            return False
        node = RBNode(key, left=self.NIL, right=self.NIL)
        father = self.NIL
        son = self.root

        while son != self.NIL:
            father = son
            if node.key < son.key:
                son = son.left
            else:
                son = son.right

        node.parent = father
        if father is self.NIL:
            self.root = node
        elif node.key < father.key:
            father.left = node
        else:
            father.right = node

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


    # Arregla un posible incumplimiento de las propiedades del arbol
    def _fix_insert(self, node):
        if node.parent is None or node.parent.color == BLACK:       #Caso1, Caso2
            return
        if node.parent == self.root and node.parent.color == RED:      #Caso3
            self.root.color = BLACK
            return
        if node.parent != self.root:
            if node.parent.parent.right.color == RED:           #Caso4a, Caso4b
                self.recolor(node, "Case4")
                self._fix_insert(node.parent.parent)
                return
            else:
                if node == node.parent.left:                    #caso5
                    self._right_rotate(node.parent)
                    self.recolor(node, "Case5")
                    return
                else:
                    self._left_rotate(node)                     #Caso 6
                    self._right_rotate(node.parent)
                    self.recolor(node, "Case5")
                    return


    # Retorna un valor boleano dependiendo si el arbol está vacío
    def isEmpty(self):
        if self.root == self.NIL:
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
            node.parent.right.color=RED
            return
    #Retorna el tamaño del arbol
    def size(self):
        return self._size


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
