#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * print_dlistint - a function to print the content of linked list
 * @h: head of a linked list
 * Return: length of the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t size = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		size++;
	}
	return (size);
}
