#include "lists.h"

/**
 * print_dlistint - prints the number of nodes contained in a list
 * @h: pointer to head node
 *
 * Return: number of nodes contained in list
 */
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *temp = (dlistint_t *)h;
	size_t nodes = 0;

	while (temp)
	{
	nodes++;
	printf("%d\n", temp->n);
	temp = temp->next;
	}
	return (nodes);
}
