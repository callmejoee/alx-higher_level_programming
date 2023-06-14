#include "lists.h"

/**
 * check_cycle - function to check if the linked
 *
 * @list: pointer to head of list
 *
 * Return: 1 on success
 */


int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *current;

	head = list;

	while (head != NULL)
	{
		current = head->next;
		while (current != NULL)
		{
			if (current == head)
			{
				return (1);
			}
			current = current->next;
		}
		head = head->next;
	}
	return (0);
}
