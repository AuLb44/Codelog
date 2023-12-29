##Data Frame Exercises Script by Andrew Albee

#Ex 1: Recreate the following data frame by creating vectors and using the data.frame function:
Names <- c( 'Sam', 'Frank', 'Amy' )
Age <- c( 22, 25, 26 )
Weight <- c( 150, 165, 120 )
Sex <- c( 'M', 'M', 'F' )
dataframe1 <- data.frame( Age, Weight, Sex, row.names = Names )

#Ex 2: Check if mtcars is a data frame using is.data.frame()
is.data.frame( mtcars )

#Ex 3: Use as.data.frame() to convert a matrix into a data rame: mat <- matrix(1:25,nrow = 5)
mat <- matrix(1:25,nrow = 5)
vectors <- c( 'V1', 'V2', 'V3', 'V4', 'V5' )
dataframe2 <- data.frame( mat )
colnames( dataframe2 ) <- vectors 

#Ex 4: Set the built-in data frame mtcars as a variable df. We'll use this df variable for the rest of the exercises.
df <- mtcars

#Ex 5: Display the first 6 rows of df
head( df )
#or 
df[ 1:6 , ]

#Ex 6: What is the average mpg value for all the cars?
mpg.avg <- sum( df[ ,'mpg' ] ) / nrow( df )
print( mpg.avg )
#or
mpg.mean <- mean( df[ , 'mpg' ] )
print( mpg.mean )

#Ex 7: Select the rows where all cars have 6 cylinders (cyl column)
df[ (df$cyl == 6), ]

#Ex 8: Select the columns am,gear, and carb.
df[ , c( 'am', 'gear', 'carb' ) ]

#Ex 9: Create a new column called performance, which is calculated by hp/wt.
df$'performance' <- df$hp / df$wt
head( df )

#Ex 10: Your performance column will have several decimal place precision. Figure out how to use round() (check help(round)) to reduce this accuracy to only 2 decimal places.
df$performance <- round( df$performance, digits = 2 )
head( df )

#Ex 10: What is the average mpg for cars that have more than 100 hp AND a wt value of more than 2.5.
avg.mpg <- mean( df[ df$hp > 100 & df$wt > 2.5  , 'mpg' ] )
print( avg.mpg )

#Ex 11: What is the mpg of the Hornet Sportabout?
df[ 'Hornet Sportabout', 'mpg']




