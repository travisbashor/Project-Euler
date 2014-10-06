// Find the sum of all multiples of 3 or 5 below 1000.
#include <stdio.h>

int main(void) {
  int i, sum = 0;

  for(i = 1; i < 1000; ++i) {
    // multiples of 3
    if(i % 3 == 0) {
      sum += i;
    }
    // multiples of 5 that aren't multiples of 3
    else if(i % 5 == 0) {
      sum += i;
    }
  }

  printf("The sum of all multiples of 3 or 5 below 1000 is: %d\n", sum);

  return 0;
}