#include <stdio.h>
#include <stdlib.h>

#define SLOTS 10

struct Node{
    int data;
    struct Node* next;
};

struct Node* hashtable[SLOTS];

int hashfn(int key){
    int slot = key % SLOTS;
    return slot;
}

void insert(int key){
    int slot  = hashfn(key);
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = key;
    newNode->next = hashtable[slot];
    hashtable[slot] = newNode;
}

int search(int key){
    int slot  = hashfn(key);
    struct Node* temp = hashtable[slot];
    while(temp != NULL){
        if(temp->data == key) return slot;
        temp = temp->next;
    }
    return -1;
}

int delete(int key){
    int slot = hashfn(key);
    struct Node* temp = hashtable[slot];
    struct Node* prev = NULL;
    while(temp != NULL){
        if(temp->data == key){
            if(prev == NULL){
                hashtable[slot] = temp->next;
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