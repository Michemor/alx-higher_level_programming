#include "lists.h"

/**
 * check_cycle - checks whether the loop contains a cycle.
 * @list: stores a pointer to the head node
 *
 * Return: 1 if cycle is present and 0 if cycle is absent
 */
int check_cycle(listint_t *list)
{
	listint_t *tort = list;
	listint_t *hare = list;

	while (tort && hare && hare->next)
	{
	tort = tort->next;
	hare = hare->next->next;
	if (hare == tort)
		return (1);
	}
	return (0);
}
