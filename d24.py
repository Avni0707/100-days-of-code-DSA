#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};

int main() {
    int n, key, i;
    struct node *head = NULL, *temp = NULL, *newnode = NULL, *prev = NULL;

    scanf("%d", &n);

    // Creating linked list
    for(i = 0; i < n; i++) {
        newnode = (struct node*)malloc(sizeof(struct node));
        scanf("%d", &newnode->data);
        newnode->next = NULL;

        if(head == NULL) {
            head = newnode;
            temp = newnode;
        } else {
            temp->next = newnode;
            temp = newnode;
        }
    }

    scanf("%d", &key);

    temp = head;

    // If head node contains key
    if(temp != NULL && temp->data == key) {
        head = temp->next;
        free(temp);
    } else {
        // Traverse to find key
        while(temp != NULL && temp->data != key) {
            prev = temp;
            temp = temp->next;
        }

        if(temp != NULL) {
            prev->next = temp->next;
            free(temp);
        }
    }

    // Printing updated list
    temp = head;
    while(temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }

    return 0;
}