#include "lists.h"

/**
 * insert_nodeint_at_index - creates node and adds it at specified index
 * @head: pointer to head node
 * @idx: position to insert new node
 * @n: integer value for creating new node
 *
 * Return: address to new node
 */
listint_t *insert_nodeint_at_index(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *newnode;
	unsigned int count;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
	return (NULL);
	}

	newnode->n = number;

	newnode->next = temp->next;
	temp->next = newnode;
	return (newnode);
}
