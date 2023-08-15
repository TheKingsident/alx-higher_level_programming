#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: A pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1); }
	listint_t *crawl;
	listint_t *quick;

	quick = *head;
	crawl = *head;
	while (quick->next != NULL && quick->next->next != NULL)
	{
		crawl = crawl->next;
		quick = quick->next->next; }

	reverse_list(&crawl->next);

	int result;

	result = compare_lists(*head, crawl->next);
	reverse_list(&crawl->next);

	return (result);
}

/**
 * reverse_list - Reverses a linked list
 * @head: A pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{

	listint_t *prevNode;
	listint_t *current;
	listint_t *next;

	prevNode = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prevNode;
		prevNode = current;
		current = next; }

	*head = prevNode;
}

/**
 * compare_lists - Compares two linked lists for equality
 * @list1: A pointer to the head of the first linked list
 * @list2: A pointer to the head of the second linked list
 * Return: 0 if not equal, 1 if equal
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
		{
			return (0); }

		list1 = list1->next;
		list2 = list2->next;

	}

	return (1);
}
