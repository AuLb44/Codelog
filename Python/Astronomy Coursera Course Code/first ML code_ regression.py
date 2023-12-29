import numpy as np
from sklearn.tree import DecisionTreeRegressor

# paste your get_features_targets function here
def get_features_targets(data):
  #creates blank array for our answer
  features = np.zeros((data.shape[0], 4))
  # goes through and assings each column to the math operation (i.e. to the calculated colors
  features[:, 0] = data[ 'u' ] - data[ 'g' ]
  features[:, 1] = data[ 'g' ] - data[ 'r' ]
  features[:, 2] = data[ 'r' ] - data[ 'i' ]
  features[:, 3] = data[ 'i' ] - data[ 'z' ]
  targets = data[ 'redshift' ]
  return features, targets

# paste your median_diff function here
def median_diff(predicted, actual):
  median_diff = np.median( abs( predicted[:] - actual[:] ) )
  return median_diff

# write a function that splits the data into training and testing subsets
# trains the model and returns the prediction accuracy with median_diff
def validate_model(model, features, targets):
  # split the data into training and testing features and predictions
  split = features.shape[0]//2
  split2 = targets.shape[0]//2
  choochoo = features[ : split ]
  didntstudy = features[ split : ]
  breakthetargets = targets[ : split2 ]
  boardtheplatforms = targets[ split2 : ]
  # train the model
  model.fit( choochoo, breakthetargets )
  # get the predicted_redshifts
  predictions = model.predict( didntstudy )
  # use median_diff function to calculate the accuracy
  return median_diff(boardtheplatforms, predictions)


if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model
  sye = DecisionTreeRegressor()

  # validate the model and print the med_diff
  diff = validate_model(sye, features, targets)
  print('Median difference: {:f}'.format(diff))
