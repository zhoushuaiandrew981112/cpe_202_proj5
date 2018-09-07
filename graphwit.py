# Name:          Zhoushuai(Andrew) Wu
# Course:        CPE 202
# Instructor:    Daniel Kauffman
# Assignment:    Proj 5: Graph Wit
# Term:          Summer 2018

#from queue import *
import queue
import re

#adj_list = {"v0" : [("v1", 1), ("v2", 2), ("v3", 3), ...], "v2" : [("v1", 1), ("v2", 2), ...], ...}


def get_patterns():
    regex = r"[^A-Z]*([A-Z])[A-Z]*[^A-Z\d]*(\d*)(<?(?:-{1,2}|={1,2})>?)?(\d*)[^A-Z\d]*[A-Z]*([A-Z])[^A-Z]*"
    r = re.compile(regex, re.I)
    return [r]


def parse_edges(patterns, strings, i_2 = 2, i_3 = 3, i_4 = 4):
    adj_lst = {}
    for s in strings:
        m = re.search(patterns[0], s)
        if m != None:
            g_lst = m.groups()
            if g_lst[0] != None and g_lst[i_4] != None and \
                g_lst[i_2] != None and g_lst[i_2] != None:
                a, b, l, r = g_lst[0], g_lst[i_4], g_lst[i_2][0], g_lst[i_2][-1]
                wba = 1 if g_lst[1] == "" else int(g_lst[1])
                wab = 1 if g_lst[i_3] == "" else int(g_lst[i_3])
                if a != "" or b != "":
                    if a not in adj_lst: adj_lst[a] = [] 
                    if b not in adj_lst: adj_lst[b] = []
                    if l != "<" and r == ">" : adj_lst[a].append((b, wab)) 
                    elif l == "<" and r != ">" : adj_lst[b].append((a, wba)) 
                    else:
                        adj_lst[a].append((b, wab)) 
                        adj_lst[b].append((a, wba))
    return adj_lst


def order_bfs(adj_list, start_vertex):
    q = queue.Queue()
    result = []
    q.put(start_vertex)
    result.append(start_vertex)
    while not q.empty():
        v = q.get()
        for tup in adj_list[v]:
            if not (tup[0] in result):
                q.put(tup[0])
                result.append(tup[0])
    return result
        

def order_dfs(adj_list, start_vertex):
    q = queue.LifoQueue()
    result = []
    q.put(start_vertex)
    q.put(start_vertex)
    result.append(start_vertex)
    while not q.empty():
        v = q.get()
        if v not in result:
            result.append(v)
        for tup in adj_list[v]:
            if tup[0] not in result:
                q.put(tup[0])
                break
    return result



#r = get_patterns()
#m = re.search(r[0], "!@#aAaAxyz+*3<-->/!qwertyb{zzZZ}&&")
#lst = m.groups()
#print(lst)
