#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    int rep;
    struct Node* next;
};

struct Node** hashTable = NULL;
int tableSize;
int count = 0;

int hashFn(int key){
    int slot = key % tableSize;
    return slot;
}

int search(int key){
    int slot = hashFn(key);
    struct Node* temp = hashTable[slot];
    while(temp != NULL){
        if(temp->data == key){
            return slot;
        }
        temp = temp->next;
    } 
    return -1;
}

int insert(int key){
    int slot = hashFn(key);
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->rep = 1;
    if(search(key) != -1){
        newNode->rep = newNode->rep + 1;
        if (newNode->rep == 2){
            return key;
        }
    }

    newNode->data = key;
    newNode->next = hashTable[slot]; 
    hashTable[slot] = newNode;
    return -1;
}

int searchRep(int key){
    int slot = hashFn(key);
    struct Node* temp = hashTable[slot];
    while(temp != NULL){
        if(temp->rep == 2){
            return key;
        }
        temp = temp->next;
    } 
    return -1;

}


int main(){

    int n;
    scanf("%d", &n);

    tableSize = n;
    hashTable = (struct Node**)calloc(tableSize, sizeof(struct Node*));

    for(int i = 0; i < n; i++){
        int val;
        scanf("%d", &val);
        if(insert(val) != -1){
            printf("%d",val);
            return val;
        }
    }

    printf("%d",-1);
    return -1;
}