#include <stdio.h>
int countZeroSumSubarrays(int arr[], int n) {
    int count = 0;
    
    // Iterate through all possible subarrays
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += arr[j];
            if (sum == 0) {
                count++;
            }
        }
    }
    
    return count;
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    int arr[n];
    printf("Enter the elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    int result = countZeroSumSubarrays(arr, n);
    printf("Count of subarrays with sum zero: %d\n", result);
    
    return 0;
}