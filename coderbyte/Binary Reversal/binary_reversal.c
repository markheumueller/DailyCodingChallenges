#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define	CHAR_BIT	8	

void reverse(char * x, int begin, int end) {
  char c;

  if (begin >= end)
    return;

  c = * (x + begin);
  *(x + begin) = * (x + end);
  *(x + end) = c;

  reverse(x, ++begin, --end);
}

char * int2bin(int i) {
  int bits = sizeof(int) * CHAR_BIT;

  char * str = malloc(bits + 1);
  if (!str) return NULL;
  str[bits] = 0;

  unsigned u = * (unsigned * ) & i;
  for (; bits--; u >>= 1)
    str[bits] = u & 1 ? '1' : '0';

  return str;
}

int * bin2int(char bin[]) {
  char * start = & bin[0];
  int total = 0;
  while ( * start) {
    total *= 2;
    if ( * start++ == '1') total += 1;
  }
  return total;
}

void BinaryReversal(char str[]) {
  int val = atoi(str);
  char * str_bin = int2bin(val);
  reverse(str_bin, 0, strlen(str_bin) - 1);
  int reverse_int = bin2int(str_bin);
  printf("%i", reverse_int);
}

int main(void) {
  // keep this function call here
  BinaryReversal(gets(stdin));
  return 0;
}