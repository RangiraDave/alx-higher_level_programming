#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Function to check whether a linked list is cycle.
 * @list: Pointer to head of the list provided.
 * Return: 1 when cycle is detected and 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *normal = list;
	listint_t *far = list;

	if (!normal || !far)
	{
		printf("Empt list provided.");
		exit(98);
	}

	while (normal != NULL && far != NULL)
	{
		normal = normal->next;
		far = far->next->next;

		if (normal == far)
			return (1);
	}

	return (0);
}
