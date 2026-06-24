/*
    #include <stdio.h> : Used on all default C code, used for interacting with the os console.
        Note: It is crucial to memorize many C libraries.
*/
#include "Class_1.h"
#include <stdio.h>

/*
Class #1
    - C explanation
    - Lineal Search
    - Binary Search
    - Hashing (Key Transformation)

*/

/*
    C explanation:
    - C is a compiled lenguage and strongly tiped lenguage.
*/

// ==== Lineal Search ====

// return_data_type function_name (parameters){}, note: x:=target
int sequencialSearch(int data[], int x, int size) {
    for (int i = 0; i < size; i++) {
        if (data[i] == x) return i; // found
    } // Note: One liner due to one block 
    return -1; // Not found
}

// ==== Binary Search ====

int binarySearchh(int data[], int x, int size) {

    int left = 0;
    int right = size - 1;

    while (left <= right) {
        int pivot = (int)((left + right) / 2);
        if (data[pivot] == x) {
            return pivot;
        }
        else if (data[pivot] > x) {
            right = pivot - 1;
        }
        else {
            left = pivot + 1;
        }
    }
    return -1;
}


// main fn to execute code;
void  execClass1() {
    int data[] = { 1,2,3,4,5,6 };
    int size = 6;
    // Note: on printf {letter}%, {d} -> integrer
    printf("The result is: %d\n", sequencialSearchh(data, 3, size));
    printf("The result is: %d", binarySearch(data, 3, size));
}