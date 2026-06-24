#include <stdio.h>
#include <stdlib.h>

#define SLOTS 10;

typedef struct Node{
    int data;
    struct Node* next;
}Node;

Node* hashTable[];

int hashFn(int key){
    int slot = key % SLOTS;
    return slot;
}

void insert(int key){
    int slot = hashFn(key);
    Node* newNode = (Node*)malloc((sizeof(Node)));
    newNode->data = key;
    newNode->next = hashTable[slot];
    hashTable[slot] = newNode;
}

int search(int key){
    int slot = hashFn(key);
    Node* temp = hashTable[slot];
    while(temp != NULL){
        if(temp->data == key){
            return slot;
        }
        temp = temp->next;
    }
    return -1;
}

void delete(int key){
    int slot = hashFn(key);
    if(search(key) == -1) {
        printf("element %d not found", key);
        return;
    }
    Node* temp = hashTable[slot];
    Node* prev = NULL;
    
    while(temp != NULL){
        if(temp->data == key){
            if(prev == NULL){
                hashTable[slot] = temp->next;
            }
            else{
                prev->next = temp->next;
            }
            prev = temp;
            temp = temp->next;
        }
    }
}

int main(){
    return 0;

}