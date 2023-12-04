#include "lists.h"

/**
 * is_palindrome - checks whether the entered list is a palindrome
 * @head: pointer to head
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_half, *second_half;
	listint_t *temp = *head;
	int i, j, len;

	if ((*head)->next == NULL)
	{
	return (1);
	}
	len = length_list(temp);
	i = 0;
	while (i != len / 2)
	{
	first_half = temp;
	second_half = temp;
	for (j = 0; j < i; j++)
	{
	first_half = first_half->next;
	}
	for (j = 0; j < len - (i + 1); j++)
	{
	second_half = second_half->next;
	}
	if (first_half->n != second_half->n)
	{
	return (0);
	}
	i++;
	}
	return (1);
}
/**
 * length_list - evaluates the length of the list
 * @current: pointer to head node
 *
 * Return: length of the lists
 */
int length_list(listint_t *current)
{
	int len = 0;

	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	return (len);
}
