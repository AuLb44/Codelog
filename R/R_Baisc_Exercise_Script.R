##Basic Exercises Script by Andrew Albee

#What is two to the power of five?
result <- 2^5
print( result )

#Create a vector called stock.prices with the following data points: 23,27,23,21,34
stock.prices <- c( 23, 27, 23, 21, 34 )
print( stock.prices )

#Assign names to the price data points relating to the day of the week, starting with Mon, Tue, Wed, etc...
days.of.trading <- c( 'Mon', 'Tues', 'Wed', 'Thu', 'Fri' )
names( stock.prices ) <- days.of.trading
print( stock.prices )

#What was the average (mean) stock price for the week? (You may need to reference a built-in function)
average.stock.price <- mean( stock.prices )
print( average.stock.price )

#Create a vector called over.23 consisting of logicals that correspond to the days where the stock price was more than $23
over.23 <- stock.prices > 23
print( over.23 )

#Use the over.23 vector to filter out the stock.prices vector and only return the day and prices where the price was over $23
print( stock.prices[ over.23 ] )


#Use a built-in function to find the day the price was the highest
maximum.stock.prices <- max( stock.prices )
maximum.price.days <- stock.prices == maximum.stock.prices
stock.prices[ maximum.price.days ] 
