# Notes of *'Pointer on C'*

> 2nd edition
> Beginning time: 8/10/2022
> 
## Quick start
### Intro
#### Commont
Between `/\*` and `*/`

If want to 'commont out' a block of codes within a commont already inside, it won't be successful.

Should use `#if` directive to logically delete
```
#if 0
    statement
#endif
```

#### Preprocessor
```
#include <stdio.h>
#include <stdib.h>
#define max_cols 20 /* max # if columns to process */
```
These are *preprocessor directives* or *directives*

The preprosessor reads the source code, modifies the file here and then pass it to complier.

`#define` is called *function prototype*, defines the constant value of a variable without type 
**So be very careful when pass a parameter**

#### main function
Each C program should contain a `main` function, which is where execution begins
```
int main ( void ) {
    
}
```
- `int` means the function returns an int value
- `void` means it expects no arguments

In C, array arguments are passed by *reference* while scalar variables and constants are passed by *value*

Therefore, changes made by a function to a scalar are lost when function returns. But for elements in array arguments, they will be actually modified.

`gets()` function reads *one line* of text from standard input and stores it in the array passed as an argument. `get` function discards *newline* character `\n` at the end of line and replaces by a `NUL` character and then return a non-NULL value to indicate this line is finished. When returns a NULL, means it's over this line

In C, there is no "string" data type, but regard a sequence of characters terminated by a NUL byte as a string. A *string literal* is a sequence of characters enclosed in quatation marks
```
"Hello"
```
This is a string literal, occupies six bytes in memory (H, e, l, l, o, NUL)

`printf` performs formatted output
| Format | Meaning |
| --- | --- |
| %d, o, x | integral in decimal, octal, hexadecimal |
| %g | floating-point value |
| %c | character |
| %s | string |
| \n | a new line |

## Basic concepts
### Environment
source code - complier - object code - linker - excutable

libraries link by linker, too

complier: preprocessor - parse (- optimizer)

- `.c` c program
- `.o` object code
- `.h` header file
> only one .c, object code deleted after linker
> .c and .o file can complier together
> `-c` can produce object file
> `-o` rename

## Data
### Basic data type
#### Integer family


#### Declear
use `int *a` rather than `int *a` to declear a pointer

`char *message = "hello"` == `char *message; message = "hello"`

#### Typedef
define new data types

used in complex definitions
```
typedef char *ptr_to_char; /* declear ptr_to_char as a new type of pointers to char data */

prt_to_char a; /* declear a as a pointer to char*/
```
use `typedef` rather than `#define`

#### Constants
initialize constants when declear or use `#define`

`#define` can be used in anywhere allows literal while `const` can only in variables
```c
/* both ok, choose one and insist it */
int const a;
const int a;

/* first one is a pointer to an int const
** you can change the value of pointer but not the value of int
** second one is a const pointer to an int
** you can change the value of int but the address is const
** the last one, neither can be changed
*/
int const *pci;
int *const pci;
int const *const pci;
```

#### Scope
a list of statements enclosed in braces is called a block

variables decleared inside a block have **block scope**

all variables ourside a block have **file scope**

#### Storage class
the storage class determines when to create and destroy, how long it will remain

there are three possible places to store: ordinary memory, runtime stack, and hardware registers

default storage:
- variables decleared outside blocks, in static memory, cannot specify any other storage class
- inside block, automatic, or called on the stack, 
- inside block, use `static` keyword, make it static variable

## Statement
### Empty statement
only a semicolon

used in situations where syntax requires a statement but no word need to be performed

### Expression statement
there is no assignment statement in C, regard it as also an operation which performs by expression

expression statement can have few effects
```c
x = y + 3; /* expression statement, execute like assignment */

y + 3; /* totally legal expression statement, statement is calculated but no where to store */

printf("Hello\n"); /* expression statement, return number of characters, dont care */

a++; /* expression, side effect as change value of a */
```

### if statement
```c
if (expression)
    statement
else
    statement
```
> braces are not neccesary here but to avoid mistake, should be added at anytime

C doesn't have *bool* type, so espression uses int only:
- 0 is false
- non 0 is true

### while statement
```
while (expression)
    staement
```

`break` can end the whole loop and execute statements behind the loop right now

`continue` can end this loop and back to expression to decide whether continue the loop

### for statement
```
for (expression 1; expression 2; expression 3)
    statement
```

### do statement
do statement before while expression

at least execute statement once

### switch statement
```c
switch (expression)
    statement list
```

use `break` in each statement to seperate situations

add `defaul:` as no match

if want execute continuous statements in cases, no break and comment as `/* FALL THRU */`

### goto statement
dangerous for green hand, hard to fix
```c
/* eg.
** goto need a label with :
** two programs are the same, see the differences
*/
i = 0;
out_next:
    if (i >= NUM_ELE - 1)
        goto outer_end;
    j = i + 1;
inner_next:
    if (j >= NUM_ELE )
        goto inner_end;
    if (value[i] <= value[j])
        goto no_swap;
    temp = value[i];
    value[i] = value[j];
    value[j] = temp;
no_swap:
    j += 1;
    goto inner_next;
inner_end:
    i += 1;
    goto outer_next;
outer_end:
    ;
```
```c
if (i = 0; i < NUM_ELE; i += 1) {
    for (j = i + 1; j < NUM_ELE; j += 1) {
        if (value[i] > calue[j]) {
            temp = value[i];
            value[i] = value[j];
            value[j] = temp;
        }
    }
}
```

can use `goto` to leave multiple loop immediately

## Operator & Expression
### Operator
#### Arithmetic
`+ - * / %`

#### Shifting
`<<` shift left `>>` shift right

shift left, discard bits on the left and zero-bit put on the right
```
      0 1 1 0 1 0 1 // before shift

0 1 1 0 1 1 0 1     // shift left for three bits

      0 1 1 0 1 0 0 // final value after shift
```

shift right 
- logical shift, zeros are shift in on the left
- arithmetic shift, put copies of the sign bit into the left (to keep the sign)
> the method depends on your complier

#### Bitwise
`&` AND; `|` OR; `^` XOR

can operate bit one by one

#### Assignment
again, where allows expression statements allows assginment

compound assignment
`+=, -=, *=, /=,%=, <<=, >>=, &=, |=, ^=` same as `a = a + (expression)` 

#### Unary
unary operators, take only one operand
`!, ++, -, &, sizeof, ~, --, +, *, (type)`
- !, performs a logical negation of its operand
- ~, produces complement of an int operand(each bit 0 to 1 and 1 to 0)
- -, negative of operand
- +, do nothing
- &, produces the address of its operand
- *, used with an pointer, get the value of the address that pointer points to
- sizeof, determines the size of its operand, measured in bytes
- (type), called a *cast*, convert the value of an expression to another type
- ++, --, both have *prefix* and *postfix* version, different when in an expression
> before the operand increments before value is used in the expression
> after the operand increments after the value is used in the expression
```
int a, b, c, d;

a = b = 10; // a and b get value 10
c = ++a;    // a adds to 11, c gets 11
d = b++;    // b adds to 11, d gets 10
```

#### Relational
`>, <, >=, <=, ==, !=`

#### Logical
`&&, ||`

bitwise needs to calculate both left and right to get a result

but if left one can decide the expression, logical won't calculate right
```
a = 1;
b = 2;

a && b; // true, both values are non-zero(true)
a & b;  // false, no bit position that contaon a one in both a and b
```
> remember, there is **NO BOOL** value in C, all results are value, non-zeros are true

#### Conditional
`expression 1 ? expression 2 : expression 3`
if 1 is true, use 2, if false, use 3

#### Comma
`expr 1, expr 2, ... , expr n` the value of the whole expression is the last one, which is any expression before `expr n` will be discarded after one time

sometimes useful
```c
a = get_value(); // get initial value before while loop
count_value(a);
while (a > 0) {

    a = get_value();
    count_value(a);

} 
```
this codes can be shorted as
```c
while (a = get_value(), count_value(a), a > 0) {
    ;
}

```

#### Subcript & Function call & Structure member
`array[subscript]`

`.` and `->` used to access a structure member

## Pointers
### Memory & Address
bit contains 0 or 1

byte = 8 bit (0 - 255 as unsigned or -128 - 127 as signed)

- each location in memory is identified by a unique address
- each location in memory contains a value

### Indirection operator
following a pointer to the location to which it points is called *indirection*, use `*`

### Illegal pointers
not initialize a pointer is very dangerous, must make sure it is initialized before using

### NULL pointer
a pointer that points to nothing

eg. a function used to search for a specific value in an array and return a pointer that points to it. If no that value, return NULL pointer
> this is a common skill in C, but violates a software engineering principle. Have a single variable (return pointer) to have two meanings (if there is a value? where is it?) is dangerous, easy to be confused
> Right way is letting the function returns two individual value, one status value indicates the result of the operation and the other is the pointer

`*NULL` is illegal

### Pointer expression
assume `char ch = 'a'; char *cp = &ch;`

| Expression | R-value | L-value |
| --- | --- | --- |
| &ch | address of ch other than cp | illegal |
| cp | value of the pointer itself | location cp |
| &cp | pointer of pointer sp | illegal |
| *cp | value of ch | location of ch |
| *cp + 1 | first get value of ch then plus 1 | illegal |
| *(cp + 1) | value of the position in right of ch | location right behind ch |
| ++cp | a copy of cp after plus 1 | illegal |
| cp++ | a copy of cp and then plus 1(the value itself is the initial cp) | illegal |

### Pointer arithmetic
when add 1 to a pointer, it will depend on the type of the pointer, char* will add 1 byte, int* will add 4 byte

pointer subtraction gets the distance of two elements in array with unit as length of elements rather than byte

## Function
### Function definition
```
type
function_name {
    expressions

    return expresion;
}
```
if no return, use `void`

### Declaration
#### Prototype
put them all in header file and `#include` it in the main function
```
char *strcpy(char *destination, char *source);
```
> the `;` tells you it's prototype
> the name of arguments are not neccesary but suggest to add

#### Default
if there is no prototype when call for the function, the return would be set as int

like if the function is float and no prototype, complier will return a int for this function and then turn it into float, then assign it to the value


### Arguments
**All** arguments in C are passed with *call by value*, which means the function will get a *copy* of the argument value.

if the argument is a name of array, it is a *copy of a pointer* that points to the first element of the array, so elements inside will be changed. 
```c
void
swap(int *x, int *y) {

    int temp;

    temp = *x;
    *x = *y;
    *y = temp;

}
```
> if use `swap(int x, int y)`, the functio will swap copies of x and y, no effect
> when call the function, you must pass address into arguments like `swap(&a, &b)`


### ADTs & Black box
ADT, abstract data type. Technique uses to design and implement ADT is called black box design

users know what the module does by *function* specofication and how to use it by *interface* specification, there is no accessing way other than defined interfaces

use `static` keyword to do so
```c
/*
** declaration for address list module
** header file names "addrlist.h"
*/

/*
** data characters
** max length of each data and max number of addresses
*/
#define NAME_LENGTH 30
#define ADDR_LENGTH 100
#define PHONE_LENGTH 11

#define MAX_ADDR 1000

/*
** interface function
**   given a name, find the corresponding address
*/
char const *
lookup_address(char const *name);

/*
**   given a name, find the corresponding phone number
*/
char const *
lookup_phone(char const *name);
```

```c
/*
** abstract data type to maintain an address list
*/

#include "addrlist.h"
#include <stdio.h>

/*
** each address has three elements, name, address, and phone
** keep in three arrays
*/
static char name[MAX_ADDR][NAME_LENGTH]; 
static char address[MAX_ADDR][ADDR_LENGTH]; 
static char phone[MAX_ADDR][PHONE_LENGTH]; 

/*
** this routine locates a name in the array and returns the subscript
** if the name does not exist, retun -1
*/
static int
find_entry(char const *name_to_find) {
    
    int entry;
    for(entry = 0; entry < MAX_ADDR; entry += 1)
        if(strcmp(name_to_find, name[entry]) == 0)
            return entry;
    return -1;

}

/*
** give a name, find coresponding address
** if name is not found, return a NULL pointer instead
*/
char const *
lookup_address(char const *name) {

    int entry;

    entry = find_entry(name);
    if(entry == -1)
        return NULL;
    else
        return address[entry];

}

/*
** give a name, find corresponding phone number;
** if name is not found, return NULL pointer instead
*/
char const *
lookup_phone(char const *name) {

    int entry;

    entry = find_entry(name);
    if(entry == -1)
        return NULL;
    else
        return phone[entry];

}
```
in this program, `lookup_address` and `looup_phone` are interface function, users can not directly access other data with `static`
> note: string is a char array with NUL as end in C
> note:this program can be optimized by structure

### Recursion
C supports *recursion* functions by its runtime stack

because it uses runtime stack, so when call recursion functions it involves like arguments must be pushed on the stack, space allocated for local variables, and when the functions return, this work must be undone. These are large overhead.

### Variable arguments list
the method to access an unbounded argument list

#### `stdarg` Macro
`stdarg` declares a type `va_list` and three macros `va_start`, `va_arg`, and `va_end`
```c
/*
** calculate average of specified number of values
*/
#include <stdarg.h>

float
average(int n_values, ...) {

    va_list var_arg;
    int count;
    float sum = 0;

    /*
    ** prepare to access the variable arguments
    */
    va_start(var_arg, n_values);

    /*
    ** add the values from the variable argument list
    */
    for(count = 0; count < n_values; count += 1) {
        sum += va_arg(var_arg, int);
    }

    /*
    ** done processing variable arguments
    */
    va_end(var_arg);

    return sum / n_values;
}

```
function `average` declares a variable names `var_arg` to access unknown arguments. `va_start` to initialize, its first argument is the name of variable `va_list` (var_arg here), second argument is the last name before `...`
> limits:
> variable arguments must be accessed one by one, cannot access a middle one only
> must have at least one named argument in the list
> unknow variables do not have prototype, which means they need to use default type

## Array
### 1-D array
name of an array in C is a *pointer constant* (`type *const P`) to the first element in the array
```c
int a[10];
int b[10];
int *c;
int *d;

c = a;
d = &a[0];

/* c == d 
** use b = a to copy a is illegal
** b[3] == *(b + 3)
** a++ b++ is illegal
*/
```
> except two situations
> - when name in `sizeof()` (return length of the whole array)
> - when name behind `&`  (return a pointer to the array)

Hint: 
- when moving through an array by fix increment, pointer variables is more effecient than subscript
- pointers declared as register variables are more efficient than those in static memory or on the stack
- if you can check for loop termination by testing something already initialized, don't use a pointer separate counter
- expressions that must be evaluated at run time are more expensive than constant expressions like `&array[size]`

### Multidimentional array
#### Storage order
*raw major order*, the rightest subscript changes first

name of multi-d array is also a pointer that points to its first element, only difference is the element is also an array(pointers to array)

for `int matrix[3][10]`, `matrix[1][5] == *(*(matrix + 1) + 5)`

#### Pointer to array
for `int matrix[3][10]`, `int (*p)[10] = matrix` p is the pointer to the first line of matrix

`int *pi = &matrix[0][0]` and `int *pi = matrix[0]` can both create pointer to the first element of matrix

#### In function
for `int matrix[3][10]`, both
```c
void
func(int (*mat)[10]);

void
func(int mat[][10]);
```
are ok.

### Arrays of pointers
`int *api[10]`, subscript has a higher precedence than indirection, so it's a 10-element array points to int, which is array of pointers

like an keyword array
```c
char const keyword[][9] = {
    "do",
    "for",
    "if",
    "register",
    "return",
    "while"
}
```
store in a matrix, each line contains 9, cover the longest keyword(include NUL)

if we use an array of pointers
```c
char const *keword[] = {
    "do",...

    "while",
    NULL
}
```
it will not waste a lot of memory
> NULL pointer at last makes the function can find the end of the array without know the length in advance

## String, Character & Byte
### Standard function
length of string `strlen`
return type is `size_`, which is an unsigned int
prototype `size_t strlen(char const *string);`

copy string `strcpy`
prototype `char *strcpy(char *dst, char const *src);`
copy src into dst, the initial value of dst will be covered
return a copy of the first argument, which is the pointer to dst

concatenate string `strcat`
prototype `char *strcat(char *dst, char const *src);`
add src to the end of dst (rest of memory should enough for src)
return a copy of the first argument, which is the pointer to dst

string comoarisons `strcmp`
prototype `int strcmp(char const *s1, char const *s2);`
- if s1 < s2, return a value smaller than 0
- if s1 = s2, return 0 (false)
- if s1 > s2, return a value larger thab 0

functions above also have length-restricted version
```c
char *strcpy(char *dst, char const *src, size_t len);
char *strcat(char *dst, char const *src, size_t len);
int strcmp(char const *s1, char const *s2, size_t len);
```
they always put `len` characters into `dst` destination
- if strlen(src) >= len, get len characters only
- if strlen(src) < len, fill up with NUL to len

### String searching
#### Find a character
`strchr` and `strrchr`
prototypes `char *strchr(char const *str, int ch)` and `char *strrchr(char const *str, int ch)`

`strchr` returns the position that `ch` first appears, if no, return NULL pointer

`strrchr` returns the last position (rightest)

#### Find several characters
`strpbrk`
`char *strpbrk(char const *str, char const *group)`

returns the position that any character in group appears in str

#### Find a substring
`strstr`
`char *strstr(char const *s1, char const *s2)`

returns the first time s2 appears in s1

#### Find string prefixes
`strspn` and `strcspn`
`size_t strspn(char const *str, char const *group)`
`size_t strcspn(char const *str, char const *group)`

`strspn` returns the subscript in s1 that doesn't contain in s2

`strcspn` is the complement, returns the first character that in group

#### Find token
`strtok`
`char *strtok(char *str, char const *sep)`

sep is a string that defines your separators, strtok returns the position of next token in str
> strtok will change the string, if you don't want it, pass a copy into it

#### Charactor operations
character classification and transformation

will reduce the portability of program cause may not use the same character set

#### Memory operation
str functions will stop when meet a NUL, when there is a NUL in the middle of the string, they can not work

these functions can deal with it
```c
void *memcpy(void *dst, void const *src, size_t, len);
void *memmove(void *dst, void const *src, size_t, len); /* like copy, slower, but can handle overlap */
void *memcmp(void const *a, void const *b, size_t, len);
void *memchr(void const *a, void const *b, size_t, len);
void *memset(void *a, int ch, size_t, len);
```
each one contains a len to declare how much characters should be dealt with

## Structures & Unions
### Structure basics
array can store data with the same type, structure can store data have different types

structure and array, two types of *aggregate data type* that can store more than one data
> elements in structure are called *member*
> access elements in array can use subscript, access members in structure can use name

#### Declare
structures are declared by listing members that they will contain
`struct tag { member-list } variable-list`

```c
struct {
    int a;
    char b;
    float c;
} x;

struct {
    int a;
    char b;
    float c;
} y[20], *z;
```
variable x, array y contains 20 structures, pointer z

these two declarations have the same member list, but they are two different types, which means `z = &x` is illegal

what if you want to connect them? use tag
```c
struct SIMPLE {
    int a;
    char b;
    float c;
};

struct SIMPLE x;
struct SIMPLE y[20], *z;
```
this declaration doesn't provide variable list (not create any variable), but associates the tag SIMPLE with the member list

now x, y, z are all the same kind of structure

> typedef can do almost the same thing 
> ```
> typedef struct {
>   int a;
>   char b;
>   float c;
> } Simple;
>
> Simple x;
> Simple y[20], *z
> ```
> the difference is that now Simple is a type and has a different method to declare variables

#### Direct member access
use `.` to access, left operand is the name of structure variable and right is desired member

can be multiple accessing like `struct COMPLEX comp`, `comp.sa[4].c`

#### Indirect member access
use a pointer to a structure to access

first indirect access by pointer, then use point operator (latter has higher priority, so brace is necessary)
a function `void func(struct COMPLEX *cp)` has a structure argument, use `(*cp).f` to call

C has a better choice, `->`, left is a pointer to a structure while right is a member `cp->f`

#### Self-referential structure
structure contains a member that has the same type of itself, use pointer rather than a full structure type
```c
/* illegal */
struct SELF_REF1 {
    int a;
    struct SELF_REF1 b;
    int c;
}

/* legal */
struct SELF_REF2 {
    int a;
    struct SELF_REF2 *b;
    int c
}
```
> `b` now is a pointer to SELF_REF2 strcuture rather than a full structure
> actually the pointer points to another structure has the same type (implement linked list and tree)

#### Initializing
```c
struct INIT_EX {
    int a;
    short b[10];
    Simple c;
} x = {
    10,
    {1,2,3,4,5},
    {25, 'x', 1.9}
}
```

### Structure, pointer and member
eg to show how to access structures and members via pointer
```c
typedef struct {
    int a;
    short b[2];
} Ex2;
typedef struct EX {
    int a;
    char b[3];
    Ex2 c;
    struct EX *d;
} Ex;

Ex x = {10, "Hi", {5, {-1, 25}}, 0};
Ex *px = &x;
```

px is a pointer to structure, cannot `px + 1`

R-value of *px is the whole structure that px points to, `*px + 1` is also illegal

px->a can also write as x.a
> the location of a is also the address of the structure
> however, int *a and px have different type but the same value
> can use cast to assign `int *pi = (int *)px`, then pi will points to a
> but the method is dangerous, correct method is `pi = &px->a`
> `->` has higher precedence than `&`, so parentheses are not needed

nested structure can also use `px->c.a` 
> `px->c.a` and `*px->c.b`
> first, px->c get structure c
> .a to access member a, which is an int, so get a value
> .b ti access member b, which is an array, so get a pointer to the first element, * indirectly access to get the first value

### Structure atorage allocation
memory is allocated for each of the members, one after another, in the order given by the member list.

extra memory is only used when needed to get the correct boundary alignment of a member

eg
```c
struct ALIGN {
    char a;
    int b;
    char c;
}
```
complier is forbidden on skip bytes for boundary alignment at the beginning of a structure, so all structures must begin on whatever boundary is required for the most stringent data type

in `ALIGN`, int is the most stringent count for 4 bytes, so one ALIGN variable needs 12 bytes (char 1, skip 3 bytes to align, int 4, char 1, 3 to align)

if let the most stringent member listed first, can reduce it to 8 byte (int 4, char 1, char 1, skip 2 to align)

`offsetof(struct ALIGN, b)` can return how many bytes away from b to the beginning (in stddef.h)


### Bit fields
declared exactly like a structure except that the members are fileds of one or more bits
> a int begind name; to define the bits for the field
> member must be int or signed int or unsigned int


### Union
All of the members of a union refer to the same location in memory

union are used when you need to store different things in one place at different time

## Dynamic memory allocation
### malloc & free
`void *malloc(size_t size)` & `void free(void *pointer)`
size is the number of bytes of memory that are needed, `malloc` returns a pointer to the beginning of that memory block
> this block is not initialized yet, do it in person or use `calloc`
> `malloc` allocates continuous blocks of memory
> if the rest of memory is not enough, returns NULL, checking it is important

`free` return the memory block back to the memory pool
> argument must be return from malloc/calloc/realloc/NULL, NULL will do nothing

### calloc & realloc
`void *calloc(size_t num_element, size_t element_size)`
`void realloc(void *ptr, size_t new_size)`

calloc is similar to malloc, but calloc will initialize the memory to all 0
> arguments are number of elements and their sizes
> if your program only wants to store some value into array, initializatio is not necessary

realloc is used to change the size of a previously allocated block of memory
> if used to expand, old contents remain unchanged and additional memory are not initialized
> if new size is smaller, remove from end and keep old contents in remain memory
> after realloc, pointers to old memory may be changed
> if ptr is NULL, realloc acts just like malloc

### Using
```c
int *pi;

pi = malloc(100);
if (pi == NULL) {
    printf("Out of memory!\n");
    exit(1);
}
```
> if allocation is successful, we get a pointer to 100 bits
> if statement used to check whether the allocation successful
> if your goal is to get 25 int (100 bits), better to use `pi = malloc(25 * sizeof(int))`, portable

`free` should free the whole memory block together rather than partial, but `realloc` can partially return from back

forget to free will lead to *memory leak*




