#include <stdio.h>

// prototypes
int greatestCommonDenominator(int, int);
int leastCommonProduct(int, int);
int smallestMultipleUpTo(int);

int main(void) {
  int i = 20;
  printf("The smallest multiple in [1,%d] is: %d\n", i, smallestMultipleUpTo(i));
  return 0;
}

// using the euclidean algorithm, recursively computes the GCD of two numbers
int greatestCommonDenominator(int low, int high) {

  // base case: high is a multiple of low
  if(high % low == 0) {
    return low;
  }
  // otherwise, recur down modulus values
  else {
    return greatestCommonDenominator(high % low, low);
  }
}

// computes the least common product of two ordered numbers, using
// greatestCommonDenominator() as an auxillary function
int leastCommonProduct(int low, int high) {
  // relatively prime case
  if(greatestCommonDenominator(low, high) == 1) {
    return low * high;
  }
  // if not relatively prime, divide the gcd out of the smaller number and return the product
  else {
    return (low / greatestCommonDenominator(low, high)) * high;
  }
  
}

// with the low end assumed to be 1, recursively finds the smallest multiple common
// to all values in the range [1, value]
int smallestMultipleUpTo(int value) {
  // base case: value = 1
  if(value == 1) {
    return 1;
  }
  else {
    return leastCommonProduct(value, smallestMultipleUpTo(value - 1));
  }
}