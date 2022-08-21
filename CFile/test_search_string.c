#include <string.h>
#include <stdio.h>

int 
main() {
    int len1, len2;
    char buffer[] = "25,142,330,Smith,J,239-4123";
    
    #if (0)
    len1 = strspn(buffer, "0123456789"); /* get 2 */
    len2 = strspn(buffer, ",0123456789"); /* get 11 */
    #endif

    
    len1 = strcspn(buffer, "01346789"); /* get 3 */
    len2 = strcspn(buffer, ",01346789"); /* get 2 */
    printf("len1 = %d, \nlen2 = %d\n", len1, len2);

    
    return 0;
}