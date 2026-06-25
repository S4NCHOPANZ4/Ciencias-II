#include <stdio.h>
#include <stdlib.h>

#define SLOTS 100003

struct Node {
    int data;
    struct Node* next;
};

struct Node** hashTable = NULL;
int tableSize = 0;
int different = 0; 

int hashFn(int key) {
    return key % SLOTS;
}

int search(int key) {
    int slot = hashFn(key);
    struct Node* temp = hashTable[slot];
    while (temp != NULL) {
        if (temp->data == key) {
            return slot; // Elemento encontrado
        }
        temp = temp->next;
    }
    return -1; // Elemento no encontrado
}

void insert(int key) {
    int slot = hashFn(key);
    
    // 2. Solo insertamos si realmente NO existe en la tabla
    if (search(key) == -1) {
        different += 1;
        
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = key;
        newNode->next = hashTable[slot]; 
        hashTable[slot] = newNode;
    }
}

int main() {
    int n; 
    if (scanf("%d", &n) != 1) return 0;

    tableSize = n;
    hashTable = (struct Node**)calloc(tableSize, sizeof(struct Node*));

    for (int i = 0; i < n; i++) {
        int val; 
        if (scanf("%d", &val) == 1) {
            insert(val); // Ya no le pasamos 'n'
        }
    }
    
    printf("%d\n", different);
    
    // El main debe retornar siempre 0 si terminó exitosamente
    return 0; 
}