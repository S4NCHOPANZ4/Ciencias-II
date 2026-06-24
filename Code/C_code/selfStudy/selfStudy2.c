#include <stdio.h>
#include <stdlib.h>

#define SLOTS 10

struct Node {
	struct Node* next;
	int data;
};

struct Node* hashTable[SLOTS];


int hashFn(int key) {
	int slot = key % SLOTS;
	return slot;
}


void insert(int key) {
	int slot = hashFn(key);
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = key;
	newNode->next = hashTable[slot];
	hashTable[slot] = newNode;
}

void print() {
	for (int i = 0; i < SLOTS; i++) {
		printf("\nLista #[%d]", i);
		struct Node* temp = hashTable[i];
		while (temp != NULL) {
			printf("\nValue [%d]", temp->data);
			temp = temp->next;
		}
	}
}

int main() {

	insert(25);
	insert(15);
	insert(7);
	
	print();
	return 0;
}