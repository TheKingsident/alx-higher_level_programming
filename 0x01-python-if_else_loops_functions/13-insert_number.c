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
	nextNode = currentNode;
	newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
	{
		printf("Allocation failed\n");
		return (NULL);
	}

	newNode->n = number;
	newNode->next = NULL;

	if (currentNode == NULL || number < currentNode->n)
	{
		newNode->next = currentNode;
		*head = newNode;
		return (newNode);
	}


	while (nextNode != NULL && number >= nextNode->n)
	{
		currentNode = nextNode;
		nextNode = nextNode->next;
	}

	newNode->next = nextNode;
	currentNode->next = newNode;

	return (newNode);
}
