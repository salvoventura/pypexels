# PyPexels

[![Latest
Version](https://badge.fury.io/py/pypexels.svg)](https://badge.fury.io/py/pypexels)
[![Documentation
Status](https://readthedocs.org/projects/pypexels/badge/?version=latest)](http://pypexels.readthedocs.io/en/latest/?badge=latest)
[![Build
Status](https://travis-ci.org/salvoventura/pypexels.svg?branch=master)](https://travis-ci.org/salvoventura/pypexels)
[![Code
Coverage](https://codecov.io/gh/salvoventura/pypexels/branch/master/graph/badge.svg)](https://codecov.io/gh/salvoventura/pypexels)
[![Code
Climate](https://codeclimate.com/github/salvoventura/pypexels/badges/gpa.svg)](https://codeclimate.com/github/salvoventura/pypexels)
[![Code
Health](https://landscape.io/github/salvoventura/pypexels/master/landscape.svg?style=flat)](https://landscape.io/github/salvoventura/pypexels/master)
[![Say
Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/salvoventura)

An open source Python wrapper for the [Pexels REST
API](https://www.pexels.com/api/). The source code is available on
GitHub at <https://github.com/salvoventura/pypexels>.

<div class="note">

<div class="admonition-title">

Note

</div>

When using this library you still need to abide to Pexels Guidelines,
which are explained on [Pexels API page](https://www.pexels.com/api/)

</div>

# Installation

`PyPexels` is available on [PyPI](https://pypi.python.org/pypi) and thus
can be installed with `pip` on most platforms. :

    $ pip install pypexels

# Dependencies

This library depends on [Requests](http://docs.python-requests.org) to
make - well - requests to the Pexels API. This additional package should
be automatically installed at installation time, or you can simply
install it by: :

    $ pip install requests

# Examples

This example shows how the interaction with the paging functionality of
the Pexels API is greatly abstracted and simplified. The code below will
iterate through all popular images, and print attributes for each photo
in there.

``` sourceCode python
from pypexels import PyPexels
api_key = 'YOUR_API_KEY'

# instantiate PyPexels object
py_pexels = PyPexels(api_key=api_key)

popular_photos = py_pexels.popular(per_page=30)
while popular_photos.has_next:
    for photo in popular_photos.entries:
        print(photo.id, photo.photographer, photo.url)
    # no need to specify per_page: will take from original object
    popular_photos = popular_photos.get_next_page()
```

# Documentation

Documentation is published on
[ReadTheDocs](http://pypexels.readthedocs.io/).

# Version

**PyPexels v1.0.0b1 (beta, v1)**

> First release with wrappers around the two Pexels API for search and
> popular.
> 
> Note that using this library you still need to abide to Pexels
> Guidelines, which are explained on [Pexels API
> page](https://www.pexels.com/api/)

# License

PyPexels is released under the [MIT
License](http://www.opensource.org/licenses/MIT).
