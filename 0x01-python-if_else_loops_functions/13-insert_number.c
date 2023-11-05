#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Function to add a node in a sorted
 * singlely linked list.
 * @head: Pointer to the head of the list.
 * @number: Number to be entered.
 * Return: Address to newlly created node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *temp, *current = *head;

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!head || current->n > number || *head == NULL)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current && current->n <= number)
	{
		temp = current;
		current = current->next;
	}
	temp->next = new_node;
	new_node->next = current;

	return (new_node);
}
