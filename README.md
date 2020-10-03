
# Object Oriented Programming

## Agenda
1. Why a data scientist should learn about OOP
2. "Everything in Python is an object"  
3. Define attributes, methods, and dot notation
4. Describe the relationship of classes and objectes, and learn to code classes
5. Overview of Inheritance
6. Code Your Own Standard Scaler

# 1. Why a data scientist should learn about OOP

![hackerman](https://media.giphy.com/media/MM0Jrc8BHKx3y/giphy.gif)

  - By becoming familiar with the principles of OOP, you will increase your knowledge of what's possible.  Much of what you might think you need to code by hand is already built into the objects.
  - With a knowledge of classes and how objects store information, you will develop a better sense of when the learning in machine learning occurs in the code, and after that learning occurs, how to access the information gained.
  - You become comfortable reading other people's code, which will improve your own code.
  - You will develop knowledge of the OOP family of programming languages, what are the strengths and weakness of Python, and the strengths and weaknesses of other language families.

  
Let's begin by taking a look at the source code for [Sklearn's standard scalar](https://github.com/scikit-learn/scikit-learn/blob/fd237278e/sklearn/preprocessing/_data.py#L517)

Take a minute to peruse the source code on your own.  



# 2. "Everything in Python is an object"  


Python is an object-oriented programming language. You'll hear people say that "everything is an object" in Python. What does this mean?


Even Python integers are objects. Consider:

By setting x equal to an integer, I'm imbuing x with the methods of the integer class.

# Pair Exercise

Let's practice accessing the methods associated with the built in string class.  
You are given a string below: 

Your task is to fix is so it reads `Hello, World!` using string methods.  To practice chaining methods, try to do it in one line.
Use the [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods), and use the inspect library to see the names of methods.


```python
example.swapcase().replace('0','o').strip().replace('?','!')
```

# Fun Detour About How Python Works

Python is dynamically typed, meaning you don't have to instruct it as to what type of object your variable is.  
A variable is a pointer to where an object is stored in memory.

For more details on this general feature of Python, see [here](https://jakevdp.github.io/WhirlwindTourOfPython/03-semantics-variables.html).
For more on shallow and deepcopy, go [here](https://docs.python.org/3/library/copy.html#copy.deepcopy)

# 3. Define attributes, methods, and dot notation

Dot notation is used to access both attributes and methods.

Take for example our familiar friend, the [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

Instance attributes are associated with each unique object.
They describe characteristics of the object, and are accessed with dot notation like so:

What are some other DataFrame attributes we know?:


```python
# Other attributes
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.T)
```

A **method** is what we call a function attached to an object

What other DataFrame methods do we know?


```python
df.describe()
df.copy()
df.head()
df.tail()
```

# 4. Describe the relationship of classes and objects, and learn to code classes

Each object is an instance of a **class** that defines a bundle of attributes and functions (now, as proprietary to the object type, called *methods*), the point being that **every object of that class will automatically have those proprietary attributes and methods**.

A class is like a blueprint that describes how to create a specific type of object.

![blueprint](img/blueprint.jpeg)


## Classes

We can define **new** classes of objects altogether by using the keyword `class`:

### Methods

We can also write functions that are associated with each class.  
As said above, a function associated with a class is called a method.

Wait a second, what's that `self` doing? 

## Magic Methods

It is common for a class to have magic methods. These are identifiable by the "dunder" (i.e. **d**ouble **under**score) prefixes and suffixes, such as `__init__()`. These methods will get called **automatically** as a result of a different call, as we'll see below.

For more on these "magic methods", see [here](https://www.geeksforgeeks.org/dunder-magic-methods-python/).

When we create an instance of a class, Python invokes the __init__ to initialize the object.  Let's add __init__ to our class.


By adding doors and moving to init, we need to pass parameters when instantiating the object.

We can also pass default arguments if there is a value for a certain parameter which is very common.

#### Positional vs. Named arguments

# Pair

 Let's bring our knowledge together, and in pairs, code out the following:

We have an attribute `moving` which indicates, with a boolean, whether the car is moving or not.  

Fill in the functions stop and go to change the attribute `moving` to reflect the car's present state of motion after the method is called.  Also, include a print statement that indicates the car has started moving or has stopped.

Make sure the method works by calling it, then printing the attribute.



```python
class Car:
    """Automotive object"""
    WHEELS = 4
     # default arguments included now in __init__
    def __init__(self, doors=4, fwd=False, driver_mood='peaceful', moving=False):
        
        self.doors = doors
        self.fwd = fwd
        self.moving = moving
        self.driver_mood = driver_mood

    def honk(self):                   # These are methods we can call on *any* car.
        print('Beep beep')
        
    def go(self):
        self.moving = True
        print('Whoa, that\'s some acceleration!')
    
    def stop(self):
        self.moving = False
        print('Screeech!')
```

## 5. Overview of inheritance

We can also define classes in terms of *other* classes, in which cases the new classes **inherit** the attributes and methods from the classes in terms of which they're defined.

Suppose we decided we want to create an electric car class.

## 6. Standard Scaler through the object lens: 

We are becomming more and more familiar with a series of methods with names such as fit or fit_transform.

After instantiating an instance of a Standard Scaler, Linear Regression model, or One Hot Encoder, we use fit to learn about the dataset and save what is learned. What is learned is saved in the attributes.

### Standard Scaler 

The standard scaler takes a series and, for each element, computes the absolute value of the difference from the point to the mean of the series, and divides by the standard deviation.

$\Large z = \frac{|x - \mu|}{s}$


## Attributes and Methods of Standard Scaler

### `.scale_`, `.mean_`, `.fit`, `.transform`, `.fit_transform`

When we fit the standard scaler, it studies the object passed to it, and saves what is learned in its instance attributes

Then, we can use the transform method to transform every element in the array to the zscore corresponding to the mean and standard deviation learned after fit() was called on the array.

# Pair program

Now we will take our new knowledge of how to create classes and make our own standard scaler. 

Look in scaler.py for the steps to the activity.

Once you have completed the tast, instantiate an instance of your scaler, and check that fitting it returns the same results as sklearns standard scaler fit above. 

Make sure the transform functions return the same results as well.


```python
from scaler_solution import MyStandardScaler

mss = MyStandardScaler()
mss.fit_transform(series_1)[:5]
```




    [0.48775857171297654,
     -0.16102190351705759,
     0.6420145667955479,
     1.53638248233551,
     -0.2589952415079247]




```python
print(mss.scale_)
print(ss.scale_[0])
```

    0.9787262077473544
    0.9787262077473542



```python
print(mss.mean_)
print(ss.mean_[0])
```

    3.0193320558223253
    3.0193320558223253

