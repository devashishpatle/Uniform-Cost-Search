import copy
def uniform_cost_search(graph, start, goal):
    path = []
    visited = [start]
    path_cost = 0
    if start == goal:
        return path, path_cost,visited
    path.append(start)
    
    openlist=[(path_cost,path)]
    while len(openlist)>0:
        currcost,currpath=openlist.pop(0)
        print('The current path is(popped openlist element)',currpath)
        currnode=currpath[-1]
        
        #check if current node is goal node
        if currnode==goal:
            return currpath, currcost, visited
        
        if currnode not in visited:
            visited.append(currnode)
        
        #expand children of current node
        neighbours=graph[currnode]
        
        #neighbours.sort() # if neighbours are to be entered in a sorted way
        print('The neighbours are',neighbours)
        for n in neighbours:
            #print('Iterations begin')
            #print('The node is',n)
            n_path_cost=currcost+n[0]
            #print('current path cost=',n_path_cost)
            n_path=copy.copy(currpath)
            n_path.append(n[1])
            #print('n_path after appending is ',n_path)
            
            n_openlist_ele=(n_path_cost, n_path)
            #print('Current open list element is', n_openlist_ele)
            if n[1] not in visited:
                openlist.append(n_openlist_ele)
                openlist.sort()
                print('***Current Open list after appending',openlist)
            
            print('')
            
    return path, n_path_cost, visited
    
# defining graph and calling uniform cost function
#graph3={'a':[(6,'b'),(3,'c')],'b':[(2,'d'),(1,'c')],'c':[(4,'b'),(8,'d'),(2,'e')],'d':[(9,'e')],'e':[(7,'d')]}
graph3={'s':[(1,'a'),(12,'g')],'a':[(3,'b'),(1,'c')],'c':[(1,'d')],'d':[(3,'g')],'b':[(3,'d')]}

#p,c,v=uniform_cost_search(graph3, 'a','d')
p,c,v=uniform_cost_search(graph3, 's','g')
print('From main')
print('The path is:',p)
print('The path cost is',c)
print('The visited nodes are',v)
