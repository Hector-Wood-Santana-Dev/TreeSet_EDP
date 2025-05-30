# Implementación del nodo de un árbol rojo-negro en Python
RED = True
BLACK = False

class RBNode:
    def __init__(self, key, color=RED, left=None, right=None, parent=None):
        # Inicializa un nodo con clave, color, hijos y padre
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class TreeSet:
    def __init__(self, collection=None):
        # Inicializa el TreeSet y añade los elementos de la colección opcional
        self.type = None
        self.NIL = RBNode(None, color=BLACK)
        self.root = self.NIL
        self._size = 0
        if collection:
            for item in collection:
                self.add(item)

    # Realiza una rotación a la izquierda desde el nodo dado
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

    # Realiza una rotación a la derecha desde el nodo dado
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

    # Agrega un elemento al 'Tree-Set' (si no existe)
    def add(self, key):
        if self.type is None:
            self.type = type(key)
        elif type(key) != self.type:
            raise TypeError(f"TreeSet only supports elements of type {self.type.__name__}")

        if self.contains(key):
            return False

        node = RBNode(key, color=RED, left=self.NIL, right=self.NIL)
        father = None
        son = self.root

        while son != self.NIL:
            father = son
            if node.key < son.key:
                son = son.left
            else:
                son = son.right

        node.parent = father
        if father is None:
            self.root = node
        elif node.key < father.key:
            father.left = node
        else:
            father.right = node

        self._fix_insert(node)
        self._size += 1
        return True

    # Agrega todos los elementos de una colección al 'Tree-Set'
    def addAll(self, collection):
        changed = False
        for item in collection:
            changed |= self.add(item)
        return changed

    # Retorna el primer elemento (mínimo)
    def first(self):
        if self.isEmpty():
            raise ValueError("TreeSet is empty")
        node = self.root
        while node.left != self.NIL:
            node = node.left
        return node.key

    # Retorna el último elemento (máximo)
    def last(self):
        if self.isEmpty():
            raise ValueError("TreeSet is empty")
        node = self.root
        while node.right != self.NIL:
            node = node.right
        return node.key


    # Reestablece las propiedades del árbol rojo-negro después de una inserción
    def _fix_insert(self, node):
        while node != self.root and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._left_rotate(node.parent.parent)
        self.root.color = BLACK


    # Verifica si el árbol está vacío
    def isEmpty(self):
        return self.root == self.NIL

    # Recolorea los nodos según el caso de corrección (no utilizada activamente)
    def recolor(self, node, case):
        if case=="Case1":
            node.parent.parent.right.color = BLACK
            node.parent.color = BLACK
            node.parent.parent.color = RED
            return
        elif case=="Case5":
            node.parent.color=BLACK
            node.parent.right.color=RED
            return

    # Devuelve el número de elementos en el TreeSet
    def size(self):
        return self._size

    # Devuelve el menor elemento mayor o igual que `e`
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

    # Elimina todos los elementos del árbol
    def clear(self):
        self.root = self.NIL
        self._size = 0
        self.type = None

    # Retorna una copia del TreeSet
    def clone(self):
        return TreeSet(list(self.iterator()))

    # Verifica si el elemento está en el conjunto
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

    # Iterador en orden descendente
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

    # Devuelve el mayor elemento menor o igual que `e`
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

    # Devuelve el menor elemento estrictamente mayor que `e`
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

    # Iterador en orden ascendente
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

    # Permite usar TreeSet en bucles for directamente
    def __iter__(self):
        return self.iterator()

    # Devuelve el mayor elemento estrictamente menor que `e`
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

    # Elimina y devuelve el primer elemento (mínimo)
    def pollFirst(self):
        if self.isEmpty():
            return None
        node = self.root
        while node.left != self.NIL:
            node = node.left
        key = self.first()
        self.remove(key)
        return key

    # Elimina y devuelve el último elemento (máximo)
    def pollLast(self):
        if self.isEmpty():
            return None
        node = self.root
        while node.right != self.NIL:
            node = node.right
        key = self.last()
        self.remove(key)
        return key

    # Elimina un elemento del árbol (si existe)
    def remove(self, key):
        if self.isEmpty():
            return False
        if self.type is not None and type(key) != self.type:
            return False
        node = self.find_node(key)
        if node is None:
            return False
        self.delete_node(node)
        self._size -= 1
        if self._size == 0:
            self.type = None
        return True

    # Encuentra el nodo que contiene la clave dada
    def find_node(self, k):
        current = self.root
        while current != self.NIL:
            if k == current.key:
                return current
            elif k < current.key:
                current = current.left
            else:
                current = current.right
        return None

    # Sustituye un subárbol por otro durante la eliminación
    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Elimina un nodo del árbol y reestablece las propiedades del árbol rojo-negro
    def delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.successor(z)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self.fix_deletion(x)

    # Arregla el árbol si hay violaciones después de una eliminación
    def fix_deletion(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    # Devuelve el sucesor en inorden del nodo dado
    def successor(self, node):
        if node.right != self.NIL:
            current = node.right
            while current.left != self.NIL:
                current = current.left
            return current
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent










