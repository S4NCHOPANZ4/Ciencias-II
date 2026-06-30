#include <stdio.h>
#include <stdlib.h>
#define SLOTS 10

struct Node{
    int data; 
    struct Node* next;
};

struct Node* hashTable[SLOTS];

int hashFn(int val){
    return val % SLOTS;
}

int insertElement(int val){
    int slot = hashFn(val);
    struct Node* newNode = malloc(sizeof(struct Node));
    newNode->data = val;
    newNode->next = hashTable[slot];
    hashTable[slot] = newNode;
}

int insertElements(int data[], int size){
    for(int i = 0; i < size; i++){
        insertElement(data[i]);
    }
}

int search(int x){
    int slot = hashFn(x);
    struct Node* temp = hashTable[slot];
    while(temp != NULL){
        if (temp->data == x) return slot; 
        temp = temp->next;
    }
    return -1;
}


int linearSearch(int data[], int x, int len){
    for(int i = 0; i< len; i++){
        if (data[i] == x) return i;
    }
    return -1;
}

int binarySearch(int data[], int x, int len){
    int bottom = 0;
    int top = data[len-1];
    while (bottom <= top){
        int middle = (int)((bottom + top)/2);
        if(data[middle] == x) return middle;
        else if(data[middle] > x) top = middle - 1;
        else if(data[middle] < x) bottom = bottom + 1;
    }
    return -1;
}

int main(){
    int data[] = {1,2,3,4};
    int len = sizeof(data)/sizeof(data[0]);
    insertElements(data, len);
    int res1 = search(3);
    int res2 = search(20);
    printf("busqueda de 3 en %d, busqueda de 20 en %d", res1, res2);
    return 0;
}