##Create our own data frames notes by Andrew Albee

#create empty data frame
empty.df <- data.frame( )

#creating some dummy vectors
days <- c( 'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
temp <- c( 25.0, 27.3, 30.5, 22.0, 21, 22.2, 26.4 )
rain <- c( T, T, F, F, T, F, T )

#factoring and categorizing string data for summary output
factor.days <- factor(days, ordered = F, levels = c( 'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ))

#put vectors into combined data frame
df.1 <- data.frame( factor.days, temp, rain )
print( df.1 )

#calls and prints structure on created data frame
str( df.1 )

#calls and prints summary on created data frame
summary( df.1 )

#calls and prints the top 6 values of data frame. Can specify number of Values in head by adding , # after in parentheses 
head( df.1 )

#calls and prints the bottom 6 values of data frame Can specify number of values in head by adding , # after in parentheses 
tail( df.1 )