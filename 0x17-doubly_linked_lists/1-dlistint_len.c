#include <stdlib.h>
#include "lists.h"
/**
 * dlistint_len- functiont to return the length of a linked list
 * @h: a pointer to the first node in a linked list
 * Return: size of a linked list
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t size = 0;

	while (h)
	{
		h = h->next;
		size++;
	}
	return (size);
}
