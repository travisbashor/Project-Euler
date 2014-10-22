# bottom- and top-end of the range of products of two 3-digit values
low, high = 100 * 100, 999 * 999

# returns a number with its digits in reverse order
def reverse(number):
  return int(str(number)[::-1])

# uses the reverse() method to determine whether or not the number is palindromic
def is_palindrome(number):
  return number == reverse(number)

# boolean-returning, on whether this number is the product of two 3-digit integers
def is_good_product(number):
  # use the root to narrow the search for factors
  root = number**0.5

  # check here first, since we are starting at the top end
  if root >= 550:
    # a loop that starts at the high end
    for i in range(999,int(root - 1), -1):
      if number % i == 0:
        return True
  else:
    # a loop that starts at the low end
    for i in range(100, int(root + 1)):
      if number % i == 0:
        return True
  return False

# given the highest- and lowest-possible products, find the highest palindromic product of two 3-digit numbers
def findPalindrome(top, bottom):
  for i in range(top, bottom, -1):
    if (is_palindrome(i) and is_good_product(i)):
      return str(i)

# show answer
print("The highest palindromic product of two three-digit numbers is: ", findPalindrome(high, low))
