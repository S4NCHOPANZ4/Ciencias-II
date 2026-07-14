#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_NODES 10

typedef struct {
    int vertices; 
    int adjacencyMatrix[MAX_NODES][MAX_NODES];
} Graph;

void initGraph(Graph* g, int newNode){
    if(g == NULL) return;
    g->vertices = newNode;
    for (int i = 0; i < newNode; i++){
        for(int j = 0;j< newNode; j++){
            g->adjacencyMatrix[i][j] = 0;
        }
    }
}

Graph createGraph(int nodes){
    Graph g; 
    if (nodes > MAX_NODES || nodes <= 0){
        puts("Cantidad de vertices invalida");
        exit(EXIT_FAILURE);
    } 
    initGraph(&g, nodes);
    return g;
}

void addEdge(Graph* g, int source, int destination){
    if(g == NULL) return;
    if(source == destination){
        puts("Error. no se permiten bucles");
        return;
    }
    if(source >= 0 && source < g -> vertices && destination >= 0 && destination < g-> vertices){
        g->adjacencyMatrix[source][destination] = 1;
        g->adjacencyMatrix[destination][source] = 1;
    }
    else {
        puts("Error. Verices fuera de range");
        return;
    }
}

bool hasEdge(Graph* g, int source, int destination){
    if(g==NULL) return false;
    if(source >= 0 && source < g->vertices && destination){
        if(g->adjacencyMatrix[source][destination] == 1){
            return true;
        }
    }else{
        puts("Error. Vertices fuera de range");
        return false;
    }
    return false;
}

void removeEdge(Graph *g, int source, int destinaton){
    if(g==NULL) return;
    if(hasEdge(g, source, destinaton)){
        g->adjacencyMatrix[source][destinaton]= 0;
        g->adjacencyMatrix[destinaton][source]= 0;
    }
    else{
        puts("Error. edge not found. nothing to delete");
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

int countEdges(Graph *g){
    if(g == NULL)return;
    int edgeCount = 0;
    for(int i =0; i< g->vertices; i++){
        for(int j=0; j <g->vertices; j++){
            if(g->adjacencyMatrix[i][j]==1){
                edgeCount++;
            }
        }
    }
    return edgeCount;
}

void printIncidenceMatrix (Graph *g){
    if(g ==NULL) return;
	printf("\n====== Incidence Matrix =====\n");
    int edgeCount = countEdges(g);

    if(edgeCount == 0){
        put("No edges were found");
        return;
    }

    int** incidenceMatrix = (int**)malloc(g->vertices * sizeof(int));
    for(int i=0; i<g->vertices;i++){
        incidenceMatrix[i] = (int*)malloc(edgeCount * sizeof(int));
        for(int j = 0; j<edgeCount; j++){
            incidenceMatrix[i][j] = 0;
        }
    }

    int edgeIndex = 0;
    for(int i =0; i < g->vertices; i++){
        for(int j =0; j < g->vertices; j++){
            if(g->adjacencyMatrix[i][j] == 1 && edgeIndex < edgeCount){
                incidenceMatrix[i][edgeIndex] = 1;
                incidenceMatrix[j][edgeIndex] = 1;
                edgeIndex++;
            }

        }
    }
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

	for (int i = 0; i < g->vertices; i++) {
		free(incidenceMatrix[i]);
	}
	free(incidenceMatrix);
}

void printCircuitMatrix(Graph *g){
    if(g == NULL) return;
	printf("\n===== Print Circuit Matrix =====");
    int edgeCount = countEdges(g);

    if(edgeCount == 0){
		printf("\nGrafo sin aristas.\n");
		return;
    }
    int cycles = edgeCount - g->vertices+1; 

    if(cycles <= 0){
	    printf("\nNo fundamental circuits possible (Tree or Forest structure).\n");
        return;
    }
    int** circuit = (int**)malloc(cycles * sizeof(int*));
    for(int i = 0; i<cycles; i++){
        circuit[i] =(int*)malloc(edgeCount * sizeof(int));
        for(int j = 0; j < edgeCount; j++){
            circuit[i][j] = 0;
        }
    }

    int edgeIndex = 0;
    int edgeList[MAX_NODES * MAX_NODES][2];

    for(int i = 0; i<g->vertices; i++){
        for(int j=i+1; j<g->vertices; j++){
            if(g->adjacencyMatrix[i][j] == 1 && edgeIndex < edgeCount){
                edgeList[edgeIndex][0] = i;
                edgeList[edgeIndex][1] = j;
                edgeIndex++;
            }
        }
    }

}


void printPathMatrix(Graph *g){
    if(g == NULL) return;
	printf("\n===== Path Matrix (Clausura Transitiva) =====\n");

    int** pathMatrix = (int**)malloc(g->vertices * sizeof(int*));
    for(int i = 0; i < g->vertices; i++){
        pathMatrix[i] = (int*)malloc(g->vertices * sizeof(int));
        for(int j = 0; j < g->vertices; j++){
            if(i ==j){
                pathMatrix[i][j] = 1;
            } else{
                pathMatrix[i][j] = g->adjacencyMatrix[i][j];
            }
        }
    }
    // Floyd Warshall 
    for(int k = 0; k < g->vertices; k++){
        for(int i = 0; i < g->vertices; i++){
            for(int j =0; j< g->vertices; j++){
                if(pathMatrix[i][k] == 1 && pathMatrix[k][j] == 1){
                    pathMatrix =1;
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


int getEdgeList(Graph *g){
    if (g==NULL) return 0;
    int edgeCount = countEdges(g);
    int edgeList[MAX_NODES * MAX_NODES][2];
    int edgeIndex = 0;

    for(int i = 0; i < g->vertices; i++){
        for(int j = 0; j< g->vertices; j++){
            if(g->adjacencyMatrix[i][j] == 1 && edgeIndex < edgeCount){
                edgeList[edgeIndex][0]= i;
                edgeList[edgeIndex][1]= j;
                edgeIndex++;
            }
        }
    }
    return edgeCount;
}


