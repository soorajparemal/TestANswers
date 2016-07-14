/* f- read integer from keyboard and print LSB */
#include <stdio.h>
int main()
{
	int n;
	scanf("%d" , &n);
	printf("%d \n" , n & 1);
}
