#include "lists.h"

/**
 * insert_node - Inserts a number in a sorted singly linkedlist
 * @head: First item in the linkedlist
 * @number: Number to be added to the linkedlist
 * Return: The address ofthe new_node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{    
    listint_t *curr;
    listint_t *temp;

    temp = malloc(sizeof(listint_t));
    curr = *head;
    if (temp == NULL)
    return (NULL);
    temp->n = number;
    temp->next = NULL;

    if (curr == NULL || curr->n >= number)
    {
        temp->next = curr;
        curr = temp;
    }
    
    else
    {
        while ((curr->next != NULL) && (curr->next->n < number))
        {
            curr = curr->next;
        }
        temp->next = curr->next;
        curr->next = temp;
        curr = temp;
    }
    return (temp);  
}
