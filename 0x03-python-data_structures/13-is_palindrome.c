#include "lists.h"

/**
 * is_palindrome - check if palindrome
 *
 * @head: head of the list
 *
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int isPalindrome = 1, length = 0, i = 0, *arr, middle = 0;
	listint_t *current;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		length++;
		current = current->next;
	}

	arr = malloc(length * sizeof(int));
	if (arr == NULL)
		return (1);

	current = *head;
	for (i = 0; i < length; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}

	middle = length / 2;
	if (length % 2 == 1)
		middle += 1;

	for (i = 0; i < middle; i++)
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
