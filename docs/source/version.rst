Version
=======
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
    * Extend Travis and Tox test coverage to include Python 3.6, 3.7 and 3.8

    Note that using this library you still need to abide to Pexels Guidelines, which
    are explained on `Pexels API page <https://www.pexels.com/api/>`_
