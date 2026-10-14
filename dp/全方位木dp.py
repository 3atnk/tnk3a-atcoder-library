import sys
sys.setrecursionlimit(10**6)


def rerooting(graph, merge, e, add_vertex, add_edge, root=0):

    N = len(graph)

    parent = [-2] * N
    parent[root] = -1

    order = [root]

    for v in order:
        for u, edge in graph[v]:
            if u == parent[v]:
                continue

            parent[u] = v
            order.append(u)

    # 子 -> 親
    down = [None] * N

    for v in reversed(order):
        x = e()

        for u, edge in graph[v]:
            if u == parent[v]:
                continue

            x = merge(x,add_edge(down[u], edge, u, v))

        down[v] = add_vertex(x, v)

    # 親 -> 子
    up = [None] * N
    ans = [None] * N

    for v in order:
        deg = len(graph[v])
        vals = [None] * deg
        for i, (u, edge) in enumerate(graph[v]):
            if u == parent[v]:
                vals[i] = add_edge(up[v], edge, u, v)
            else:
                vals[i] = add_edge(down[u], edge, u, v)

        prefix = [e() for _ in range(deg + 1)]
        suffix = [e() for _ in range(deg + 1)]

        for i in range(deg):
            prefix[i + 1] = merge(prefix[i],vals[i])

        for i in range(deg - 1, -1, -1):
            suffix[i] = merge(vals[i],suffix[i + 1])

        ans[v] = add_vertex(prefix[deg], v)

        for i, (u, edge) in enumerate(graph[v]):
            if u == parent[v]:
                continue
            without_u = merge(prefix[i],suffix[i + 1])

            up[u] = add_vertex(without_u,v)
    return ans


N = int(input())
graph = [[] for _ in range(N)]


# =========================
# この問題固有のDP
# =========================

def e():
    return 0

def merge(a, b):
    return max(a, b)

def add_vertex(x, v):
    return x

def add_edge(x, cost, from_v, to_v):
    return x + cost

dp = rerooting(graph,merge,e,add_vertex,add_edge)

