#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
	int is_pal;
	int index;
} listint_t;


size_t print_listint(const listint_t *h);
size_t print_listint_pal(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
bool palindrome(listint_t *head, int count);

#endif /* LISTS_H */
