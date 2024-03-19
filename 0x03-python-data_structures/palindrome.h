#ifndef PALINDROME_H
#define PALINDROME_H

/* Definition of a singly linked list node */
typedef struct listint_t
{
    int data;
    struct listint_t *next;
} listint_t;

int is_palindrome(listint_t **head);

#endif /* PALINDROME_H */
