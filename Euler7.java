import java.util.ArrayList;


public class Euler7 {
  public static void main(String[] args) {
    ArrayList<Integer> indexedSetOfPrimes = generatePrincipalPrimes();
    int i = 6;
    
    /* since all primes are one-off from multiples of 6, we may restrict our search
    to only those values */
    while(indexedSetOfPrimes.size() < 10001) {
      // check 6i - 1
      if(isPrime(i - 1, indexedSetOfPrimes)) {
        indexedSetOfPrimes.add(i - 1);
      }
      // check 6i + 1
      if(isPrime(i + 1, indexedSetOfPrimes)) {
        indexedSetOfPrimes.add(i + 1);
      }
      
      i += 6;
    }
    
    System.out.printf("The 10,001st prime is: %d", indexedSetOfPrimes.get(10000));
    
  }
  
  // generates a list of the two first primes to use in our main()- and isPrime() functions
  public static ArrayList<Integer> generatePrincipalPrimes() {
    ArrayList<Integer> principalPrimes = new ArrayList<Integer>();
    principalPrimes.add(2);
    principalPrimes.add(3);
    
    return principalPrimes;
  }
  
  // checks an integer for primality, given a list of primes below that integer
  public static boolean isPrime(int num, ArrayList<Integer> primesBelow) {
    int i = 0; // index of the integer 2 in any indexed set of primes
    
    /* only bother dividing by primes below the square root of the number 
     to test for primality */
    while(primesBelow.get(i) <= Math.sqrt(num)) {
      if(num % primesBelow.get(i) == 0) {
        return false;
      }
      i++;
    }
    return true;
  }
}
