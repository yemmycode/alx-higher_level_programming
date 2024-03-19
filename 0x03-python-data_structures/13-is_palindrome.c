#include <stdio.h>
#include <stdlib.h>
#include "palindrome.h"

/* Function: Check if a singly linked list is a palindrome */

int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev_slow = *head;
listint_t *second_half, *mid_node = NULL;
int res = 1;

if (*head != NULL && (*head)->next != NULL)
{
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}

second_half = slow;
prev_slow->next = NULL;

if (mid_node != NULL)
{
prev_slow->next = mid_node;
mid_node->next = second_half;
}
else
{
prev_slow->next = second_half;
}
}
return (res);
}
