
# Object Oriented Programming

## Agenda
1. Why a data scientist should learn about OOP
2. "Everything in Python is an object"  
3. Define attributes, methods, and dot notation
4. Describe the relationship of classes and objectes, and learn to code classes
5. Overview of Inheritance
6. Important data science tools through the lens of objects: Standard Scaler and One-Hot-Encoder

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




    str




```python
type('')

```




    builtin_function_or_method




```python
type({})

```




    dict




```python
type(print)
```




    builtin_function_or_method



Even Python integers are objects. Consider:


```python
x = 5
```


```python
type(x)
```




    int



By setting x equal to an integer, I'm imbuing x with the methods of the integer class.


```python
x.bit_length()
```




    3




```python
x.__float__()
```




    3.0




```python
help(int)
```

    Help on class int in module builtins:
    
    class int(object)
     |  int([x]) -> integer
     |  int(x, base=10) -> integer
     |  
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |  
     |  If x is not a number or if base is given, then x must be a string,
     |  bytes, or bytearray instance representing an integer literal in the
     |  given base.  The literal can be preceded by '+' or '-' and be surrounded
     |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     |  Base 0 means to interpret the base from the string as an integer literal.
     |  >>> int('0b100', base=0)
     |  4
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __ceil__(...)
     |      Ceiling of an Integral returns itself.
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floor__(...)
     |      Flooring an Integral returns itself.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(self, format_spec, /)
     |      Default object formatter.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __invert__(self, /)
     |      ~self
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __round__(...)
     |      Rounding an Integral returns itself.
     |      Rounding with an ndigits argument also returns an integer.
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |  
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __sizeof__(self, /)
     |      Returns size in memory, in bytes.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Truncating an Integral returns itself.
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  bit_length(self, /)
     |      Number of bits necessary to represent self in binary.
     |      
     |      >>> bin(37)
     |      '0b100101'
     |      >>> (37).bit_length()
     |      6
     |  
     |  conjugate(...)
     |      Returns self, the complex conjugate of any int.
     |  
     |  to_bytes(self, /, length, byteorder, *, signed=False)
     |      Return an array of bytes representing an integer.
     |      
     |      length
     |        Length of bytes object to use.  An OverflowError is raised if the
     |        integer is not representable with the given number of bytes.
     |      byteorder
     |        The byte order used to represent the integer.  If byteorder is 'big',
     |        the most significant byte is at the beginning of the byte array.  If
     |        byteorder is 'little', the most significant byte is at the end of the
     |        byte array.  To request the native byte order of the host system, use
     |        `sys.byteorder' as the byte order value.
     |      signed
     |        Determines whether two's complement is used to represent the integer.
     |        If signed is False and a negative integer is given, an OverflowError
     |        is raised.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
     |      Return the integer represented by the given array of bytes.
     |      
     |      bytes
     |        Holds the array of bytes to convert.  The argument must either
     |        support the buffer protocol or be an iterable object producing bytes.
     |        Bytes and bytearray are examples of built-in objects that support the
     |        buffer protocol.
     |      byteorder
     |        The byte order used to represent the integer.  If byteorder is 'big',
     |        the most significant byte is at the beginning of the byte array.  If
     |        byteorder is 'little', the most significant byte is at the end of the
     |        byte array.  To request the native byte order of the host system, use
     |        `sys.byteorder' as the byte order value.
     |      signed
     |        Indicates whether two's complement is used to represent the integer.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  denominator
     |      the denominator of a rational number in lowest terms
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  numerator
     |      the numerator of a rational number in lowest terms
     |  
     |  real
     |      the real part of a complex number
    


Python is dynamically typed, meaning you don't have to instruct it as to what type of object your variable is.  
A variable is a pointer to where an object is stored in memory.


```python
# interesting side note about how variables operate in Python
```


```python
print(hex(id(x)))
```

    0x10ec225e0



```python
y = 3
```


```python
print(hex(id(y)))
```

    0x10ec225e0



```python
# this can have implications 

x_list = [1,2,3,4]
y_list = x_list

x_list.pop()
print(x_list)
print(y_list)
```

    [1, 2, 3]
    [1, 2, 3]



```python
# when you use copy(), you create a shallow copy of the object
z_list = y_list.copy()
y_list.pop()
print(y_list)
print(z_list)
```

    [1]
    [1, 2]



```python
a_list = [[1,2,3], [4,5,6]]
b_list = a_list.copy()
a_list[0][0] ='z'
b_list
```




    [['z', 2, 3], [4, 5, 6]]




```python
import copy

#deepcopy is needed for mutable objects
a_list = [[1,2,3], [4,5,6]]
b_list = copy.deepcopy(a_list)
a_list[0][0] ='z'
b_list
```




    [[1, 2, 3], [4, 5, 6]]



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




    pandas.core.frame.DataFrame



Instance attributes are associated with each unique object.
They describe characteristics of the object, and are accessed with dot notation like so:


```python
df.shape
```




    (3, 2)



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

    Index(['price', 'sqft'], dtype='object')
    RangeIndex(start=0, stop=3, step=1)
    price    int64
    sqft     int64
    dtype: object
              0    1    2
    price    50   40   30
    sqft   1000  950  500


A **method** is what we call a function attached to an object


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3 entries, 0 to 2
    Data columns (total 2 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   price   3 non-null      int64
     1   sqft    3 non-null      int64
    dtypes: int64(2)
    memory usage: 176.0 bytes



```python
# isna() is a method that comes along with the DataFrame object
df.isna()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sqft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



What other DataFrame methods do we know?


```python
#__SOLUTION__
df.describe()
df.copy()
df.head()
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sqft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40</td>
      <td>950</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>



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

    Help on class str in module builtins:
    
    class str(object)
     |  str(object='') -> str
     |  str(bytes_or_buffer[, encoding[, errors]]) -> str
     |  
     |  Create a new string object from the given object. If encoding or
     |  errors is specified, then the object must expose a data buffer
     |  that will be decoded using the given encoding and error handler.
     |  Otherwise, returns the result of object.__str__() (if defined)
     |  or repr(object).
     |  encoding defaults to sys.getdefaultencoding().
     |  errors defaults to 'strict'.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(self, format_spec, /)
     |      Return a formatted version of the string as described by format_spec.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __sizeof__(self, /)
     |      Return the size of the string in memory, in bytes.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  capitalize(self, /)
     |      Return a capitalized version of the string.
     |      
     |      More specifically, make the first character have upper case and the rest lower
     |      case.
     |  
     |  casefold(self, /)
     |      Return a version of the string suitable for caseless comparisons.
     |  
     |  center(self, width, fillchar=' ', /)
     |      Return a centered string of length width.
     |      
     |      Padding is done using the specified fill character (default is a space).
     |  
     |  count(...)
     |      S.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of substring sub in
     |      string S[start:end].  Optional arguments start and end are
     |      interpreted as in slice notation.
     |  
     |  encode(self, /, encoding='utf-8', errors='strict')
     |      Encode the string using the codec registered for encoding.
     |      
     |      encoding
     |        The encoding in which to encode the string.
     |      errors
     |        The error handling scheme to use for encoding errors.
     |        The default is 'strict' meaning that encoding errors raise a
     |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
     |        'xmlcharrefreplace' as well as any other name registered with
     |        codecs.register_error that can handle UnicodeEncodeErrors.
     |  
     |  endswith(...)
     |      S.endswith(suffix[, start[, end]]) -> bool
     |      
     |      Return True if S ends with the specified suffix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      suffix can also be a tuple of strings to try.
     |  
     |  expandtabs(self, /, tabsize=8)
     |      Return a copy where all tab characters are expanded using spaces.
     |      
     |      If tabsize is not given, a tab size of 8 characters is assumed.
     |  
     |  find(...)
     |      S.find(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  format(...)
     |      S.format(*args, **kwargs) -> str
     |      
     |      Return a formatted version of S, using substitutions from args and kwargs.
     |      The substitutions are identified by braces ('{' and '}').
     |  
     |  format_map(...)
     |      S.format_map(mapping) -> str
     |      
     |      Return a formatted version of S, using substitutions from mapping.
     |      The substitutions are identified by braces ('{' and '}').
     |  
     |  index(...)
     |      S.index(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in S where substring sub is found, 
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the substring is not found.
     |  
     |  isalnum(self, /)
     |      Return True if the string is an alpha-numeric string, False otherwise.
     |      
     |      A string is alpha-numeric if all characters in the string are alpha-numeric and
     |      there is at least one character in the string.
     |  
     |  isalpha(self, /)
     |      Return True if the string is an alphabetic string, False otherwise.
     |      
     |      A string is alphabetic if all characters in the string are alphabetic and there
     |      is at least one character in the string.
     |  
     |  isascii(self, /)
     |      Return True if all characters in the string are ASCII, False otherwise.
     |      
     |      ASCII characters have code points in the range U+0000-U+007F.
     |      Empty string is ASCII too.
     |  
     |  isdecimal(self, /)
     |      Return True if the string is a decimal string, False otherwise.
     |      
     |      A string is a decimal string if all characters in the string are decimal and
     |      there is at least one character in the string.
     |  
     |  isdigit(self, /)
     |      Return True if the string is a digit string, False otherwise.
     |      
     |      A string is a digit string if all characters in the string are digits and there
     |      is at least one character in the string.
     |  
     |  isidentifier(self, /)
     |      Return True if the string is a valid Python identifier, False otherwise.
     |      
     |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
     |      "class".
     |  
     |  islower(self, /)
     |      Return True if the string is a lowercase string, False otherwise.
     |      
     |      A string is lowercase if all cased characters in the string are lowercase and
     |      there is at least one cased character in the string.
     |  
     |  isnumeric(self, /)
     |      Return True if the string is a numeric string, False otherwise.
     |      
     |      A string is numeric if all characters in the string are numeric and there is at
     |      least one character in the string.
     |  
     |  isprintable(self, /)
     |      Return True if the string is printable, False otherwise.
     |      
     |      A string is printable if all of its characters are considered printable in
     |      repr() or if it is empty.
     |  
     |  isspace(self, /)
     |      Return True if the string is a whitespace string, False otherwise.
     |      
     |      A string is whitespace if all characters in the string are whitespace and there
     |      is at least one character in the string.
     |  
     |  istitle(self, /)
     |      Return True if the string is a title-cased string, False otherwise.
     |      
     |      In a title-cased string, upper- and title-case characters may only
     |      follow uncased characters and lowercase characters only cased ones.
     |  
     |  isupper(self, /)
     |      Return True if the string is an uppercase string, False otherwise.
     |      
     |      A string is uppercase if all cased characters in the string are uppercase and
     |      there is at least one cased character in the string.
     |  
     |  join(self, iterable, /)
     |      Concatenate any number of strings.
     |      
     |      The string whose method is called is inserted in between each given string.
     |      The result is returned as a new string.
     |      
     |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
     |  
     |  ljust(self, width, fillchar=' ', /)
     |      Return a left-justified string of length width.
     |      
     |      Padding is done using the specified fill character (default is a space).
     |  
     |  lower(self, /)
     |      Return a copy of the string converted to lowercase.
     |  
     |  lstrip(self, chars=None, /)
     |      Return a copy of the string with leading whitespace removed.
     |      
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  partition(self, sep, /)
     |      Partition the string into three parts using the given separator.
     |      
     |      This will search for the separator in the string.  If the separator is found,
     |      returns a 3-tuple containing the part before the separator, the separator
     |      itself, and the part after it.
     |      
     |      If the separator is not found, returns a 3-tuple containing the original string
     |      and two empty strings.
     |  
     |  replace(self, old, new, count=-1, /)
     |      Return a copy with all occurrences of substring old replaced by new.
     |      
     |        count
     |          Maximum number of occurrences to replace.
     |          -1 (the default value) means replace all occurrences.
     |      
     |      If the optional argument count is given, only the first count occurrences are
     |      replaced.
     |  
     |  rfind(...)
     |      S.rfind(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  rindex(...)
     |      S.rindex(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the substring is not found.
     |  
     |  rjust(self, width, fillchar=' ', /)
     |      Return a right-justified string of length width.
     |      
     |      Padding is done using the specified fill character (default is a space).
     |  
     |  rpartition(self, sep, /)
     |      Partition the string into three parts using the given separator.
     |      
     |      This will search for the separator in the string, starting at the end. If
     |      the separator is found, returns a 3-tuple containing the part before the
     |      separator, the separator itself, and the part after it.
     |      
     |      If the separator is not found, returns a 3-tuple containing two empty strings
     |      and the original string.
     |  
     |  rsplit(self, /, sep=None, maxsplit=-1)
     |      Return a list of the words in the string, using sep as the delimiter string.
     |      
     |        sep
     |          The delimiter according which to split the string.
     |          None (the default value) means split according to any whitespace,
     |          and discard empty strings from the result.
     |        maxsplit
     |          Maximum number of splits to do.
     |          -1 (the default value) means no limit.
     |      
     |      Splits are done starting at the end of the string and working to the front.
     |  
     |  rstrip(self, chars=None, /)
     |      Return a copy of the string with trailing whitespace removed.
     |      
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  split(self, /, sep=None, maxsplit=-1)
     |      Return a list of the words in the string, using sep as the delimiter string.
     |      
     |      sep
     |        The delimiter according which to split the string.
     |        None (the default value) means split according to any whitespace,
     |        and discard empty strings from the result.
     |      maxsplit
     |        Maximum number of splits to do.
     |        -1 (the default value) means no limit.
     |  
     |  splitlines(self, /, keepends=False)
     |      Return a list of the lines in the string, breaking at line boundaries.
     |      
     |      Line breaks are not included in the resulting list unless keepends is given and
     |      true.
     |  
     |  startswith(...)
     |      S.startswith(prefix[, start[, end]]) -> bool
     |      
     |      Return True if S starts with the specified prefix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      prefix can also be a tuple of strings to try.
     |  
     |  strip(self, chars=None, /)
     |      Return a copy of the string with leading and trailing whitespace remove.
     |      
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  swapcase(self, /)
     |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
     |  
     |  title(self, /)
     |      Return a version of the string where each word is titlecased.
     |      
     |      More specifically, words start with uppercased characters and all remaining
     |      cased characters have lower case.
     |  
     |  translate(self, table, /)
     |      Replace each character in the string using the given translation table.
     |      
     |        table
     |          Translation table, which must be a mapping of Unicode ordinals to
     |          Unicode ordinals, strings, or None.
     |      
     |      The table must implement lookup/indexing via __getitem__, for instance a
     |      dictionary or list.  If this operation raises LookupError, the character is
     |      left untouched.  Characters mapped to None are deleted.
     |  
     |  upper(self, /)
     |      Return a copy of the string converted to uppercase.
     |  
     |  zfill(self, width, /)
     |      Pad a numeric string with zeros on the left, to fill a field of the given width.
     |      
     |      The string is never truncated.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  maketrans(x, y=None, z=None, /)
     |      Return a translation table usable for str.translate().
     |      
     |      If there is only one argument, it must be a dictionary mapping Unicode
     |      ordinals (integers) or characters to Unicode ordinals, strings or None.
     |      Character keys will be then converted to ordinals.
     |      If there are two arguments, they must be strings of equal length, and
     |      in the resulting dictionary, each character in x will be mapped to the
     |      character at the same position in y. If there is a third argument, it
     |      must be a string, whose characters will be mapped to None in the result.
    



```python
# Your code here
```


```python
#__SOLUTION__
example.swapcase().replace('0','o').strip().replace('?','!')
```




    'Hello, World!'



# 4. Describe the relationship of classes and objects, and learn to code classes

Each object is an instance of a **class** that defines a bundle of attributes and functions (now, as proprietary to the object type, called *methods*), the point being that **every object of that class will automatically have those proprietary attributes and methods**.

A class is like a blueprint that describes how to create a specific type of object.

![blueprint](img/blueprint.jpeg)


# Classes 


```python
class CPSSchool:
    """Chicago Public School Object"""
    pass # This called a stub. 
```

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




    __main__.Car




```python
# We can give describe the ferrari as having four wheels

ferrari.wheels = 4
ferrari.wheels
```




    4




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




    4




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




    4




```python
# But a ferrari does not have 4 doors! 
# These attributes can be overwritten 

ferrari.doors = 2
ferrari.doors
```




    2



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

    Beep beep
    Beep beep


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

    4
    True


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

    4
    False


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


      File "<ipython-input-154-6046029021d3>", line 2
        civic = Car(doors = 4, True)
                              ^
    SyntaxError: positional argument follows keyword argument




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

    peaceful
    Beep beep
    pissed


# Pair

 Let's bring our knowledge together, and in pairs, code out the following:

We have an attribute `moving` which indicates, with a boolean, whether the car is moving or not.  

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

    False
    Whoa, that's some acceleration!
    True
    Screeech!
    False


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

    Beep beep





    4




```python
#  Then we can add more attributes
class ElectricCar(Car):
    """Automotive object"""
    
    # default arguments included now in __init__
    def __init__(self, hybrid=False):
        super().__init__()
        self.hybrid = True 
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

    False
    Whirrrrrr
    serene


## 6. Important data science tools through the lens of objects: 

We are becomming more and more familiar with a series of methods with names such as fit or fit_transform.

After instantiating an instance of a Standard Scaler, Linear Regression model, or One Hot Encoder, we use fit to learn about the dataset and save what is learned. What is learned is saved in the attributes.

### 1. Standard Scaler 

The standard scaler takes a series and, for each element, computes the absolute value of the difference from the point to the mean of the series, and divides by the standard deviation.

$\Large z = \frac{|x - \mu|}{s}$

What attributes and methods are available for a Standard Scaler object? Let's check out the code on [GitHub](https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_data.py)!

## Attributes

### `.scale_`


```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# instantiate a standard scaler object
ss = StandardScaler()

# We can instantiate as many scaler objects as we want
maxs_scaler = StandardScaler()
```


```python
# Let's create a dataframe with two series

series_1 = np.random.normal(3,1,1000)
print(series_1.mean())
print(series_1.std())
```

    2.934646609831092
    0.982546083453659


When we fit the standard scaler, it studies the object passed to it, and saves what is learned in its instance attributes


```python
ss.fit(series_1.reshape(-1,1))

# standard deviation is saved in the attribute scale_
ss.scale_
```




    array([0.98254608])




```python
# mean is saved into the attribut mean
ss.mean_
```




    array([2.93464661])




```python
# Knowledge Check

# What value should I put into the standard scaler to make the equality below return 0

ss.transform([])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-172-66adfde57247> in <module>
          3 # What value should I put into the standard scaler to make the equality below return 0
          4 
    ----> 5 ss.transform([])
    

    ~/anaconda3/lib/python3.7/site-packages/sklearn/preprocessing/_data.py in transform(self, X, copy)
        793         X = check_array(X, accept_sparse='csr', copy=copy,
        794                         estimator=self, dtype=FLOAT_DTYPES,
    --> 795                         force_all_finite='allow-nan')
        796 
        797         if sparse.issparse(X):


    ~/anaconda3/lib/python3.7/site-packages/sklearn/utils/validation.py in check_array(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, warn_on_dtype, estimator)
        554                     "Reshape your data either using array.reshape(-1, 1) if "
        555                     "your data has a single feature or array.reshape(1, -1) "
    --> 556                     "if it contains a single sample.".format(array))
        557 
        558         # in the future np.flexible dtypes will be handled like object dtypes


    ValueError: Expected 2D array, got 1D array instead:
    array=[].
    Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.



```python
#__SOLUTION__
ss.transform([ss.mean_])
```




    array([[0.]])




```python
# we can then use these attributes to transform objects
np.random.seed(42)
random_numbers = np.random.normal(3,1, 2)
random_numbers
```




    array([3.49671415, 2.8617357 ])




```python
ss.transform(random_numbers.reshape(-1,1))
```




    array([[ 0.51708177],
           [-0.13592498]])




```python
# We can also use a scaler on a DataFrame
series_1 = np.random.normal(3,1,1000)
series_2 = np.random.uniform(0,100, 1000)
df_2 = pd.DataFrame([series_1, series_2]).T
ss_df = StandardScaler()
ss_df.fit_transform(df_2)

```




    array([[ 0.63918361, -1.63325007],
           [ 1.53240185,  1.50265028],
           [-0.260668  , -1.56258467],
           ...,
           [ 0.56254398, -1.61544876],
           [ 1.40620165, -1.36827099],
           [ 0.92178475, -0.56807826]])




```python
ss_df.transform([[5, 50]])
```




    array([[ 2.01911307, -0.00948621]])



## Pair Exercise: One-hot Encoder

Another object that you will use often is OneHotEncoder from sklearn. It is recommended over pd.get_dummies() because it can trained, with the learned informed stored in the attributes of the object.


```python
from sklearn.preprocessing import OneHotEncoder
```


```python
np.random.seed(42)
# Let's create a dataframe that has days of the week and number of orders. 

days = np.random.choice(['m','t', 'w','th','f','s','su'], 1000)
orders = np.random.randint(0,1000,1000)

df = pd.DataFrame([days, orders]).T
df.columns = ['days', 'orders']
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>days</th>
      <th>orders</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>su</td>
      <td>758</td>
    </tr>
    <tr>
      <th>1</th>
      <td>th</td>
      <td>105</td>
    </tr>
    <tr>
      <th>2</th>
      <td>f</td>
      <td>562</td>
    </tr>
    <tr>
      <th>3</th>
      <td>su</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>w</td>
      <td>132</td>
    </tr>
  </tbody>
</table>
</div>



Let's interact with an important parameters which we can pass when instantiating the OneHotEncoder object:` drop`.  

By dropping column, we avoid the [dummy variable trap](https://en.wikipedia.org/wiki/Dummy_variable_(statistics)).  

By passing `drop = True`, sklearn drops the first category it happens upon.  In this case, that is 'su'.  But what if we want to drop 'm'.  We can pass an array like object in as parameter to specify which column to drop.





```python
# Instantiate the OHE object with a param that tells it to drop Monday
ohe = None
```


```python
#__SOLUTION__
# Instantiate a OneHotEncoder object

ohe = OneHotEncoder(drop=['m'])
```


```python
# Now, fit_transform the days column of the dataframe

ohe_array = None
```


```python
#__SOLUTION__
ohe_matrix = ohe.fit_transform(df[['days']])
```


```python
# look at __dict__ and checkout drop_idx_
# did it do what you wanted it to do?
ohe.__dict__
```




    {'categories': 'auto',
     'sparse': True,
     'dtype': numpy.float64,
     'handle_unknown': 'error',
     'drop': array(['m'], dtype=object),
     'categories_': [array(['f', 'm', 's', 'su', 't', 'th', 'w'], dtype=object)],
     'drop_idx_': array([1])}




```python
# check out the categories_ attribute
ohe.categories_
```




    [array(['f', 'm', 's', 'su', 't', 'th', 'w'], dtype=object)]




```python
# Check out the object itself
ohe_matrix
```




    <1000x6 sparse matrix of type '<class 'numpy.float64'>'
    	with 844 stored elements in Compressed Sparse Row format>



It is a sparse matrix, which is a matrix that is composed mostly of zeros


```python
# We can convert it to an array like so
oh_df = pd.DataFrame.sparse.from_spmatrix(ohe_matrix)
```


```python
# Now, using the categories_ attribute, set the column names to the correct days of the week
# you can use drop_idx_ for this as well


```


```python
#__SOLUTION__
ohe_columns = list(ohe.categories_[0])
ohe_columns.pop(int(ohe.drop_idx_))
oh_df.columns = ohe_columns
oh_df.head()
oh_df.columns = ohe_columns
oh_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f</th>
      <th>s</th>
      <th>su</th>
      <th>t</th>
      <th>th</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Add the onehotencoded columns to the original df, and drop the days column

```


```python
#__SOLUTION__
# Now, add the onehotencoded columns to the original df, and drop the days column

df = df.join(oh_df).drop('days', axis=1)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>orders</th>
      <th>f</th>
      <th>s</th>
      <th>su</th>
      <th>t</th>
      <th>th</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>758</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>105</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>562</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>80</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>132</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>


