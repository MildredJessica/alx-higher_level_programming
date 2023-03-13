#include "lists.h"

/**
 * reverse_listint - Reverses a linkedlist
 * @head: Pointer to the first node in the list
 * Return: Pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the linkedlist
 * Return: 0 if there is no palindrome
 *         Otherwise 1
 */
int is_palindrome(listint_t **head)
{
listint_t *front, *back, *temp, *dup = NULL;

front = back = temp = *head;

if (*head == NULL || (*head)->next == NULL)
return (1);
while (1)
{
back = back->next->next;
if (!back)
{
dup = front->next;
break;
}
if (!back->next)
{
dup = front->next->next;
break;    
}
back = back->next;
}
reverse_listint(&dup);
while (dup && temp)
{
if (temp->n == dup->n)
{
dup = dup->next;
temp = temp->next;
}
else
return (0);
}
if (!dup)
return (1);
return (0);
}
