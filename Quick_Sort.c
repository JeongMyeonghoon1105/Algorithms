#include <stdio.h>

/*
void swap(int * left, int * right) {
    int temp=*left;
    *left=*right;
    *right=temp;
    printf("%d, %d\n", *left, *right);
}
*/

void quick(int arr[], int left, int right) {
    int pivot=0;
    
    if (left==right) {
        pivot=6;
    } else {
        pivot=left;
    }
    
    if (arr[right]<arr[pivot]) {
        // swap(&arr[left], &arr[right]);
        int temp=arr[left];
        arr[left]=arr[right];
        arr[right]=temp;
        left++; 
        if(right<6){
            right++;
        }
    } else {
        if(right<6){
            right++;
        }
    }
    
    printf("left: %d, right: %d, pivot: %d\n", left, right, pivot);
    for(int i=0; i<7; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    quick(arr, left, right);
}

int main() {
    int arr[7]={3, 6, 6, 7, 4, 3, 5};
    
    quick(arr, 0, 0);

    return 0;
}
