#include <stdio.h>
#define SLOTS 10

// Class 2 - Hashing 

int hashTable[SLOTS][5];

void init() {
	for (int i = 0; i < SLOTS; i++) {
		for (int j = 0; j < 5; j++) {
			hashTable[i][j] = -1;
		}
	}
}

int hash_fn(int key) {
	int slot = key % SLOTS; // change this line for another function
	return slot;
}

void insert(int key) {
	int slot = hash_fn(key);
	for (int i = 0; i < 5; i++) {
		if (hashTable[slot][0] != -1) {
			hashTable[slot][0] = key;
			break;
		}
	}
}

int search(int key) {
	int slot = hash_fn(key);
	for (int i = 0; i < 5; i++) {
		if (hashTable[key] == -1) {
			return -1;
		}
		else {
			if (hashTable[slot][i] == key) {
				return slot;
			}
		}
	}
	
}

void printTable(){
	for (int i = 0; i < SLOTS; i++) {
		printf("Slot [%d] \n", i);
		for (int j = 0; j < 5; j++) {

			printf("element [%d] -> %d \n", j, hashTable[i][j]);
		}
	}
}

int main() {
	init();
	insert(234);
	insert(543);
	insert(1);
	printTable();
	printf("print for 3 is %d", search(3));
	return 0;
}

