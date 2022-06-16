#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 *
 * @list: The linked list
 *
 * Return: 1 if there is a cycle,  0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t tmp1, tmp2;

	tmp1 = *list;
	tmp2 = *list;

	while (tmp2.next != NULL)
	{
		if (*(tmp2.next) == tmp1)
			return (1);
		tmp2 = *(tmp2.next);
	}
	return (0);
}
