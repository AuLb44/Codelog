## List code-a-long notes by Andrew Albee

#create a random specified vector, matrix, and data frame
v <- c( 1, 2, 3 )
m <- matrix( 1:10, nrow = 2 )
df <- mtcars

#checking to make sure each is assigned to be the correct data type
class( v )
class( m )
class( df )

#create list to store all three sets of data
my.list1 <- list( v, m, df )

#assigning names to objects in list
my.named.list <- list( Random_sample_vector = v, Random_sample_matrix = m, Random_sample_data_frame = df )

#with names assigned to data list naming convention for data frames works
#so to call a specific part of the list can use
my.named.list$Random_sample_matrix
#or
my.named.list[[ 'Random_sample_matrix']]
class( my.named.list[[ 'Random_sample_matrix']] )
#or
my.named.list[[ 2 ]]
class( my.named.list[[ 2 ]] )

#calling object from list with number will also call the name given to the object in a class 'List' object
my.named.list[ 'Random_sample_matrix' ]
class( my.named.list[ 'Random_sample_matrix' ] )
#or
my.named.list[ 2 ]
class( my.named.list[ 2 ] )

#combining lists
double.list <- c( my.named.list, my.list1 )


