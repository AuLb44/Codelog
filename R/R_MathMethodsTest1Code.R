## Math Methods 1 Test 1 code 
## By Andrew ALbee

## GNU Terry Pratchett

## Take Home test 
library(MASS)
#Question 1

function_1a <- fu

integrand1a <- function(x) { x - x^2 }
integrand1b <- function(y) { ( ( 2*y^2) - (2*y^3 ) )}

result1a <- integrate( integrand1a, lower = 0, upper = 1 )
result1b <- integrate( integrand1b, lower = 0, upper = 1 )
result_path1 <- fractions( as.numeric( result1a[1] ) ) + fractions( as.numeric( result1b[1] ) )
print(result_path1)