#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_NODES 10

typedef struct {
	int node; 
	int adjMatrix[MAX_NODES][MAX_NODES];
}Graph;


void initGraph(Graph *g, int newNodes) {
	g->node = newNodes;
	for (int i = 0; i < newNodes; i++) {
		for (int j = 0; j < newNodes; j++) {
			g->adjMatrix[i][j] = 0;
		}
	}
}

Graph createGraph(int newNodes) {
	Graph g;
	if (newNodes > MAX_NODES) exit(EXIT_SUCCESS);
	initGraph(&g, newNodes);
	return g;
}

void addEdge(Graph *g, int source, int destination) {
	if (source == destination){
		return;
	}
	if (source < g->node && source >= 0 && destination < g->node && destination >= 0) {
		g->adjMatrix[source][destination] = 1;
		g->adjMatrix[destination][source] = 1;
	}
}

bool hasEdge(Graph *g, int source, int destination) {
	bool has = false;
	if (source < g->node && source >= 0 && destination < g->node && destination >= 0) {
		if (g->adjMatrix[source][destination] == 1 && g->adjMatrix[destination][source] == 1) {
			has = true;
		}
	}
	return has;
}

void deleteNode(Graph *g, int source, int destination) {
	bool exists = hasEdge(g, source, destination);
	if (exists) {
		g->adjMatrix[source][destination] = 0;
		g->adjMatrix[destination][source] = 0;
	}

}

int countEdges(Graph *g) {
	int edges = 0;
	for (int i = 0; i < g->node; i++) {
		for (int j = i; j < g->node; j++) {
			if (g->adjMatrix[i][j] == 1) {
				edges++;
			}
		}
	}
	return edges;
}
//Edge List

int createEdgeList(Graph *g, int edgeList[][2]){
    int edge = 0;
    for(int i = 0; i < g->node; i++){
        for(int j=i+1; j < g->node; j++){
            if(g->adjMatrix[i][j]){
                edgeList[edge][0] = i;
                edgeList[edge][1] = j;
                edge++;
                
            }
        }
    }
    return edge;
}


void printIncidenceMatrix(Graph *g) {
	int edges = countEdges(g);
	if (edges == 0){
		return;
	}
	int incidenceMatrix[g->node][edges];
    for(int i = 0; i < g->node; i++){
        for(int j = 0; j < edges; j++){
            incidenceMatrix[i][j] = 0;
        }
    }
    int edge = 0;
    for (int i = 0; i < g->node; i++) {
        for (int j = i + 1; j < g->node; j++) {
            if (g->adjMatrix[i][j]) {
                incidenceMatrix[i][edge] = 1;
                incidenceMatrix[j][edge] = 1;
                edge++;
            }
        }
    }
	printf("=====Incidence Matrix=====\n");
    printf("  ");
    for (int j = 0; j < edges; j++)
        printf("e%d ", j);
    printf("\n");
    for(int i = 0; i < g->node; i++){
        printf("v[%d]", i);
        for(int j = 0; j < edges; j++){
            printf("%d ", incidenceMatrix[i][j]);
        }
        printf("\n");
    }

}

void printPathMatrix(Graph* g){
    int pathMatrix[g->node][g->node];
    for(int i = 0; i < g->node; i++){
        for(int j = 0; j < g->node; j++){
            if(i == j){
                pathMatrix[i][j] = 1;
            }else{
                pathMatrix[i][j] = g->adjMatrix[i][j];
            }
        }
    }
    // Floyd-Warshall 
    for(int k = 0; k < g->node; k++){
        for(int i = 0; i < g->node; i++){
            for(int j = 0; j < g->node; j++){
                if(pathMatrix[i][k] && pathMatrix[k][j]){
                    pathMatrix[i][j] = 1;
                }
            }
        }
    }
    printf("=====Path Matrix=====\n");
    printf("  ");
    for (int j = 0; j < g->node; j++)
        printf("e%d ", j);
    printf("\n");
    for(int i = 0; i < g->node; i++){
        printf("v[%d]", i);
        for(int j = 0; j < g->node; j++){
            printf("%d ", pathMatrix[i][j]);
        }
        printf("\n");
    }

}

void printCircuitMAtrix(Graph *g){
    int edges = countEdges(g);
    if(edges == 0){
        return;
    }
    int edgeList[edges][2];
    createEdgeList(g, edgeList);
    for(int i = 0; i < edges; i++){
        printf();

    }

    
}


int main() {
    printf("Inicio del programa\n");
    Graph graph = createGraph(3);
    addEdge(&graph,1,2);
    addEdge(&graph,0,1);
    addEdge(&graph,0,2);
    printIncidenceMatrix(&graph);
    printPathMatrix(&graph);
	return 0;
}