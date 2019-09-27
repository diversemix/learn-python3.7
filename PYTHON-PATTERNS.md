# Python Patterns

----

This is a collection of patterns and useful notes I've picked up along the way.

## Emulating a switch statement

This can be done with using a `dict` to map variables or functions:

```{python}
num_to_string = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(num_to_string[2])
```

## Overloading - singledispatch

Given the following example:

```{python}
class Animal:

    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        print(self.sound)

class Cow(Animal):

    def __init__(self):
        super().__init__('Moo')
        pass


class Sheep(Animal):

    def __init__(self):
        super().__init__('Baa')
        pass


class Pig(Animal):

    def __init__(self):
        super().__init__('Oink')
        pass


a = Pig()
a.speak()
```

Then to obey the SRP, if we wanted to implement a draw function (nothing to do
with the nature of an Animal). Then we could do this by overloading draw given
the type of animal, by adding code something like:

```{python}
from functools import singledispatch

@singledispatch
def draw(animal):
    raise TypeError("Don't know how to draw {!r}".format(animal))

@draw.register(Cow)
def _(animal):
    print(u"\U0001F404")

@draw.register(Sheep)
def _(animal):
    print(u"\U0001F411")

@draw.register(Pig)
def _(animal):
    print(u"\U0001F416")

p = Cow()
draw(p)
p.speak()
```

## Double Dispatch

You cannot use the `singledispatch` inside of a class as the first argument `self`
is always the same type. The solution is to call out to a function outside of the
class (decorated with `singledispatch`) and swap the arguments.

## DataDescriptors

Below is an example of two classes, one a `DataDescriptor` (i.e. it implements,
`__set__` and/or `__del__`) and one not as in this case it only implements
`__get__`.


```{python}

class DataDescriptor:

    def __get__(self, instance, owner):
        print("DataDescriptor.__get__({!r}, {!r}, {!r})"
              .format(self, instance, owner))

    def __set__(self, instance, value):
        print("DataDescriptor.__set__({!r}, {!r}, {!r})"
              .format(self, instance, value))


class NonDataDescriptor:

    def __get__(self, instance, owner):
        print("NonDataDescriptor.__get__({!r}, {!r}, {!r})"
              .format(self, instance, owner))


class Owner:

    a = DataDescriptor()
    b = NonDataDescriptor()

```

# Abstract Classes

First, very different from other languages...

