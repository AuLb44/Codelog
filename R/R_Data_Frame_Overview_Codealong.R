## Data Frame overview code-a-long by Andrew Albee

#create empty data frame
empty.df <- data.frame( )

#create dummy random variables
c1 <- 1:10
c2 <- letters[ 1:10 ]

#create a data fame with the random dummy variable wit the column names defined 
df <- data.frame( col.name.1 = c1, col.name.2 = c2 )

#write a file from data frame to csv
write.csv( df, file = 'saved_df.csv' )

#read a csv file and creates a data frame from file data
df2 <- read.csv( 'saved_df.csv' )
##note when you write your data frame to a file the index list will save as well so if you read the created csv based on a data frame, the index will be read as well

#gives row number of data fame
nrow( df )

#gives column number of data frame
ncol( df )

#calls and prints structure on created data frame
str( df )

#calls and prints summary on created data frame
summary( df )

#calls a specific column and row by number
df[[ 5, 2 ]]

#calls a specific row and column value by column name and row number
df[[ 5, 'col.name.2']]

#assign a new value to a specific place in the data frame
df[[ 2, 'col.name.1' ]] <- 9999

#call a specific row from a data frame
df[ 1, ]

#call a specific column from a data frame in vector form
df$col.name.1
#or
df[ ,'col.name.1']
#or
df[ , 1 ]
#or
df[[ 'col.name.1' ]]

#call a specific column from a data frame in data frame form
df[ 'col.name.1' ]
#or
df[ 1 ]

#create a new data frame with column names
df2 <- data.frame( col.name.1 = 2000, col.name.2 = 'new')

#bind df2 to df giving df the column names specified in df2
dfnew <- rbind( df, df2 )
print( dfnew )

#create a new column to a existing dollar frame by taking 2 times col.name.1 and assigning it to a newly created column
df$newcol <- 2 * df$col.name.1
print( df )

#to rename columns in data frame 
#by renaming all of them
colnames( df )
colnames( df ) <- c('1', '2', '3')
#or by naming individual columns
colnames( df )[ 2 ] <- 'Gary'
print( df )

#to select and print specific rows of your data frame 
head( mtcars, 9)

#to select and print and print specific rows from a data frame with conditional statements
mtcars[ ( mtcars$mpg > 20 ) & ( mtcars$cyl == 6 ) , ]

#to select and print and print specific rows and column from a data frame with conditional statements
mtcars[ ( mtcars$mpg > 20 ) & ( mtcars$cyl == 6 ) , c( 1, 2, 4) ]
#or
mtcars[ ( mtcars$mpg > 20 ) & ( mtcars$cyl == 6 ) , c( 'mpg', 'cyl', 'hp') ]

#detect for missing data points in data frame
is.na( mtcars )
#checks if any values in the data frame come back true (aka missing)
any( is.na( mtcars ) )

#replaces any missing values in your data frame with a specified value
df[ is.na( df ) ] <- 0

#replaces any missing data in a specified column of your data frame with a specific value
df$'3'[ is.na( df$'3' ) ] <- mean( df$'3' )

#testing to see if data of different sizes can be added to a data frame without issues
df3 <- data.frame( )
v1 <- c( letters[ ] )
v2 <- c( 1:5 )
v3 <- c( letters[ 12:26 ] )

df3 <- data.frame( v1, v2, v3 )
#answer: no, or at least not without a some working around

#using a library "plyr" you can use the function "rbind.fill"
library( 'plyr' )
df3 <- rbind.fill( data.frame(v1), data.frame(v2), data.frame(v3) )
#this function takes data frames and combines them by row filling in the values missing for each row with 'NA' if not specified
#note first data frame starts row numbers

#or you can use the library "dplyr" and use the function "dplyr::bind_rows"
library( 'dplyr' )
df4 <- bind_rows( data.frame( v1 ), data.frame( v2 ), data.frame( v3 ) )



