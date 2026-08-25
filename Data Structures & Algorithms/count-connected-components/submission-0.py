class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        adj = {i : [] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()

        comp = 0
        

        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbour in adj[current]:
                    if neighbour not in visit:
                        visit.add(neighbour)
                        stack.append(neighbour)

            

        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                comp +=1
         
        return comp       


                


