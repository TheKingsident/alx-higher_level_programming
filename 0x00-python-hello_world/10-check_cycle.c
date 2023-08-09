#include "lists.h"

/**
 * check_cycle - Function in C that checks if a singly
 * linked list has a cycle in it.
 * @list: The linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *goFast;
	listint_t *goSlow;


	goFast = list;
	goSlow = list;

	if (list == NULL)
	{
		return (0);
	}

	while (goFast != NULL && goFast->next != NULL)
	{
		goSlow = goSlow->next;
		goFast = goFast->next->next;

		if (goSlow == goFast)
		{
			return (1);
		}
	}

	return (0);
}
