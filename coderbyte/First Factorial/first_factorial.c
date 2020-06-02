#include <stdio.h> 
#include <string.h>

void FirstFactorial(int num[]) {
  
    int val = 1;
    for (int i = 2; i <= num; i++) val *= i; 
    printf("%d", val);

}

int main(void) { 
   
  // keep this function call here
  FirstFactorial(gets(stdin));
  return 0;
    
}