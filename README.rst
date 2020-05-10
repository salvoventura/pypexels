########
PyPexels
########
|Latest Version| |Docs Build Status| |Build Status| |Code Coverage| |Code Climate| |Landscape Io| |Say Thanks|

An open source Python wrapper for the `Pexels REST API <https://www.pexels.com/api/>`_.
The source code is available on GitHub at `https://github.com/salvoventura/pypexels <https://github.com/salvoventura/pypexels>`_.

.. note::  When using this library you still need to abide to Pexels Guidelines, which are explained on `Pexels API page <https://www.pexels.com/api/>`_


############
Installation
############
``PyPexels`` is available on `PyPI <https://pypi.python.org/pypi>`_ and thus can be installed with ``pip`` on most platforms.
::

    $ pip install pypexels

############
Dependencies
############
This library depends on `Requests <http://docs.python-requests.org>`_ to make - well - requests to the Pexels API.
This additional package should be automatically installed at installation time, or you can simply install it by:
::

    $ pip install requests

########
Examples
########
This example shows how the interaction with the paging functionality of the Pexels API is greatly abstracted and
simplified. The code below will iterate through all popular images, and print attributes for each photo in there.

.. code-block:: python

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

#############
Documentation
#############
Documentation is published on `ReadTheDocs <http://pypexels.readthedocs.io/>`_.


#######
Version
#######
**PyPexels v1.0.0rc1 (release candidate, v1)**

    This is the first release candidate for production ready 1.0.0 of PyPexels.
    Thanks to all the early adopters, there have been a number of improvements
    and bugfixes and now should be a good time to start the rc process.

    This release introduces some good functionality, in particular:

    * Support for Videos API: search, popular
    * Introduction of SinglePhoto and SingleVideo
      * This allows instantiating a `Photo` or `Video` object using a `photo_id` or `video_id`
    * Introduction of `get_attribution()` method on `Photo` and `Video` classes
      * This simplifies crediting the author
    * Fix some documentation issues
    * Extend Travis and Tox test coverage to include Python3.6, 3.7 and 3.8

**PyPexels v1.0.0b4 (beta, v4)**

    Fourth beta release introduces bugfix for Issue#7 AttributeError raised on Search.entries.
    REST API calls could fail silently making body an object of type None. With this fix,
    failing REST API calls will raise a PexelsError exception instead.


**PyPexels v1.0.0b3 (beta, v3)**

    Third beta release introduces support for `curated` and `random`.

    Note that using this library you still need to abide to Pexels Guidelines, which
    are explained on `Pexels API page <https://www.pexels.com/api/>`_


**PyPexels v1.0.0b2 (beta, v2)**

    Second beta release introduces Python3 support.

    Note that using this library you still need to abide to Pexels Guidelines, which
    are explained on `Pexels API page <https://www.pexels.com/api/>`_


**PyPexels v1.0.0b1 (beta, v1)**

    First release with wrappers around the two Pexels API for `search` and `popular`.

    Note that using this library you still need to abide to Pexels Guidelines, which
    are explained on `Pexels API page <https://www.pexels.com/api/>`_


#######
License
#######
PyPexels is released under the `MIT License <http://www.opensource.org/licenses/MIT>`_.


.. |Build Status| image:: https://travis-ci.org/salvoventura/pypexels.svg?branch=master
    :target: https://travis-ci.org/salvoventura/pypexels
    :alt: Build Status

.. |Docs Build Status| image:: https://readthedocs.org/projects/pypexels/badge/?version=latest
    :target: http://pypexels.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |Latest Version| image:: https://badge.fury.io/py/pypexels.svg
    :target: https://badge.fury.io/py/pypexels

.. |Code Coverage| image:: https://codecov.io/gh/salvoventura/pypexels/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/salvoventura/pypexels

.. |Code Climate| image:: https://codeclimate.com/github/salvoventura/pypexels/badges/gpa.svg
   :target: https://codeclimate.com/github/salvoventura/pypexels
   :alt: Code Climate

.. |Landscape Io| image:: https://landscape.io/github/salvoventura/pypexels/master/landscape.svg?style=flat
   :target: https://landscape.io/github/salvoventura/pypexels/master
   :alt: Code Health

.. |Say Thanks| image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/salvoventura
   :alt: Say Thanks
