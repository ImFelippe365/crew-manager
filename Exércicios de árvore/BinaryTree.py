class Knot:
    def __init__(self, value, smaller = None, bigger = None):
        self.value = value
        self.bigger_leaf = bigger
        self.smaller_leaf = smaller

    def add(self, value):
        if (value == self.value):
            return

        if value > self.value:
            if self.bigger_leaf is None:
                self.bigger_leaf = Knot(value)
            else:
                return self.bigger_leaf.add(value)
        else:
            if self.smaller_leaf is None:
                self.smaller_leaf = Knot(value)
            else:
                return self.smaller_leaf.add(value)
            
    def get_max_value(self, knot):
        if knot.bigger_leaf is None:
            return knot
        
        return self.get_max_value(knot.bigger_leaf)
    
    def get_min_value(self, knot):
        if knot.smaller_leaf is None:
            return knot
        
        return self.get_min_value(knot.smaller_leaf)
            
    def remove(self, value, knot, previous_knot):
        if knot is None:
            return 'Não encontrado'
        
        if knot.value == value:
            # Remover o nó quando não possuir folhas
            if knot.smaller_leaf is None and knot.bigger_leaf is None:
                if value > previous_knot.value:
                    previous_knot.bigger_leaf = None
                else:
                    previous_knot.smaller_leaf = None

                return knot

            # Remover o nó quando tiver pelo menos uma das folhas
            if knot.smaller_leaf is None or knot.bigger_leaf is None:
                knot_to_substitute = None

                if knot.smaller_leaf:
                    knot_to_substitute = knot.smaller_leaf
                else:
                    knot_to_substitute = knot.bigger_leaf

                if value > previous_knot.value:
                    previous_knot.bigger_leaf = knot_to_substitute
                else:
                    previous_knot.smaller_leaf = knot_to_substitute
                    
                return knot

            # Remover o nó quando tiver dois filhos
            if knot.smaller_leaf and knot.bigger_leaf:
                successor_knot = self.get_min_value(knot.bigger_leaf)
                knot_to_substitute = self.remove(successor_knot.value, knot, knot)
                knot.value = knot_to_substitute.value
                    
                return knot
            
            return 'Encontrou, mas não fez nada'
        
        return self.remove(value, knot.smaller_leaf if knot.value > value else knot.bigger_leaf, knot)
        
            
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.bigger_leaf is None and self.smaller_leaf is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.bigger_leaf is None:
            lines, n, p, x = self.smaller_leaf._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.smaller_leaf is None:
            lines, n, p, x = self.bigger_leaf._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.smaller_leaf._display_aux()
        right, m, q, y = self.bigger_leaf._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class Tree:
    def __init__(self, root):
        self.root = Knot(root)

        self.insert = self.root.add
        self.remove = self.root.remove
        self.display = self.root.display
    
    def get_height(self, knot):
        if knot is None:
            return 0
        
        return 1 + max(self.get_height(knot.smaller_leaf), self.get_height(knot.bigger_leaf))
    
    def get_leaves_quantity(self, knot):
        if knot is None:
            return 0

        if knot.smaller_leaf is None and knot.bigger_leaf is None:
            return 1
        
        return self.get_leaves_quantity(knot.smaller_leaf) + self.get_leaves_quantity(knot.bigger_leaf)
    
    def get_knot_quantity(self, knot):
        if knot is None or knot.smaller_leaf is None or knot.bigger_leaf is None:
            return 0
        
        return 1 + self.get_knot_quantity(knot.smaller_leaf) + self.get_knot_quantity(knot.bigger_leaf)


new_tree = Tree(15)

new_tree.insert(5)
new_tree.insert(3)
new_tree.insert(12)
new_tree.insert(10)
new_tree.insert(13)
new_tree.insert(6)
new_tree.insert(7)

new_tree.insert(16)
new_tree.insert(20)
new_tree.insert(18)
new_tree.insert(23)

print('Árvore binária')
print(25*'-')
print('Tamanho da árvore ->', new_tree.get_height(new_tree.root))
print('Quantidade de nós ->', new_tree.get_knot_quantity(new_tree.root))
print('Quantidade de folhas ->', new_tree.get_leaves_quantity(new_tree.root))
print(25*'-')
print('Antes')
new_tree.display()
print(25*'-')
print('Depois')
new_tree.remove(16, new_tree.root, new_tree.root)
new_tree.remove(15, new_tree.root, new_tree.root)
new_tree.display() 
print(25*'-')