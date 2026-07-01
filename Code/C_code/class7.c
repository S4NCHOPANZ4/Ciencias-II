#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

# define MAX_NODES 10 


// Matriz de adj

typedef struct{
	int vertices;
	int adjacencyMatrix[MAX_NODES][MAX_NODES];
}Graph;


// Operations

void initGraph(Graph *g, int newNodes) {
	g->vertices = newNodes;
	for (int i = 0; i < newNodes; i++) {
		for (int j = 0; j < newNodes; j++) {
			g->adjacencyMatrix[i][j] = 0;
		}
	}
}

Graph createGraph(int nodes) {
	Graph g; 
	if (nodes > MAX_NODES) {
		puts("Cantidad de vertices superior a la permitida");
		exit(EXIT_FAILURE);
	}
	initGraph(&g , nodes);
	return g;
}

void addEdge(Graph *g, int source, int destination) {
	if (source == destination) {
		puts("Nigga wtf");
		return;
	}
	if (source < g->vertices && destination < g->vertices) {
		g->adjacencyMatrix[source][destination] = 1;
		g->adjacencyMatrix[destination][source] = 1;
	}
	else {
		puts("Nigga wtf our of range");
		return;
	}
}

bool hasEdge(Graph *g, int  source, int destination) {
	bool has = false;
	if (source < g->vertices && destination < g->vertices) {
		if (g->adjacencyMatrix[source][destination] == 1) {
			has = true;
		}
	}else{
		puts("Nigga wtf our of range");
		return;
	}
	return has;
}


int main() {
	int nodes;
	printf("Ingrese Cantidad de datos");
	scanf("%d", &nodes);
	Graph graph = createGraph(nodes);
	return 0;
}