#include <stdio.h>
#include <string.h>

/*
** To test how signed and unsigned keywords working
** signed char should be 1 byte, within -255 - 255
** unsigned cancels the mark which indicates the positive or negatice
** this program out output as 255
*/





int main() {
    unsigned char a[500];
    for (int i = 0; i < 300; i++) {
        a[i] = -1 - i;
    }
    printf("%d\n", strlen(a));
    return 0;
}