def sumOfSquares n
  # closed-form expression for the first "n" squares
  sum = (n * (n + 1) * (2 * n + 1)) / 6
  return sum
end

# returns the sum of the first n counting numbers, aka the nth triangular number
def triangularNumber n
  # closed-form expression for the sum of the first "n" counting numbers
  # i.e. 1+2+...+n
  thisNum = (n * (n + 1) / 2)
  return thisNum
end

# returns the square of the sum of counting numbers up to n
# i.e. (1+2+...+n)^2
# note: this is also the sum of the first n cubes
def squareOfSum n
  return triangularNumber(n)**2
end

# returns the square of the sum minus the sum of the squares
def difference n
  # derived closed-form expression for the difference, given their respective formulae
  diff = (n * (n + 1) * (2 * n - 2) * (3 * n + 2)) / 24
  return diff
end

answer = difference 100
puts "The difference between the sum of the squares of the first 
100 natural numbers and the square of the sum is #{answer}."