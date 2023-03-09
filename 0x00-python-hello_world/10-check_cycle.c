#include "lists.h"

/**
 * check_cycle - Checks if a linkedlist has a cycle
 * @list: Linkedlist
 * Return: 0 if there is no cycle otherwise 1
 */
int check_cycle(listint_t *list)
{
int num = 0;
if (list->n != 0)
num = 1;
return (num);
}
