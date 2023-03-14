#include "lists.h"


/**
 * size - Returns the length of a singly-linked .
 * @head: A pointer to the starting node of the list.
 *
 * Return: Tje size.
 */
int size(listint_t **head)
{
int counter = 0;
listint_t *curr = *head;

while (curr != NULL)
{
curr = curr->next;
counter++;
}
return (counter);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
int i = 0, j;
listint_t  *front, *rear;
int count = size(head);

if (*head == NULL || (*head)->next == NULL)
return (1);
while (i != count / 2)
{
front = rear = *head;
for (j = 0; j < i; j++)
front = front->next;
for (j = 0; j < count - (i + 1); j++)
rear = rear->next;
if (front->n != rear->n)
return (0);
else
i++;
}
return (1);
}
