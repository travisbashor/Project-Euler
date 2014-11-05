# calculate the product of consecutive integers in an array within the given range
def calculate_block_product(some_array, low, high):
  block_product = 1
  for i in range(low, high + 1):
    block_product *= some_array[i]
  return block_product

# this is the step-wise calculation that will take place when we loop through the number array
def calculate_new_product(old_product, some_array, index):
  new_product = old_product / some_array[index - 13]
  new_product *= some_array[index]
  return new_product

# gather input from the file, and make it a string of characters without whitespace 
with open('euler8.txt') as input_file:
  string = "".join(input_file.read().split('\n'))

# convert the string to an array of chars, then that array to integers  
character_array = list(string)
number_array = list(map(int, character_array))

# set the principal product from the first 13 integers
product = calculate_block_product(number_array, 0, 12)
highest_product = product
i = 13

# manual manipulation of the i variable here will allow us to skip
# values that we do not need to consider
while i < len(number_array):
  # if the next number is non-zero, the new product is ready to compute
  if number_array[i] != 0:
    product = calculate_new_product(product, number_array, i)
  # if it is zero, we don't have to consider the next 13 products, which would all be zero
  else:
    i += 13
    # we move forward 13 and make a new product. Since there may still have been a zero 
    # in our new block, we include a check that our new product is not zero before moving forward
    while True:
      product = calculate_block_product(number_array, i - 12, i)
      if product != 0:
        break
      elif i == len(number_array) - 1:
        break
      else:
        i += 1

  # after generating the new product, see if it is the highest thus far
  if product > highest_product:
    highest_product = product

  # step forward
  i += 1

# display the answer
print("The highest product in the block of integers is: %d" % highest_product)