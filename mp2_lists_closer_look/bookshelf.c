#include <stdio.h>

int main(void) {

    // Declare an array of 5 pointers.
    char *books[5] = {
        "Python Crash Course",
        "Serious Python",
        "Fluent Python",
        "Mastering Regular Expressions",
        "Fundamentals of Data Visualization"
    };
    
    // Loop over the array, and print each element.
    for (int i=0; i<5; i++) {
        printf("%s\n", books[i]);
    }

    return 0;
}