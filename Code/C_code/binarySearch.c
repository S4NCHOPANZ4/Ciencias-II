#include <stdio.h>
#include <stdlib.h>


int binarySearch(int data[], int x, int size){
    int bottom = 0;
    int top = size;

    while(bottom <= top){
        int middle = (int)((bottom + top)/2);
        if(x == data[middle]){
            return middle;
        }else if(x > data[middle]){
            bottom = middle +1;
        }else{
            top = middle - 1;
        }
    }
    return -1;
}


int main(){

    int data[] = { 1,2,3,4,5,6 };
    int size = 6;
    printf("The result is: %d", binarySearch(data, 3, size));
    return 0;

}