import pandas as pd
import numpy as np

class MyStandardScaler:

    """
    This class is a personal rendition of a StandarScaler.

    It takes in an array-like object, and studies it to find the information necessary
    to obtain a z-score (formula below) to every element:

    $\Large z = \frac{|x - \mu|}{s}$

    """
    # Part 1
    ##################################################
    # Code the __init__ method here.
    # You do not have to pass any params beside self if you prefer not to, but you can.
    # For example, you may want to base a default a boolean fitted=False which updates to True
    # once fit/fit_transform is run.
    ##################################################


    # Part 2
    ##################################################
    # Code a fit method.  Pass self and a variable representing an array like object
    # which you want to find the mean and standard deviation of.
    # The result of calling the function should create two new attributes: self.mean_, self.scale_,
    # If the __init__ function included a fitted=False, the function should convert that to true.
    ##################################################

    # Part 3
    ##################################################
    # Code a transform method which takes an array_like_object as a parameter,
    # and transforms each element of that array into its corresponding z-score
    # Use the attributes self.mean_ and self.scale_ to apply the z-score calculation
    # These will be available only after .fit() has been called,
    # so if you used the fitted parameter, check to make sure it's value is True
    # before applying the transform
    # Return the standardized array.
    ##################################################

    # Part 4
    ##################################################
    # Code a fit_transform method here which performs the fit and transform
    # methods coded above in one step.
    # return the standardized array.
    ##################################################




