#include <main.h>

/* Define the structure for the hash table node */
typedef struct hash_node_s {
    char *key;
    char *value;
    struct hash_node_s *next;
} hash_node_t;

/* Define the structure for the hash table */
typedef struct hash_table_s {
    unsigned long int size;
    hash_node_t **array;
} hash_table_t;

/* Function to create a hash table */
hash_table_t *hash_table_create(unsigned long int size) {
    hash_table_t *hash_table = NULL;
    unsigned long int i;

    /* Allocate memory for the hash table structure */
    hash_table = (hash_table_t *)malloc(sizeof(hash_table_t));
    if (hash_table == NULL) {
        return NULL;  /* Return NULL if memory allocation fails */
    }

    /* Set the size of the hash table */
    hash_table->size = size;

    /* Allocate memory for the array of hash table nodes */
    hash_table->array = (hash_node_t **)malloc(sizeof(hash_node_t *) * size);
    if (hash_table->array == NULL) {
        free(hash_table);  /* Free the hash table memory */
        return NULL;  /* Return NULL if memory allocation fails */
    }

    /* Initialize each array element to NULL */
    for (i = 0; i < size; i++) {
        hash_table->array[i] = NULL;
    }

    return hash_table;  /* Return the pointer to the newly created hash table */
}

