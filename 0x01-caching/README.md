Curriculum <br>
**Short Specializations** <br>

# 0x01. Caching

`Back-end`

#### Concepts

_For this project, look at these concepts:_

* [Back-end concepts](https://www.intranet.alxswe.com/concepts/557)

## Background Context

In this project, you will learn different caching algorithms. <br>

## Resources

**Read or watch:**

* [Cache replacement policies - FIFO](https://www.en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
* [Cache replacement policies - LIFO](https://www.en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
* [Cache replacement policies - LRU](https://www.en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
* [Cache replacement policies - MRU](https://www.en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
* [Cache replacement policies - LFU](https://www.en.wikipedia.org/wiki/Cache_replacement_policies#Least_Frequently_Used_%28LFU%29)

## Requirements

* All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
* All files should end with a new line
* First line of files exactly `#!/usr/bin/env python3`
* Mandatory `README.md` file
* Code use the `pycodestyle` style (version 2.5.*)
* Length of file tested using `wc`
* All modules should be documented (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions (inside and outside a class) should be documented (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* A documentation is a real sentence explaining purpose of module, function, or method (length will be verified)

## More Info

### Parent class `BaseCaching`

All your classes must inherit from `BaseCaching` defined below: <br>

```python3
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

Class BaseCaching():
      """ BaseCaching defines:
      	- constants of your caching system
      	- where your data are stored (in a dictionary)
      """
      MAX_ITEM = 4

      def __init__(self):
      	  """ Initialize
	  """
	  self.cache_data = {}

      def print_cache(self):
      	  """ Print the cache
	  """
	  print("Current cache:")
	  for key in sorted(self.cache_data.keys()):
	      print("{}: {}".format(key, self.cache_data.get(key)))

      def put(self, key, item):
      	  """ Add an item in the cache
	  """
	  raise NotImplementedError("put must be implemented in your cache class")

      def get(self, key):
      	  """ Get an item by key
	  """
	  raise NotImplementedError("get must be implemented in your cache class")
```

### Finally...
