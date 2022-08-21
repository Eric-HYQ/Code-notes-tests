#include <stdio.h>
#include <stdlib.h>

#include "sInt.h"

#if 0
int compar(void const *a, void const *b) {
    register int const *pa = a;
    register int const *pb = b;

    return *pa > *pb ? 1 : *pa < *pb ? -1 : 0;
}
#endif

int
main() {
    int *array;
    int nValues;
    int i;

    /*
    ** see how many values
    */
    printf("How many values are there?");
    if (scanf("%d", &nValues) != 1 || nValues <= 0) {
        printf("Illegal number of values.\n");
        exit(EXIT_FAILURE);
    }

    /*
    ** allocate memory to store
    */
    array = malloc(nValues * sizeof(int));
    if (array == NULL) {
        printf("Can't get memory for that many values.\n");
        exit(EXIT_FAILURE);
    }

    /*
    ** read those values
    */
    for (i = 0; i < nValues; i += 1) {
        printf("?");
        scanf("%d", array + 1);
        if (scanf("%d", array + 1) != 1) {
            printf("Error reading value #%d\n", i);
            free(array);
            exit(EXIT_FAILURE);
        }
    }

    /*
    ** sort
    */
    qsort(array, nValues, sizeof(int), compar);

    for (i = 0; i < nValues; i += 1)
        printf("%d\n", array[i]);

    free(array);
    return EXIT_SUCCESS;
}