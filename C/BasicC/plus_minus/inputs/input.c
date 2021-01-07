#define _CRT_SECURE_NO_WARNINGS 
//scanf is not recommended, so this code disables the warning

#include <stdio.h> 

int main()
{
    int num1;

    printf("Enter the number: "); //it must be "" to print or scan something!
    scanf("%d, &num1"); //save the input number
    printf("%d\n", num1);

    return 0;
}