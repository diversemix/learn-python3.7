# learn-python3.7
Learn what's new in python 3.7

## Installation

I followed [these instructions](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
to install on Ubuntu 18.04.

Don't forget to install pip
```
python3.7 -m pip install pip
```

I also had to upgrade `docker-compose` too [see here](https://docs.docker.com/compose/install/)

## Dataclass

https://www.python.org/dev/peps/pep-0557/
https://docs.python.org/3/library/dataclasses.html

I particularly like how you can do auto `id` fields -as often is done when using a database.

```
from dataclasses import dataclass, field, InitVar
import typing
import uuid

@dataclass(frozen=True, order=True)
class AuditEntry(object):
    some_internal_var: typing.ClassVar[int]

    id: uuid.UUID = field(compare=False, default_factory=uuid.uuid4, init=False)
    operation: str = field(compare=False)

```

## Breakpoint Function

https://www.python.org/dev/peps/pep-0553/

Now you can separate the debugger from the code by inserting the `breakpoint()` function in your code
and defining the debugger with the `PYTHONBREAKPOINT` environment variable.
Setting this to zero allows you not to stop on breakpoints at all.

Example you can use the interactive terminal debugger with:

```
sudo pip install pudb
PYTHONBREAKPOINT=pudb.set_trace
```

## Changes to Encoding

https://www.python.org/dev/peps/pep-0538/

## Time Module

https://www.python.org/dev/peps/pep-0564/

Resolution is now in nano-seconds (ns) since epoch. Makes calculations a whole lot more accurate than using floating point.
New functions typically end in `_ns` to denote the function is returning the time in ns.
For example: `clock_gettime_ns()`

## References

- [What's new in Python](https://docs.python.org/release/3.7.4/whatsnew/index.html)
- []