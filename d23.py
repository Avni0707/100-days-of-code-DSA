#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
struct Node* mergeSortedLists(struct Node* head1, struct Node* head2) {
    struct Node* mergedHead = NULL;
    struct Node* mergedTail = NULL;
    
    while (head1 != NULL && head2 != NULL) {
        struct Node* newNode;
        if (head1->data < head2->data) {
            newNode = createNode(head1->data);
            head1 = head1->next;
        } else {
            newNode = createNode(head2->data);
            head2 = head2->next;
        }
        
        if (mergedHead == NULL) {
            mergedHead = newNode;
            mergedTail = newNode;
        } else {
            mergedTail->next = newNode;
            mergedTail = newNode;
        }
    }
    
    while (head1 != NULL) {
        struct Node* newNode = createNode(head1->data);
        if (mergedHead == NULL) {
            mergedHead = newNode;
            mergedTail = newNode;
        } else {
            mergedTail->next = newNode;
            mergedTail = newNode;
        }
        head1 = head1->next;
    }
    
    while (head2 != NULL) {
        struct Node* newNode = createNode(head2->data);
        if (mergedHead == NULL) {
            mergedHead = newNode;
            mergedTail = newNode;
        } else {
            mergedTail->next = newNode;
            mergedTail = newNode;
        }
        head2 = head2->next;
    }
    
    return mergedHead;
}
void traverseList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}
int main() {
    int n, m;
    printf("Enter the number of elements in the first list: ");
    scanf("%d", &n);
    
    struct Node* head1 = NULL;
    struct Node* tail1 = NULL;
    
    printf("Enter the elements of the first list: ");
    for (int i = 0; i < n; i++) {
        int data;
        scanf("%d", &data);
        struct Node* newNode = createNode(data);
        
        if (head1 == NULL) {
            head1 = newNode;
            tail1 = newNode;
        } else {
            tail1->next = newNode;
            tail1 = newNode;
        }
    }
    
    printf("Enter the number of elements in the second list: ");
    scanf("%d", &m);
    
    struct Node* head2 = NULL;
    struct Node* tail2 = NULL;
    
    printf("Enter the elements of the second list: ");
    for (int i = 0; i < m; i++) {
        int data;
        scanf("%d", &data);
        struct Node* newNode = createNode(data);
        
        if (head2 == NULL) {
            head2 = newNode;
            tail2 = newNode;
        } else {
            tail2->next = newNode;
            tail2 = newNode;
        }
    }
    
    struct Node* mergedHead = mergeSortedLists(head1, head2);
    
    printf("Merged Linked List: ");
    traverseList(mergedHead);
    
    return 0;
}