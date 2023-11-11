#include <stdlib.h>
#include<stdio.h>
#include "lists.h"
/**
 * add_dnodeint - a function to add node at the beggining of the linked list
 * @head: pointer to the first node of a linked list
 * @n: the value of a new lists
 * Return: a pointer to the new node
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new;

	new = malloc(sizeof(dlistint_t));
	if (!head || !new)
		return (NULL);
	new->n = n;
        new->next = (*head);
        (*head) = new;
	return (new);
}
