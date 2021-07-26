class Graph():
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        #print(self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path=path + [start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        
        paths=[]

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return(paths)
        
    
    def get_shortest_path(self,start,end,path=[]):
        paths=self.get_paths(start,end,path)  
        min_len=1000
        i=0
        index=0        
        for p in paths:
            l=len(p)
            if l < min_len:
                min_len=l
                index=i
            i+=1
        return(paths[index])


if __name__=="__main__":
    routes=[
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto")
    ]

    route_graph=Graph(routes)
    start="Mumbai"
    end="New York"
    print(f"path between {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"shortest path between {start} and {end}: ",route_graph.get_shortest_path(start,end))
