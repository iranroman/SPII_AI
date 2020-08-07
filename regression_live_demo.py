from sklearn import datasets
import numpy as np
X,y = datasets.load_breast_cancer(return_X_y=True)

feature_idx = 0

# removin the mean
X[:,feature_idx] -= np.mean(X[:,feature_idx]) 
# removing unit variance
X[:,feature_idx] /= 100*np.var(X[:,feature_idx]) 

y_0 = np.where(y==0)
y_1 = np.where(y==1)

while True:

	bias, slope = input("Enter bias and slope values: ").split()

	y_hat = float(bias) + float(slope)*X[y_0[0][0],feature_idx]

	print('==== CANCER EXAMPLE ====')
	print('linear regression y_hat: ', y_hat)

	y_hat = 1/(1+np.exp(-y_hat))
	
	print('logistic regression y_hat: ', y_hat)

	y_hat = float(bias) + float(slope)*X[y_1[0][0],feature_idx]

	print('==== HEALTHY EXAMPLE ====')
	print('linear regression y_hat: ', y_hat)

	y_hat = 1/(1+np.exp(-y_hat))
	
	print('logistic regression y_hat: ', y_hat)

	print('*****************************')
	print('*****************************')
	print('*****************************')


