#include "selfstudy_1.h"
#include <stdio.h>
/*
 #include <string.h>
 libreria para manipular caenas de caracteres y bloques de memoria
 strlen(cadena) longitud de una cadena
 strcpy(dest,orig) copia de una cadena
 srtcat(dest, orig) concatena candenas
 strcmp(a,b) compara cadenas
*/
#include <string.h> 
/*
 #include <stdlib.h>
 Contiene funciones generales del sistema, conversion de datos y gestion dinamica de memoria
 malloc() reserva memoria dinamica
 calloc() reserva memoria e inicializa en cero
 realloc() redimensiona memoria
 free() lonera memoria

 atoi() convierte texto a entero
 atof() convierte texto a float

 rand() genera numeros aleatorios
 srand() inicializa una semilla
 exit() termina el programa

*/
#include <stdlib.h> 

/*
 #define es una directiva de preprocesador de C. sirve para crear una sustitucion de texto antes de que
 el compilador procese el programa.
*/

#define SIZE 10

/*
struct Node define un tipo de estructura llamado Node (como una plantilla)
typedef significa "type definition". Sirve para darle un nombre nuevo a un tipo existente.
	Sin typedef: cada vez que quiera definir un Nodo nuevo: struct Node n1;
	Con typedef: Node n1;
*/

/*
	struct Node* next;
	Es un puntero al siguiente nodo no almacena al nodo solo una direccion a la
	posicion de memoria en la que se encuentra al Nodo.
*/

/*
	char key[50];
	Al escribir char key[50], le estamos diciendo a C "Reserva automaticamente un
	espacio de 50 bytes para guardar texto dentro de cada nodo"
 */

typedef struct Node {
	char key[50];
	int data;
	struct Node* next;
}Node;


/*
	Estamos creando un arreglo de SIZE cantidad de elementos que son punteros
	"Es un arreglo de 1000 punteros a nodos"
*/
Node* hashTable[SIZE] = { NULL };


/*
	Con char* estamos tomando la direccion de memoria a la primera letra del string
*/
int hashFunction(char* key) {
	int sum = 0;  // variable para acumular la suma de todos los caracteres
	for (int i = 0; key[i] != '\0'; i++) { // ciclo en el que vamos a recorrer la cadena caracter por caracter
		//  '\0' indica un caracter con valor nulo (final de la cadena)
		sum += key[i];  // sumamos el valor ASCII de cada caracter
	}
	return sum % SIZE; // Devuelve el residuo al dividir por SIZE, nos asegura un indice entre 0 y 9 (de esta manera tenemos una tabla con 10 "slots")
}


void insert(char* key, int value) {
	int index = hashFunction(key); // Indica la posicion en la que ha de ser agregado un dato 

	/*
	sizeof(Node) nos indica cuantos bytes ocupa un Node
	malloc(...) Reserva memoria dinamicamente, osea pide espacio para un nodo
	(Node*) Convierte el resultado de malloc en un puntero asignado a newNode
	*/

	Node* newNode = (Node*)malloc(sizeof(Node));

	/*
		strcpy(...) copia la cadena recibida al nodo
		si key = "Torres"
		entonces
		newNode->key = "Torres"
	*/
	strcpy(newNode->key, key);

	newNode->data = value; // se le asigna a newNode.data el valor de value

	/*
	se le asigna como valor next al elemento ya presenta en la hashtable de no tener ninguno se asigna un NULL
	*/
	newNode->next = hashTable[index];
	hashTable[index] = newNode; // se asgina el newNode a su respectiva posicion en la hashTable

}

int search(char* key) {
	int index = hashFunction(key); // nos retorna el indice extacto donde debe de estar en la hashtable. 
	Node* temp = hashTable[index]; //valor temporal por si este elemento no es el buscado dado [] -> [objetivo] -> []

	while (temp != NULL) {
		/*
			strcmp() compara dos strings
			0 si son iguales
			< 0 (negativo) si a es menor que b alfabeticamente
			> 0 (positivo) si a es mayor que b alfabeticamente
		*/
		if (strcmp(temp->key, key) == 0) {
			return temp->data;
		}
		temp = temp->next; // seguir recorriendo la linked list.
	}
	return -1;
}

int binarySearch(int data[], int x, int size) {
	int bottom = 0;
	int top = size - 1;

	while (bottom <= top) {
		int middle = (bottom + top) / 2;
		if (data[middle] == x) {
			return middle;
		}
		else if (x > data[middle]) {
			bottom = middle + 1;
		}
		else {
			top = middle - 1;
		}
	}
	return -1;
}

void  execSS1() {
	int data[] = { 1,2,3,4,5,6 };
	int longitud = sizeof(data) / sizeof(data[0]);
	printf("The result is: %d", binarySearch(data, 3, longitud));

	//insert("Juan", 30);
	//insert("Maria", 25);
	//insert("Pedro", 40);

	//char personaBuscar[50] = "Maria";
	//int edad = search(personaBuscar);

}