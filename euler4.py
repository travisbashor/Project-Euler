# bottom- and top-end of the range of products of two 3-digit values
low, high = 100 * 100, 999 * 999

def reverse(number):
  return int(str(number)[::-1])

def is_palindrome(number):
  return number == reverse(number)

def is_good_product(number):
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

def findPalindrome(top, bottom):
  for i in range(top, bottom, -1):
    if (is_palindrome(i) and is_good_product(i)):
      return str(i)

print("The highest palindromic product of two three-digit numbers is: ", findPalindrome(high, low))
