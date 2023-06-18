#include "lists.h"

/**
 * is_palindrome - check if palindrome
 *
 * @head: head of the list
 *
 * return: 1 if palindrome 0 if else
 */

int is_palindrome(listint_t **head)
{
	int isPalindrome = 1;
	int length = 0;
	int i = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (isPalindrome);

	listint_t *current = *head;

	while (current != NULL)
	{
		length++;
		current = (current)->next;
	}

	int *arr = malloc(length * sizeof(int));

	current = *head;
	for (i = 0; i < length; i++)
	{
		arr[i] = current->n;
		*head = current->next;
	}

	for (i = 0; i < (length / 2); i++)
	{
		if (arr[i] != arr[length - i - 1])
		{
			isPalindrome = 0;
			break;
		}
	}

	free(arr);
	return (isPalindrome);

}
