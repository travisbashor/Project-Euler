# Find the sum of all even-valued fibonacci terms up to four million 
sum = 0;

#first two fibonacci terms
a = 1
b = 2

while(b <= 4_000_000)
  sum += b if b.even?
  c = a + b
  a = b
  b = c
end

puts "The sum of all even-valued fibonacci terms up to four million is: #{sum}."