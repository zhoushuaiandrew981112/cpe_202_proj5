# Name:          Zhoushuai(Andrew) Wu
# Course:        CPE 202
# Instructor:    Daniel Kauffman
# Assignment:    Proj 5: Graph Wit
# Term:          Summer 2018

#from queue import *
import queue

#adj_list = {"v0" : [("v1", 1), ("v2", 2), ("v3", 3), ...], "v2" : [("v1", 1), ("v2", 2), ...], ...}


def get_paterns():
#    result = []





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
