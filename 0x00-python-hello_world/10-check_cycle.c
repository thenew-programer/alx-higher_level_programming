#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: the list that will be checked
 * Return: 0 on failure and 1 on success
*/

int check_cycle(listint_t *list)
{
	listint_t *current;
	int i;

	i = 0;
	while (list != NULL)
	{
		if (list->visited)
		{
			return (1);
		}
			current = list;
			list = list->next;
	}
	return (0);
}
