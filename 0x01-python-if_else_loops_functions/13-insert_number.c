#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *currentNode;
	listint_t *nextNode;

	currentNode = *head;
	nextNode = currentNode->next;
	newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
	{
		printf("Allocation failed\n");
		return (NULL);
	}

	newNode->n = number;

	if (currentNode == NULL || number < currentNode->n)
	{
		newNode->next = nextNode;
		currentNode->next = newNode;
		return (newNode);
	}


	while (nextNode != NULL)
	{
		if (number > currentNode->n && number <= nextNode->n)
		{

			newNode->next = nextNode;
			currentNode->next = newNode;

			return (newNode);
		}

		currentNode = nextNode;
		nextNode = nextNode->next;
	}

	return (newNode);
}
