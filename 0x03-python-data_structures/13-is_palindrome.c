#include "lists.h"

/**
 * is_palindrome - Function that checks linked list for palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 1 if it is palindrome and 0 if not.
 *
 * Description: First splits the linked list,
 * reverses the first half and then
 * compares the two.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *next, *prev;

	if (!head || !*head || !(*head)->next)
		return (1);

	slow = *head;
	fast = *head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	prev->next = NULL;
	slow = reverse_list(slow);
	next = *head;

	while (slow)
	{
		if (slow->n != next->n)
		{
			slow = reverse_list(slow);
			prev->next = slow;
			return (0);
		}
		slow = slow->next;
		next = next->next;
	}
	return (1);
}

/**
 * reverse_list - Function to reverse the list.
 * @head: Pointer to the new head.
 *
 * Return: Pointer to the head of reversed list.
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *next;

	while (head)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}
