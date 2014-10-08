
public class Euler3 {
  private static final long TEST_VALUE = 600851475143L;
  public static void main(String[] args) {
    System.out.printf("The largest prime factor of %d is:\n%d", TEST_VALUE, largestPrimeFactor(TEST_VALUE));
  }
  
  // return the largest prime factor of a long, n
  public static long largestPrimeFactor(long n) {
    long LPF = 1;
    long high, low;
    
    // since we know the TEST_VALUE is not even, disregard even values in the search for divisors
    for(int i = 3; i < Math.sqrt(n); i += 2) {
      // if a divisor is found, check the primality of the high/low divisor pair
      if(n % i == 0) {
        // assign high/low divisor pair
        low = i;
        high = n / ((long) i);
        
        // if the high is prime, end the search
        if(isPrime(high)) {
          LPF = high;
          break;
        }
        // if the low is prime, continue the search
        else if(isPrime(low)) {
          LPF = low;
        }
      }
    }
    
    return LPF;
  }
  
  // return primality of the long, n. Auxillary function for largestPrimeFactor()
  public static boolean isPrime(long n) {
    boolean primality = false;
    
    // check next to multiples of 6 for prime candidates
    if(((n - 1) % 6 != 0) && ((n + 1) % 6 != 0)) {
      primality = false;
    }
    // if n is a candidate, check for primality
    else {
      for(int i = 2; i < Math.sqrt(n); ++i) {
        if(n % i == 0) {
          primality = false;
          break;
        }
        primality = true;
      }
    }
    
    return primality;
  }
}
