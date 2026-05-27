import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMapActors = {}
        for a in DAO.getAllActors():
            self._idMapActors[a.id] = a

    def getAllVoti(self):
        return DAO.getRatings

    def buildGraph(self, r1, r2):
        self._graph.clear()
        attori = DAO.getActor(r1, r2)


        self._graph.add_nodes_from(attori)
        collegamenti = DAO.getCollegamenti()

        for id1, id2, income in collegamenti:
            if self.hasNode(id1) and self.hasNode(id2):
                u = self.getNode(id1)
                v = self.getNode(id2)
                #print((self.hasEdge(v,u)))
                if income[0]=='$':
                    income=income[2:]
                    if self.hasEdge(u, v) or self.hasEdge(v, u):
                        self._graph[u][v]["weight"] += income

                    else:
                        self._graph.add_edge(u,v,weight=income)

    def hasNode(self, id1):
        return self._graph.has_node(self._idMapActors[id1])

    def getNode(self, id1):
        return self._idMapActors[id1]

    def hasEdge(self, u, v):
        return self._graph.has_edge(u, v)

    def getNodiArchi(self):
        return len(self._graph.nodes), len(self._graph.edges)


