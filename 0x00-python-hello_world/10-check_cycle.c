#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: the list that will be checked
 * Return: 0 on failure and 1 on success
*/

int check_cycle(listint_t *list)
{
	while (list != NULL)
	{
		if (list->visited)
		{
			return (1);
		}
		list->visited = true;
		list = list->next;
	}
	return (0);
}
