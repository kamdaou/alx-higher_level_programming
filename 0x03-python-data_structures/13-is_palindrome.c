#include "lists.h"
int length(listint_t *head);
/**
* is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: head of the list
 *
 * Return: 1 if its a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	return length(*head);
}
/**
 * length - gets the length of a linked list
 * @head: the list
 * Return: the length
 */
int length(listint_t *head)
{
	int n = 0;
	struct listint_s *nh;

	for (nh = head; nh->next != NULL; nh = nh->next)
		n++;
	return (n);
}
