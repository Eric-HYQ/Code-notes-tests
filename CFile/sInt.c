#include "sInt.h"

int compar(void const *a, void const *b) {
    register int const *pa = a;
    register int const *pb = b;

    return *pa > *pb ? 1 : *pa < *pb ? -1 : 0;
}
