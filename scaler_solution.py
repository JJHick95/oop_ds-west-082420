class MyStandardScaler:

    """
    This class is a personal rendition of a StandarScaler.

    It takes in an array-like object, and studies it
    to find the information necessary to calculate
    a z-score for each elemnt:

    z-score = (x - mu)/s
    """

    def __init__(self, fitted=False):

        self.fitted = fitted

    def fit(self, array_like_object):

        '''
        Caution: Only apply to training data.  To not fit on test data

        :param array_like_object:
        :return: the mean and standard standard deviation
        of the array_like_object
        '''

        mean = sum(array_like_object)/len(array_like_object)
        std = (sum(
                    [(element - mean)**2 for element in array_like_object]
                  )/len(array_like_object))**(1/2)
        self.mean_ = mean
        self.scale_ = std
        self.fitted = True

    def transform(self, array_like_object):

        """
        :param array_like_object:
        :return: the array-like object transformed to be centered
        around one with a std of 1
        """

        if self.fitted is False:
            print("Fit your training data first")
            return

        else:

            standardized_array = [(element-self.mean_)/self.scale_
                                  for element in array_like_object]
            return standardized_array

    def fit_transform(self, array_like_object):

        """
        :param array_like_object:
        :return: the array-like object transformed to be centered
        around one with a std of 1
        """

        self.fit(array_like_object)
        standardized_array = self.transform(array_like_object)
        return standardized_array
