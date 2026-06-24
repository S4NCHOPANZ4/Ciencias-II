#include <stdio.h>
#include <stdlib.h>

#define SLOTS 10

struct Node{
    int data;
    struct Node* next;
};

struct Node* hashmap[SLOTS];

int hashfn(int key){
    int slot = key % SLOTS;
    return slot;
}

void insert(int key){
    int slot  = hashfn(key);
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = key;
    newNode->next = hashmap[slot];
    hashmap[slot] = newNode;
}

int search(int key){
    int slot  = hashfn(key);
    struct Node* temp = hashmap[slot];
    while(temp != NULL){
        if(temp->data == key) return slot;
        temp = temp->next;
    }
    return -1;
}

int delete(int key){
    int slot = hashfn(key);
    struct Node* temp = hashmap[slot];
    struct Node* prev = NULL;
    while(temp != NULL){
        if(temp->data == key){
            if(prev == NULL){
                hashmap[slot] = temp->next;
            }else{
                prev->next = temp->next;
            }
            free(temp);
            return slot;
        }
        prev = temp; 
        temp = temp->next;
    }
}


int main(){
    return 0;
}