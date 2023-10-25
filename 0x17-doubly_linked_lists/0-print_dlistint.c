#include "lists.h"

/**
 * print_dlistint - a function that prints all the elements
 * @h: input
 * Return: numbers node
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *node = h;
	size_t a = 0;

	while (node)
	{
		printf("%i\n", node->n);
		a++;
		node = node->next
	}
	return a;
}
