
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




    str




```python
type('')

```




    str




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




    5.0




```python
help(int)
```

    Help on class int in module builtins:
    
    class int(object)
     |  int(x=0) -> integer
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
     |  __format__(...)
     |      default object formatter
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(...)
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
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
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
     |  __sizeof__(...)
     |      Returns size in memory, in bytes
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
     |  bit_length(...)
     |      int.bit_length() -> int
     |      
     |      Number of bits necessary to represent self in binary.
     |      >>> bin(37)
     |      '0b100101'
     |      >>> (37).bit_length()
     |      6
     |  
     |  conjugate(...)
     |      Returns self, the complex conjugate of any int.
     |  
     |  from_bytes(...) from builtins.type
     |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
     |      
     |      Return the integer represented by the given array of bytes.
     |      
     |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument indicates whether two's complement is
     |      used to represent the integer.
     |  
     |  to_bytes(...)
     |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
     |      
     |      Return an array of bytes representing an integer.
     |      
     |      The integer is represented using length bytes.  An OverflowError is
     |      raised if the integer is not representable with the given number of
     |      bytes.
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument determines whether two's complement is
     |      used to represent the integer.  If signed is False and a negative integer
     |      is given, an OverflowError is raised.
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
     |  __format__(...)
     |      S.__format__(format_spec) -> str
     |      
     |      Return a formatted version of S as described by format_spec.
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
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
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
     |  __sizeof__(...)
     |      S.__sizeof__() -> size of S in memory, in bytes
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  capitalize(...)
     |      S.capitalize() -> str
     |      
     |      Return a capitalized version of S, i.e. make the first character
     |      have upper case and the rest lower case.
     |  
     |  casefold(...)
     |      S.casefold() -> str
     |      
     |      Return a version of S suitable for caseless comparisons.
     |  
     |  center(...)
     |      S.center(width[, fillchar]) -> str
     |      
     |      Return S centered in a string of length width. Padding is
     |      done using the specified fill character (default is a space)
     |  
     |  count(...)
     |      S.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of substring sub in
     |      string S[start:end].  Optional arguments start and end are
     |      interpreted as in slice notation.
     |  
     |  encode(...)
     |      S.encode(encoding='utf-8', errors='strict') -> bytes
     |      
     |      Encode S using the codec registered for encoding. Default encoding
     |      is 'utf-8'. errors may be given to set a different error
     |      handling scheme. Default is 'strict' meaning that encoding errors raise
     |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
     |      'xmlcharrefreplace' as well as any other name registered with
     |      codecs.register_error that can handle UnicodeEncodeErrors.
     |  
     |  endswith(...)
     |      S.endswith(suffix[, start[, end]]) -> bool
     |      
     |      Return True if S ends with the specified suffix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      suffix can also be a tuple of strings to try.
     |  
     |  expandtabs(...)
     |      S.expandtabs(tabsize=8) -> str
     |      
     |      Return a copy of S where all tab characters are expanded using spaces.
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
     |  isalnum(...)
     |      S.isalnum() -> bool
     |      
     |      Return True if all characters in S are alphanumeric
     |      and there is at least one character in S, False otherwise.
     |  
     |  isalpha(...)
     |      S.isalpha() -> bool
     |      
     |      Return True if all characters in S are alphabetic
     |      and there is at least one character in S, False otherwise.
     |  
     |  isdecimal(...)
     |      S.isdecimal() -> bool
     |      
     |      Return True if there are only decimal characters in S,
     |      False otherwise.
     |  
     |  isdigit(...)
     |      S.isdigit() -> bool
     |      
     |      Return True if all characters in S are digits
     |      and there is at least one character in S, False otherwise.
     |  
     |  isidentifier(...)
     |      S.isidentifier() -> bool
     |      
     |      Return True if S is a valid identifier according
     |      to the language definition.
     |      
     |      Use keyword.iskeyword() to test for reserved identifiers
     |      such as "def" and "class".
     |  
     |  islower(...)
     |      S.islower() -> bool
     |      
     |      Return True if all cased characters in S are lowercase and there is
     |      at least one cased character in S, False otherwise.
     |  
     |  isnumeric(...)
     |      S.isnumeric() -> bool
     |      
     |      Return True if there are only numeric characters in S,
     |      False otherwise.
     |  
     |  isprintable(...)
     |      S.isprintable() -> bool
     |      
     |      Return True if all characters in S are considered
     |      printable in repr() or S is empty, False otherwise.
     |  
     |  isspace(...)
     |      S.isspace() -> bool
     |      
     |      Return True if all characters in S are whitespace
     |      and there is at least one character in S, False otherwise.
     |  
     |  istitle(...)
     |      S.istitle() -> bool
     |      
     |      Return True if S is a titlecased string and there is at least one
     |      character in S, i.e. upper- and titlecase characters may only
     |      follow uncased characters and lowercase characters only cased ones.
     |      Return False otherwise.
     |  
     |  isupper(...)
     |      S.isupper() -> bool
     |      
     |      Return True if all cased characters in S are uppercase and there is
     |      at least one cased character in S, False otherwise.
     |  
     |  join(...)
     |      S.join(iterable) -> str
     |      
     |      Return a string which is the concatenation of the strings in the
     |      iterable.  The separator between elements is S.
     |  
     |  ljust(...)
     |      S.ljust(width[, fillchar]) -> str
     |      
     |      Return S left-justified in a Unicode string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  lower(...)
     |      S.lower() -> str
     |      
     |      Return a copy of the string S converted to lowercase.
     |  
     |  lstrip(...)
     |      S.lstrip([chars]) -> str
     |      
     |      Return a copy of the string S with leading whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  partition(...)
     |      S.partition(sep) -> (head, sep, tail)
     |      
     |      Search for the separator sep in S, and return the part before it,
     |      the separator itself, and the part after it.  If the separator is not
     |      found, return S and two empty strings.
     |  
     |  replace(...)
     |      S.replace(old, new[, count]) -> str
     |      
     |      Return a copy of S with all occurrences of substring
     |      old replaced by new.  If the optional argument count is
     |      given, only the first count occurrences are replaced.
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
     |  rjust(...)
     |      S.rjust(width[, fillchar]) -> str
     |      
     |      Return S right-justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  rpartition(...)
     |      S.rpartition(sep) -> (head, sep, tail)
     |      
     |      Search for the separator sep in S, starting at the end of S, and return
     |      the part before it, the separator itself, and the part after it.  If the
     |      separator is not found, return two empty strings and S.
     |  
     |  rsplit(...)
     |      S.rsplit(sep=None, maxsplit=-1) -> list of strings
     |      
     |      Return a list of the words in S, using sep as the
     |      delimiter string, starting at the end of the string and
     |      working to the front.  If maxsplit is given, at most maxsplit
     |      splits are done. If sep is not specified, any whitespace string
     |      is a separator.
     |  
     |  rstrip(...)
     |      S.rstrip([chars]) -> str
     |      
     |      Return a copy of the string S with trailing whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  split(...)
     |      S.split(sep=None, maxsplit=-1) -> list of strings
     |      
     |      Return a list of the words in S, using sep as the
     |      delimiter string.  If maxsplit is given, at most maxsplit
     |      splits are done. If sep is not specified or is None, any
     |      whitespace string is a separator and empty strings are
     |      removed from the result.
     |  
     |  splitlines(...)
     |      S.splitlines([keepends]) -> list of strings
     |      
     |      Return a list of the lines in S, breaking at line boundaries.
     |      Line breaks are not included in the resulting list unless keepends
     |      is given and true.
     |  
     |  startswith(...)
     |      S.startswith(prefix[, start[, end]]) -> bool
     |      
     |      Return True if S starts with the specified prefix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      prefix can also be a tuple of strings to try.
     |  
     |  strip(...)
     |      S.strip([chars]) -> str
     |      
     |      Return a copy of the string S with leading and trailing
     |      whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  swapcase(...)
     |      S.swapcase() -> str
     |      
     |      Return a copy of S with uppercase characters converted to lowercase
     |      and vice versa.
     |  
     |  title(...)
     |      S.title() -> str
     |      
     |      Return a titlecased version of S, i.e. words start with title case
     |      characters, all remaining cased characters have lower case.
     |  
     |  translate(...)
     |      S.translate(table) -> str
     |      
     |      Return a copy of the string S in which each character has been mapped
     |      through the given translation table. The table must implement
     |      lookup/indexing via __getitem__, for instance a dictionary or list,
     |      mapping Unicode ordinals to Unicode ordinals, strings, or None. If
     |      this operation raises LookupError, the character is left untouched.
     |      Characters mapped to None are deleted.
     |  
     |  upper(...)
     |      S.upper() -> str
     |      
     |      Return a copy of S converted to uppercase.
     |  
     |  zfill(...)
     |      S.zfill(width) -> str
     |      
     |      Pad a numeric string S with zeros on the left, to fill a field
     |      of the specified width. The string S is never truncated.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
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



# Fun Detour About How Python Works

Python is dynamically typed, meaning you don't have to instruct it as to what type of object your variable is.  
A variable is a pointer to where an object is stored in memory.


```python
# interesting side note about how variables operate in Python
```


```python
print(hex(id(x)))
```

    0x109bcc700



```python
y = 5
```


```python
print(hex(id(y)))
```

    0x109bcc700



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

    [1, 2]
    [1, 2, 3]



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
    price    3 non-null int64
    sqft     3 non-null int64
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
      <td>0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2</td>
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
      <td>0</td>
      <td>50</td>
      <td>1000</td>
    </tr>
    <tr>
      <td>1</td>
      <td>40</td>
      <td>950</td>
    </tr>
    <tr>
      <td>2</td>
      <td>30</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>



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




    __main__.Car




```python
# Try importing car_b's automotive object and check the output of type.
```


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


      File "<ipython-input-50-6046029021d3>", line 2
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
        super().__init__(self)
        self.hybrid = hybrid 
```


```python
volt = ElectricCar(hybrid=True)
volt.hybrid
volt.driver_mood
```




    'peaceful'




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

    3.0193320558223253
    0.9787262077473542


When we fit the standard scaler, it studies the object passed to it, and saves what is learned in its instance attributes


```python
ss.fit(series_1.reshape(-1,1))

# standard deviation is saved in the attribute scale_
ss.scale_
```




    array([0.97872621])




```python
# mean is saved into the attribute mean
ss.mean_
```




    array([3.01933206])



Then, we can use the transform method to transform every element in the array to the zscore corresponding to the mean and standard deviation learned after fit() was called on the array.


```python
ss.transform(series_1.reshape(-1,1))[:5]
```




    array([[ 0.48775857],
           [-0.1610219 ],
           [ 0.64201457],
           [ 1.53638248],
           [-0.25899524]])




```python
# let's double check the math by applying the z-score formula
(series_1[0]-ss.mean_)/ss.scale_
```




    array([0.48775857])




```python
# We can call fit and transform in one step as well

ss.fit_transform(series_1.reshape(-1,1))[:5]
```




    array([[ 0.48775857],
           [-0.1610219 ],
           [ 0.64201457],
           [ 1.53638248],
           [-0.25899524]])



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




    [0.48775857171297654,
     -0.16102190351705759,
     0.6420145667955479,
     1.53638248233551,
     -0.2589952415079247]




```python
#__SOLUTION__
print(mss.scale_)
print(ss.scale_[0])
```

    0.9787262077473544
    0.9787262077473542



```python
#__SOLUTION__
print(mss.mean_)
print(ss.mean_[0])
```

    3.0193320558223253
    3.0193320558223253

