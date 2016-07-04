for num in xrange(1, 101):
    if num % 15 == 0:
        print "FizzBuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    elif num % 7 == 0:
        print "Woof"
    else:
        print num
