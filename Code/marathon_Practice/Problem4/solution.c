#include <stdlib.h>
#include <stdio.h>
#define SIZE 1000

struct Node {
    char* data;
    int count;
    struct Node* next; 
};

struct Node** hashTable = NULL; 

int hashFn(char* key){
    int sum = 0;
    for(int i = 0; key[i] != '\0'; i++){
        sum += key[i];
    }
    return sum;
}


void insert(char* key){
    int slot = hashFn(key);
    if (hashTable[slot] == NULL){
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = key;
        newNode->count = 1;
        hashTable[slot] = newNode;
        return;
    }
    struct Node* add = hashTable[slot];
    add->count +=1;
    hashTable[slot] = add;
    return;    
}

int searchBiggest(int n){
    struct Node* temp = hashTable[0];
    int max = 0;
    char* value = "";
    for(int i = 0; i < n; i++){
        struct Node* data = hashTable[i];
        if(data->count > max){
            max = data->count;
            value = data->data;
        }    
    }
    printf("%d %s", max, value);
    return 0;
}

int main(){
    hashTable = calloc(100, sizeof(struct Node*));
    int n; 
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        char val[100];
        scanf("%99s", &val);
        insert(val);
    }
    searchBiggest(n);
    return 0;
}