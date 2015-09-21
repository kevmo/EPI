# 5.01 Compute Parity

# A parity bit (also called a check bit) is a bit added to the end
# of a string of binary code that indicates whether the number of
# bits in the string with a value of 1 is even or odd. This is the
# simplest form of error detecting code.


def determine_parity(num):
  """Expect a binary number, return 0 if number is even parity, 1 if odd.

  This is a brute force algorithm.
  Time complexity: O(n), where n is the number of digits in num.

  """
  digits = [int(i) for i in str(num)]

  number_of_ones = reduce(lambda x, y: x + y, digits)

  parity = number_of_ones % 2

  return parity


print "This should be 0:", determine_parity(10001)
print "This should be 0:", determine_parity(0)
print "This should be 1:", determine_parity(111)
print "This should be 1:", determine_parity(1110000101)
