
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



```python
# It means
type('Hello World')
```


```python
type('')

```


```python
type({})

```


```python
type(print)
```

Even Python integers are objects. Consider:


```python
x = 5
```


```python
type(x)
```

By setting x equal to an integer, I'm imbuing x with the methods of the integer class.


```python
x.bit_length()
```


```python
x.__float__()
```


```python
help(int)
```

# Pair Exercise

Let's practice accessing the methods associated with the built in string class.  
You are given a string below: 


```python
example = '   hELL0, w0RLD?   '
```

Your task is to fix is so it reads `Hello, World!` using string methods.  To practice chaining methods, try to do it in one line.
Use the [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods), and use the inspect library to see the names of methods.


```python
# We can also use
help(str)
```


```python
# Your code here
```


```python
#__SOLUTION__
example.swapcase().replace('0','o').strip().replace('?','!')
```

# Fun Detour About How Python Works

Python is dynamically typed, meaning you don't have to instruct it as to what type of object your variable is.  
A variable is a pointer to where an object is stored in memory.


```python
# interesting side note about how variables operate in Python
```


```python
print(hex(id(x)))
```


```python
y = 5
```


```python
print(hex(id(y)))
```


```python
# this can have implications 

x_list = [1,2,3,4]
y_list = x_list

x_list.pop()
print(x_list)
print(y_list)
```


```python
# when you use copy(), you create a shallow copy of the object
z_list = y_list.copy()
y_list.pop()
print(y_list)
print(z_list)
```


```python
a_list = [[1,2,3], [4,5,6]]
b_list = a_list.copy()
a_list[0][0] ='z'
b_list
```


```python
import copy

#deepcopy is needed for mutable objects
a_list = [[1,2,3], [4,5,6]]
b_list = copy.deepcopy(a_list)
a_list[0][0] ='z'
b_list
```

For more details on this general feature of Python, see [here](https://jakevdp.github.io/WhirlwindTourOfPython/03-semantics-variables.html).
For more on shallow and deepcopy, go [here](https://docs.python.org/3/library/copy.html#copy.deepcopy)

# 3. Define attributes, methods, and dot notation

Dot notation is used to access both attributes and methods.

Take for example our familiar friend, the [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)


```python
import pandas as pd
# Dataframes are another type of object which we are familiar with.

df = pd.DataFrame({'price':[50,40,30],'sqft':[1000,950,500]})
```


```python
type(df)
```

Instance attributes are associated with each unique object.
They describe characteristics of the object, and are accessed with dot notation like so:


```python
df.shape
```

What are some other DataFrame attributes we know?:


```python
# answer
```


```python
#__SOLUTION__
# Other attributes
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.T)
```

A **method** is what we call a function attached to an object


```python
df.info()
```


```python
# isna() is a method that comes along with the DataFrame object
df.isna()
```

What other DataFrame methods do we know?


```python
#__SOLUTION__
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


```python
class Car:
    """Automotive object"""
    pass # This called a stub. 
```


```python
# Instantiate a car object
ferrari =  Car()
type(ferrari)
```


```python
# Try importing car_b's automotive object and check the output of type.
```


```python
# We can give describe the ferrari as having four wheels

ferrari.wheels = 4
ferrari.wheels
```


```python
# But wouldn't it be nice to not have to do that every time? 
# We assume the blueprint of a car will have include the 4 wheels specification
# and assign it as an attribute when building the class
```


```python
class Car:
    """Automotive object"""
    
    wheels = 4                      # These are attributes of *every* car.

```


```python
civic = Car()
civic.wheels

```


```python
#  Then we can add more attributes
class Car:
    """Automotive object"""
    
    wheels = 4                      # These are attributes of *every* car.
    doors = 4

```


```python
ferrari = Car()
ferrari.doors

```


```python
# But a ferrari does not have 4 doors! 
# These attributes can be overwritten 

ferrari.doors = 2
ferrari.doors
```

### Methods

We can also write functions that are associated with each class.  
As said above, a function associated with a class is called a method.


```python
#  Then we can add more attributes
class Car:
    """Automotive object"""
    
    wheels = 4                      # These are attributes of *every* car.
    doors = 4

    def honk(self):                   # These are methods we can call on *any* car.
        print('Beep beep')
        
    
```


```python
ferrari = civic = Car()
ferrari.honk()
civic.honk()

```

Wait a second, what's that `self` doing? 

## Magic Methods

It is common for a class to have magic methods. These are identifiable by the "dunder" (i.e. **d**ouble **under**score) prefixes and suffixes, such as `__init__()`. These methods will get called **automatically** as a result of a different call, as we'll see below.

For more on these "magic methods", see [here](https://www.geeksforgeeks.org/dunder-magic-methods-python/).

When we create an instance of a class, Python invokes the __init__ to initialize the object.  Let's add __init__ to our class.



```python
#  Then we can add more attributes
class Car:
    """Automotive object"""
    
    WHEELS = 4                      # Capital letters mean wheels is a constant
    
    def __init__(self, doors, fwd):
        
        self.doors = doors
        self.fwd = fwd
        

    def honk(self):                   # These are methods we can call on *any* car.
        print('Beep beep')
    
```

By adding doors and moving to init, we need to pass parameters when instantiating the object.


```python
civic = Car(4, True)
print(civic.doors)
print(civic.fwd)
```

We can also pass default arguments if there is a value for a certain parameter which is very common.


```python
#  Then we can add more attributes
class Car:
    """Automotive object"""
    
    WHEELS = 4                     
    
    # default arguments included now in __init__
    def __init__(self, doors=4, fwd=False):
        
        self.doors = doors
        self.fwd = fwd
        

    def honk(self):                  
        print('Beep beep')
    
```


```python
civic = Car()
print(civic.doors)
print(civic.fwd)
```

#### Positional vs. Named arguments


```python
# we can pass our arguments without names
civic = Car(4, True)

```


```python
# or with names
civic = Car(doors=4, fwd=True)

```


```python
# or with a mix
civic = Car(4, fwd=True)

```


```python
# but only when positional precides named
civic = Car(doors = 4, True)
```


```python
# The self argument allows our methods to update our attributes.

#  Then we can add more attributes
class Car:
    """Automotive object"""
    
    WHEELS = 4                     
    
    # default arguments included now in __init__
    def __init__(self, doors=4, fwd=False, driver_mood='peaceful'):
        
        self.doors = doors
        self.fwd = fwd
        self.driver_mood = driver_mood
        

    def honk(self):                  
        print('Beep beep')
        self.driver_mood = 'pissed'
    
```


```python
civic = Car()
print(civic.driver_mood)
civic.honk()
print(civic.driver_mood)
```

# Pair

 Let's bring our knowledge together, and in pairs, code out the following:

Add an attribute `moving` to the __init__ function, which indicates, with a boolean, whether the car is moving or not.  

Fill in the functions stop and go to change the attribute `moving` to reflect the car's present state of motion after the method is called.  Also, include a print statement that indicates the car has started moving or has stopped.

Make sure the method works by calling it, then printing the attribute.



```python
#  Then we can add more attributes
class Car:
    """Automotive object"""
    
    # default arguments included now in __init__
    def __init__(self, doors=4, fwd=False, driver_mood='peaceful'):
        
        self.doors = doors
        self.fwd = fwd
        self.driver_mood = driver_mood
        
    def honk(self):                   # These are methods we can call on *any* car.
        print('Beep beep')
        
    def go(self):
        pass
    
    def stop(self):
        pass
```


```python
#__SOLUTION__
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


```python
# run this code to make sure your 
civic = Car()
print(civic.moving)

civic.go()
print(civic.moving)

civic.stop()
print(civic.moving)
```

## 5. Overview of inheritance

We can also define classes in terms of *other* classes, in which cases the new classes **inherit** the attributes and methods from the classes in terms of which they're defined.

Suppose we decided we want to create an electric car class.


```python
#  Then we can add more attributes
class ElectricCar(Car):
    """Automotive object"""
    
    pass
```


```python
prius = ElectricCar()
prius.honk()
prius.WHEELS
```


```python
#  Then we can add more attributes
class ElectricCar(Car):
    """Automotive object"""
    
    # default arguments included now in __init__
    def __init__(self, hybrid=False):
        super().__init__(self)
        self.hybrid = hybrid 
```


```python
volt = ElectricCar(hybrid=True)
volt.hybrid
volt.driver_mood
```


```python
#  And we can overwrite methods and parent attributes
class ElectricCar(Car):
    """Automotive object"""
    
    # default arguments included now in __init__
    def __init__(self, hybrid=False):
        
        # Prius owners are calmer than the average car owner
        super().__init__(driver_mood='serene')
        
        self.hybrid = True
        
    # overwrite inheritd methods
    
    def go(self):
        
        print('Whirrrrrr')
        self.moving = True
```


```python
prius = ElectricCar()
print(prius.moving)
prius.go()
prius.moving
print(prius.driver_mood)
```

## 6. Standard Scaler through the object lens: 

We are becomming more and more familiar with a series of methods with names such as fit or fit_transform.

After instantiating an instance of a Standard Scaler, Linear Regression model, or One Hot Encoder, we use fit to learn about the dataset and save what is learned. What is learned is saved in the attributes.

### Standard Scaler 

The standard scaler takes a series and, for each element, computes the absolute value of the difference from the point to the mean of the series, and divides by the standard deviation.

$\Large z = \frac{|x - \mu|}{s}$


## Attributes and Methods of Standard Scaler

### `.scale_`, `.mean_`, `.fit`, `.transform`, `.fit_transform`


```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# instantiate a standard scaler object
ss = StandardScaler()

# We can instantiate as many scaler objects as we want
maxs_scaler = StandardScaler()
```


```python
# Let's work with a random array of numbers.
np.random.seed(42)
series_1 = np.random.normal(3,1,1000)
print(series_1.mean())
print(series_1.std())
```

When we fit the standard scaler, it studies the object passed to it, and saves what is learned in its instance attributes


```python
ss.fit(series_1.reshape(-1,1))

# standard deviation is saved in the attribute scale_
ss.scale_
```


```python
# mean is saved into the attribute mean
ss.mean_
```

Then, we can use the transform method to transform every element in the array to the zscore corresponding to the mean and standard deviation learned after fit() was called on the array.


```python
ss.transform(series_1.reshape(-1,1))[:5]
```


```python
# let's double check the math by applying the z-score formula
(series_1[0]-ss.mean_)/ss.scale_
```


```python
# We can call fit and transform in one step as well

ss.fit_transform(series_1.reshape(-1,1))[:5]
```

# Pair program

Now we will take our new knowledge of how to create classes and make our own standard scaler. 

Look in scaler.py for the steps to the activity.

Once you have completed the tast, instantiate an instance of your scaler, and check that fitting it returns the same results as sklearns standard scaler fit above. 

Make sure the transform functions return the same results as well.


```python
%load_ext autoreload
%autoreload 2

```


```python
#__SOLUTION__
from scaler_solution import MyStandardScaler

mss = MyStandardScaler()
mss.fit_transform(series_1)[:5]
```


```python
#__SOLUTION__
print(mss.scale_)
print(ss.scale_[0])
```


```python
#__SOLUTION__
print(mss.mean_)
print(ss.mean_[0])
```
