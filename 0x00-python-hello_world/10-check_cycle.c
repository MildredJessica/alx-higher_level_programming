#include "lists.h"

/**
 * check_cycle - Checks if a linkedlist has a cycle
 * @list: Linkedlist
 * Return: 0 if there is no cycle otherwise 1
 */
int check_cycle(listint_t *list)
{
listint_t *first, *second;

first = second = list;
while (first && second && second->next)
{
first = first->next;
second = second->next->next;
if (first == second)
return (1);
}
return (0);
}
