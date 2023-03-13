#include "lists.h"

/**
 * size - Returns the size of the linkedlist
 * @head: Singky linked list
 * Return: Size
 */
int size(listint_t **head)
{
listint_t *cur = *head;
int count = 0;
while (cur != NULL)
{
cur = cur->next;
count++;
}
return (count);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Singly linkedlist
 * Return: 0 if there is no palindrome
 *         Otherwise 1
 */
int is_palindrome(listint_t **head)
{
listint_t *front, *back;
int i = 0, j;
int count = size(head);

while (i < (count / 2))
{
front = back = *head;
for (j = 0; j < i; j++)
front = front->next;
for (j = 0; j < count - (i + 1); j++)
{
back = back->next;
}
if (front->n != back->n)
return (0);
else
i++;
}
return (1);
}
