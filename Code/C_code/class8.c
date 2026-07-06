#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

# define MAX_NODES 10 


// Matriz de adj

typedef struct {
	int vertices;
	int adjacencyMatrix[MAX_NODES][MAX_NODES];
}Graph;


// Operations

void initGraph(Graph* g, int newNodes) {
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
	initGraph(&g, nodes);
	return g;
}

void addEdge(Graph* g, int source, int destination) {
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

bool hasEdge(Graph* g, int  source, int destination) {
	bool has = false;
	if (source < g->vertices && destination < g->vertices) {
		if (g->adjacencyMatrix[source][destination] == 1) {
			has = true;
		}
	}
	else {
		puts("Nigga wtf our of range");
		return false;
	}
	return has;
}

void removeEdge(Graph* g, int  source, int destination) {
	if (hasEdge(g, source, destination)) {
		g->adjacencyMatrix[source][destination] = 0;
		g->adjacencyMatrix[destination][source] = 0;
	}
	else {
		puts("No se puede eliminar");
	}

}

void printMatrix(Graph* g) {
	printf("======Graph=====");
	printf("\t");
	for (int i = 0; i < g->vertices; i++) {
		printf("\t [%d]", i);
	}
	printf("\n");
	for (int i = 0; i < g->vertices; i++) {
		for (int j = 0; j < g->vertices; j++) {
			printf("%d", g->adjacencyMatrix[i][j]);
		}
		printf("\n");
	}

}

void  printIncidenceMatrix(Graph *g) {
	printf("======Incidence=====");
	int edgeCount = 0;

	for (int i = 0; i < g->vertices; i++) {
		for (int j = i; j < g->vertices; j++) {
			if (g->adjacencyMatrix[i][j] == 1) {
				edgeCount++;
			}
		}
	}
	if(edgeCount == 0) {
		return;
	}

	int incidenceMatrix[g->vertices][edgeCount];
	for (int i = 0; i < g->vertices; i++) {
		for (int j = i; j < edgeCount; j++) {
			if (g->adjacencyMatrix[i][j] == 1) {
				incidenceMatrix[i][j] = 0;
			}
		}
	}
	int edgeIndex = 0;
	for (int i = 0; i < g->vertices; i++) {
		for (int j = i; j < i; j++) {
			if (g->adjacencyMatrix[i][j] == 1) {
				incidenceMatrix[j][edgeIndex] = 1; // source
				incidenceMatrix[i][edgeIndex] = 1; // destination
			}
		}
	}
	printf("\t");
	for (int i = 0; i < edgeCount; i++) {
		printf("\t [%d]", i);
	}
	printf("\n");
	for (int i = 0; i < g->vertices; i++) {
		for (int j = 0; j < g->vertices; j++) {
			printf("%d", incidenceMatrix[i][j]);
		}
		printf("\n");
	}
}


int countEdges(Graph *g) {
	int edgeCount = 0;

	for (int i = 0; i < g->vertices; i++) {
		for (int j = i; j < g->vertices; j++) {
			if (g->adjacencyMatrix[i][j] == 1) {
				edgeCount++;
			}
		}
	}
	return edgeCount;
}
// Circuit sequencia de nodos que definen un camino
// Corte Separan el grafo en dos rafos 
// Ruta si existe ruta conecta o no conecta

void printCircuitMatrix(Graph* g) {
	printf("\n=====Print Circuit Matrix=====");
	int edgeCount = countEdges(g);

	if (edgeCount == 0) {
		return;
	}

	//relacion directa entre potenciales ciclos 
	int cycles = edgeCount - g->vertices;

	//mas vertices que aristas
	if (cycles <= 0) {
		printf("Not possible nigga");
		return;
	}
	int** circuit = (int**)malloc(cycles * sizeof(int*)); // Define Y axis
	for (int i = 0; i < cycles; i++) {
		circuit[i] = (int*)malloc(edgeCount * sizeof(int)); // Define X axis
	}

	for (int i = 0; i < cycles; i++) {
		for (int j = 0; j < edgeCount; j++) {
			circuit[i][j];
		}
	}

	// Circuits 
	int cycleIndex = 0;
	int edgeIndex;
	int edgList[edgeCount][2];


	for (int i = 0; i < g->vertices && edgeIndex < edgeCount; i++) {
		for (int j = 0; j < g->vertices && edgeIndex < edgeCount; j++) {
			if (g->adjacencyMatrix[i][j] == 1) {
				edgeList[edgeIndex][0] = i; // fuente
				edgeList[edgeIndex][1] = j; // Dest
			}
		}
	}
	for (int e = 0; e < edgeCount && cycleIndex < cycle; e++) {
		circut[cycleIndex][e] = 1;
		cycleIndex++;
	}

}


void printPathMatrix(Graph* g) {
	printf("\n=====Path Matrix=====");
	int pathMatrix[g->vertices][g->vertices];
	for (int i = 0; i < g->vertices; i++) {
		for (int j = 0; j < g->vertices; j++) {
			if (i == j) {
				pathMatrix[i][j] = 1;
			}
			else {
				pathMatrix[i][j] = g->adjacencyMatrix[i][j];
			}
			
		}
	}
	// Floyd Warshall
	for (int k = 0; k < g->vertices; k++) {
		for (int i = 0; i < g->vertices; i++) {
			for (int j = 0; i < g->vertices; j++) {
				if (pathMatrix[i][k] && pathMatrix[k][j]) {
					pathMatrix[i][j] = 1;
				
				}
			}
		}
	}


}
//Edge List

int getEdgeList(Graph* g) {
	int edgeCount = countEdges(g);
	int edgList[edgeCount][2];
	int edgeIndex = 0;
	for (int i = 0; i < g->vertices && edgeIndex < edgeCount; i++) {
		for (int j = 0; j < g->vertices && edgeIndex < edgeCount; j++) {
			if (g->adjacencyMatrix[i][j] == 1) {
				edgeList[edgeIndex][0] = i; // fuente
				edgeList[edgeIndex][1] = j; // Dest
			}
		}
	}
	
}

void printCutSetMatrix(Graph* g) {
	printf("\n=====Cut Matrix=====");
	int edgeCount = countEdges(g);
	if (edgeCount == 0) {
		printf("douhhh");
		return;
	}
	int cutsets = g->vertices - 1;
	int cutsetMatrix[cutsets][edgeCount];


	for (int i = 0; i < cutsets; i++) {
		for (int j = 0; j < edgeCount; j++) {
			cutsetMatrix[i][j] = 0;
		}
	}

	int edgeList = getEdgeList(g);
	for (int c = 0; c < cutsets; c++) {
		for (int e = 0; e < edgeCount; e++) {

		}
	}
}

int main() {
	int nodes;
	printf("Ingrese Cantidad de datos");
	scanf("%d", &nodes);
	Graph graph = createGraph(nodes);
	addEdge(&graph, 0, 1);
	addEdge(&graph, 1, 2);
	addEdge(&graph, 2, 1);
	printMatrix(&graph);
	printIncidenceMatrix(&graph);

	return 0;
}