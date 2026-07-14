#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_NODES 10 

// Matriz de adj
typedef struct {
	int vertices;
	int adjacencyMatrix[MAX_NODES][MAX_NODES];
} Graph;

// Operations
void initGraph(Graph* g, int newNodes) {
	if (g == NULL) return;
	g->vertices = newNodes;
	for (int i = 0; i < newNodes; i++) {
		for (int j = 0; j < newNodes; j++) {
			g->adjacencyMatrix[i][j] = 0;
		}
	}
}

Graph createGraph(int nodes) {
	Graph g;
	g.vertices = 0;
	if (nodes > MAX_NODES || nodes <= 0) {
		puts("Cantidad de vertices invalida o superior a la permitida");
		exit(EXIT_FAILURE);
	}
	initGraph(&g, nodes);
	return g;
}

void addEdge(Graph* g, int source, int destination) {
	if (g == NULL) return;
	if (source == destination) {
		puts("Error: No se permiten bucles (source == destination)");
		return;
	}
	if (source >= 0 && source < g->vertices && destination >= 0 && destination < g->vertices) {
		g->adjacencyMatrix[source][destination] = 1;
		g->adjacencyMatrix[destination][source] = 1;
	}
	else {
		puts("Error: Vertices fuera de rango");
		return;
	}
}

bool hasEdge(Graph* g, int source, int destination) {
	if (g == NULL) return false;
	if (source >= 0 && source < g->vertices && destination >= 0 && destination < g->vertices) {
		if (g->adjacencyMatrix[source][destination] == 1) {
			return true;
		}
	}
	else {
		puts("Error: Vertices fuera de rango");
		return false;
	}
	return false;
}

void removeEdge(Graph* g, int source, int destination) {
	if (g == NULL) return;
	if (hasEdge(g, source, destination)) {
		g->adjacencyMatrix[source][destination] = 0;
		g->adjacencyMatrix[destination][source] = 0;
	}
	else {
		puts("No se puede eliminar: arista inexistente");
	}
}

void printMatrix(Graph* g) {
	if (g == NULL) return;
	printf("\n====== Graph Adjacency Matrix =====\n");
	printf("Nodes:\t");
	for (int i = 0; i < g->vertices; i++) {
		printf("[%d]\t", i);
	}
	printf("\n");
	for (int i = 0; i < g->vertices; i++) {
		printf("[%d]\t", i);
		for (int j = 0; j < g->vertices; j++) {
			printf(" %d \t", g->adjacencyMatrix[i][j]);
		}
		printf("\n");
	}
}

int countEdges(Graph *g) {
	if (g == NULL) return 0;
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

void printIncidenceMatrix(Graph *g) {
	if (g == NULL) return;
	printf("\n====== Incidence Matrix =====\n");
	int edgeCount = countEdges(g);

	if (edgeCount == 0) {
		printf("Grafo sin aristas.\n");
		return;
	}

	// Inicializacion de matriz dinámica basada en V x E
	int** incidenceMatrix = (int**)malloc(g->vertices * sizeof(int*));
	for (int i = 0; i < g->vertices; i++) {
		incidenceMatrix[i] = (int*)malloc(edgeCount * sizeof(int));
		for (int j = 0; j < edgeCount; j++) {
			incidenceMatrix[i][j] = 0;
		}
	}

	// Mapeo correcto de aristas unicas a columnas de incidencia
	int edgeIndex = 0;
	for (int i = 0; i < g->vertices; i++) {
		for (int j = i + 1; j < g->vertices; j++) {
			if (g->adjacencyMatrix[i][j] == 1 && edgeIndex < edgeCount) {
				incidenceMatrix[i][edgeIndex] = 1; // source / vertex 1
				incidenceMatrix[j][edgeIndex] = 1; // destination / vertex 2
				edgeIndex++;
			}
		}
	}

	// Impresion estilizada de cabeceras
	printf("Edges:\t");
	for (int i = 0; i < edgeCount; i++) {
		printf("e[%d]\t", i);
	}
	printf("\n");

	for (int i = 0; i < g->vertices; i++) {
		printf("[%d]\t", i);
		for (int j = 0; j < edgeCount; j++) {
			printf(" %d \t", incidenceMatrix[i][j]);
		}
		printf("\n");
	}

	// Liberacion de memoria dinamica
	for (int i = 0; i < g->vertices; i++) {
		free(incidenceMatrix[i]);
	}
	free(incidenceMatrix);
}

void printCircuitMatrix(Graph* g) {
	if (g == NULL) return;
	printf("\n===== Print Circuit Matrix =====");
	int edgeCount = countEdges(g);

	if (edgeCount == 0) {
		printf("\nGrafo sin aristas.\n");
		return;
	}

	// Relacion fundamental de ciclos fundamentales (E - V + componentes_conexas)
	int cycles = edgeCount - g->vertices + 1;

	if (cycles <= 0) {
		printf("\nNo fundamental circuits possible (Tree or Forest structure).\n");
		return;
	}

	int** circuit = (int**)malloc(cycles * sizeof(int*)); 
	for (int i = 0; i < cycles; i++) {
		circuit[i] = (int*)malloc(edgeCount * sizeof(int)); 
		for (int j = 0; j < edgeCount; j++) {
			circuit[i][j] = 0;
		}
	}

	int edgeIndex = 0;
	int edgeList[MAX_NODES * MAX_NODES][2];
	
	// Inicializacion preventiva del arreglo bidimensional
	for (int i = 0; i < (MAX_NODES * MAX_NODES); i++) {
		edgeList[i][0] = 0;
		edgeList[i][1] = 0;
	}

	for (int i = 0; i < g->vertices; i++) {
		for (int j = i + 1; j < g->vertices; j++) {
			if (g->adjacencyMatrix[i][j] == 1 && edgeIndex < edgeCount) {
				edgeList[edgeIndex][0] = i; 
				edgeList[edgeIndex][1] = j; 
				edgeIndex++;
			}
		}
	}

	// TODO: Implementar algoritmo para identificar los ciclos fundamentales del grafo
	// e indexarlos sobre las filas de la matriz 'circuit'.
	// Ejemplo de esquema de recorrido básico provisto en diseño original:
	int cycleIndex = 0;
	for (int e = 0; e < edgeCount && cycleIndex < cycles; e++) {
		circuit[cycleIndex][e] = 1;
		cycleIndex++;
	}

	// TODO: Agregar el bloque de visualizacion formateado para 'circuit' y liberar la memoria dinamica de forma segura.
}

void printPathMatrix(Graph* g) {
	if (g == NULL) return;
	printf("\n===== Path Matrix (Clausura Transitiva) =====\n");
	
	int** pathMatrix = (int**)malloc(g->vertices * sizeof(int*));
	for (int i = 0; i < g->vertices; i++) {
		pathMatrix[i] = (int*)malloc(g->vertices * sizeof(int));
		for (int j = 0; j < g->vertices; j++) {
			if (i == j) {
				pathMatrix[i][j] = 1;
			} else {
				pathMatrix[i][j] = g->adjacencyMatrix[i][j];
			}
		}
	}

	// Floyd Warshall - Corrección del bucle interno (j < g->vertices)
	for (int k = 0; k < g->vertices; k++) {
		for (int i = 0; i < g->vertices; i++) {
			for (int j = 0; j < g->vertices; j++) {
				if (pathMatrix[i][k] == 1 && pathMatrix[k][j] == 1) {
					pathMatrix[i][j] = 1;
				}
			}
		}
	}

	// Impresion de Matriz de Caminos
	printf("Nodes:\t");
	for (int i = 0; i < g->vertices; i++) {
		printf("[%d]\t", i);
	}
	printf("\n");
	for (int i = 0; i < g->vertices; i++) {
		printf("[%d]\t", i);
		for (int j = 0; j < g->vertices; j++) {
			printf(" %d \t", pathMatrix[i][j]);
		}
		printf("\n");
	}

	for (int i = 0; i < g->vertices; i++) {
		free(pathMatrix[i]);
	}
	free(pathMatrix);
}

// Edge List - Retorna la cuenta y llena una matriz externa simulando el comportamiento diseñado
int getEdgeList(Graph* g) {
	if (g == NULL) return 0;
	int edgeCount = countEdges(g);
	int edgeList[MAX_NODES * MAX_NODES][2];
	int edgeIndex = 0;

	for (int i = 0; i < g->vertices; i++) {
		for (int j = i + 1; j < g->vertices; j++) {
			if (g->adjacencyMatrix[i][j] == 1 && edgeIndex < edgeCount) {
				edgeList[edgeIndex][0] = i; 
				edgeList[edgeIndex][1] = j; 
				edgeIndex++;
			}
		}
	}
	return edgeCount;
}

void printCutSetMatrix(Graph* g) {
	if (g == NULL) return;
	printf("\n===== Cut Matrix =====");
	int edgeCount = countEdges(g);
	if (edgeCount == 0) {
		printf("\nGrafo vacio sin conjuntos de corte disponibles.\n");
		return;
	}
	
	int cutsets = g->vertices - 1;
	
	// Creación segura de matriz estática local o dinámica indexada
	int cutsetMatrix[MAX_NODES][MAX_NODES * MAX_NODES];

	for (int i = 0; i < cutsets; i++) {
		for (int j = 0; j < edgeCount; j++) {
			cutsetMatrix[i][j] = 0;
		}
	}

	// Conservación del flujo de diseño original
	int edgeListCount = getEdgeList(g);
	(void)edgeListCount; // Evita warnings de variable no usada

	// TODO: Implementar la logica de busqueda de subgrafos de corte (Cut-Sets fundamentales)
	// relacionando los cortes de aristas con las columnas de 'cutsetMatrix'.
	for (int c = 0; c < cutsets; c++) {
		for (int e = 0; e < edgeCount; e++) {
			// Lógica pendiente de desarrollo por diseño
		}
	}
	
	// TODO: Agregar el formateado de impresion de columnas de aristas vs filas de cortes.
}

int main() {
	int nodes = 0;
	printf("Ingrese Cantidad de datos: ");
	if (scanf("%d", &nodes) != 1) {
		puts("Error al leer la entrada.");
		return EXIT_FAILURE;
	}
	
	Graph graph = createGraph(nodes);
	
	// Caso de prueba controlado para evitar desbordamientos
	if (nodes >= 3) {
		addEdge(&graph, 0, 1);
		addEdge(&graph, 1, 2);
		addEdge(&graph, 2, 0); 
	} else if (nodes == 2) {
		addEdge(&graph, 0, 1);
	}

	printMatrix(&graph);
	printIncidenceMatrix(&graph);
	printPathMatrix(&graph);
	printCircuitMatrix(&graph);
	printCutSetMatrix(&graph);

	return 0;
}