import networkx as nx
from itertools import product
from functools import cache

codes = """286A
480A
140A
413A
964A""".split("\n")

kp_num = nx.grid_2d_graph(3, 4)
kp_num.remove_node((0, 0))

mapping = {
    (0, 1): "1",
    (0, 2): "4",
    (0, 3): "7",
    (1, 0): "0",
    (1, 1): "2",
    (1, 2): "5",
    (1, 3): "8",
    (2, 0): "A",
    (2, 1): "3",
    (2, 2): "6",
    (2, 3): "9"
}

kp_num = nx.relabel_nodes(kp_num, mapping)

kp_num_moves = {
    ("A", "0"): "<",
    ("0", "A"): ">",
    ("A", "3"): "^",
    ("3", "A"): "v",
    ("0", "2"): "^",
    ("2", "0"): "v",
    ("3", "2"): "<",
    ("2", "3"): ">",
    ("3", "6"): "^",
    ("6", "3"): "v",
    ("2", "1"): "<",
    ("1", "2"): ">",
    ("2", "5"): "^",
    ("5", "2"): "v",
    ("1", "4"): "^",
    ("4", "1"): "v",
    ("6", "5"): "<",
    ("5", "6"): ">",
    ("6", "9"): "^",
    ("9", "6"): "v",
    ("5", "4"): "<",
    ("4", "5"): ">",
    ("5", "8"): "^",
    ("8", "5"): "v",
    ("4", "7"): "^",
    ("7", "4"): "v",
    ("9", "8"): "<",
    ("8", "9"): ">",
    ("8", "7"): "<",
    ("7", "8"): ">"
}

kp_dir = nx.grid_2d_graph(3, 2)
kp_dir.remove_node((0, 1))

mapping = {
    (0, 0): "<",
    (1, 0): "v",
    (2, 0): ">",
    (1, 1): "^",
    (2, 1): "A"
}

kp_dir = nx.relabel_nodes(kp_dir, mapping)

kp_dir_moves = {
    (">", "v"): "<",
    ("v", ">"): ">",
    (">", "A"): "^",
    ("A", ">"): "v",
    ("v", "<"): "<",
    ("<", "v"): ">",
    ("v", "^"): "^",
    ("^", "v"): "v",
    ("A", "^"): "<",
    ("^", "A"): ">"
}


def get_inputs(output, graph, dict_):
    inputs = []
    for x, y in zip("A" + output, output):
        paths = nx.all_shortest_paths(graph, x, y)
        sub_inputs = ["".join(dict_[(u, v)] for u, v in zip(path, path[1:])) + "A" for path in paths]
        inputs.append(sub_inputs)
    return [''.join(s) for s in product(*inputs)]    
    

@cache
def min_length(seq, n):
    if  n == 0:
        return len(seq)
    if seq.count("A") > 1:
        return sum(min_length(pt, n) for pt in [x + "A" for x in seq.split("A")][:-1])
    else:
        return min(min_length(x, n - 1) for x in get_inputs(seq, kp_dir, kp_dir_moves))


def complexity(code, n):
    seqs = get_inputs(code, kp_num, kp_num_moves)
    min_len = min(min_length(seq, n) for seq in seqs)
    return min_len*int(code[:-1])


# Part 1
print(sum(complexity(code, 2) for code in codes))

# Part 2
print(sum(complexity(code, 25) for code in codes))