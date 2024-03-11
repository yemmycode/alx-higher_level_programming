#include "lists.h"

/**
* check_cycle - Determines whether a linked list contains a cycle.
* @head: Pointer to the linked list to check.
*
* Return: 1 if the list has a cycle, 0 if it doesn't.
*/
int check_cycle(listint_t *head)
{
listint_t *current = head;
listint_t *next_node = head;

if (!head)
return (0);

while (current && next_node && next_node->next)
{
current = current->next;
next_node = next_node->next->next;
if (current == next_node)
return (1);
}

return (0);
}
