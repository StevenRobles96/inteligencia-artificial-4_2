class Node(object):
    def __init__(self, label: str=None):
        self.label = label
        self.children = []
        
    def __lt__(self,other):
        return (self.label < other.label)
    
    def __gt__(self,other):
        return (self.label > other.label)
    
    def __repr__(self):
        return '{}'.format(self.label)
    
    def add_child(self, node, cost=1):
        if type(node) is list:
            [self.add_child(sub_node) for sub_node in node]
            return
        edge = Edge(self, node, cost)
        self.children.append(edge)
    
    
class Edge(object):
    
    def __init__(self, source: Node, destination: Node, cost: int=1, bidirectional: bool=False):
        self.source = source
        self.destination = destination
        self.cost = cost
        self.bidirectional = bidirectional
    
    def __repr__(self):
        return '{}'.format(self.cost)
        
        def iddfs(root: Node, goal: str, maximum_depth: int = 10):
    for depth in range(0, maximum_depth):
        result = _dls([root], goal, depth)
        if result is None:
            continue
        return result
    
    raise ValueError('goal not in graph with depth {}'.format(maximum_depth))

def _dls(path: list, goal: str, depth: int):
    current = path[-1]
    if current.label == goal:
        return path
    if depth <= 0:
        return None
    for edge in current.children:
        new_path = list(path)
        new_path.append(edge.destination)
        result = _dls(new_path, goal, depth - 1)
        if result is not None:
            return result
            
      
   
            """PRIMER GRAFO""""
            
            
            """ Inicializacion de los nodos """

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

""" Inicializacion de los hijos de cada nodo """
A.add_child([B, C, E])
B.add_child([A, D, F])
C.add_child([G, A])
D.add_child(B)
E.add_child([F, A])
F.add_child([E, B])
G.add_child(C)

_ = [print(node) for node in [A, B, C, D, E, F, G]]

iddfs(D, 'F')

              """SEGUNDO GRAFO"""
              
              """ Inicializacion de los nodos """

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
J = Node('J')

""" Inicializacion de los hijos de cada nodo """
A.add_child([B, H])
B.add_child([A, C, E])
C.add_child([D, B])
D.add_child(C)
E.add_child([B, F, G])
F.add_child(E)
G.add_child([E, J])
H.add_child([A, I])
I.add_child([H, J])
J.add_child([I, G])

_ = [print(node) for node in [A, B, C, D, E, F, G, H, I, J]]

iddfs(D, 'J')

             """TERCER GRAFO"""
             
""" Inicializacion de los nodos """

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
J = Node('J')
K = Node('K')
L = Node('L')
M = Node('M')

""" Inicializacion de los hijos de cada nodo """
A.add_child([B, H])
B.add_child([A, C, F])
C.add_child([B, D])
D.add_child([C, E, G])
E.add_child([D, M])
F.add_child([B, D])
G.add_child([D, L])
H.add_child([A, I, J])
I.add_child([H])
J.add_child([H, K])
K.add_child([J, L, M])
L.add_child([K, G])
M.add_child([K, E])

_ = [print(node) for node in [A, B, C, D, E, F, G, H, I, J, K, L, M]]

iddfs(A, 'M')
