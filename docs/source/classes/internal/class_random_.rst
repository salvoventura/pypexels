#################
API: Class Random
#################
This class is used to emulate a **random** API using the ``PyPexels`` ``/curated/`` REST API.

It is returned as result from a call to ``PyPexels.random(per_page)``


==========
Properties
==========
Properties exposed by the ``Random`` class.

-----------------------------------------------------
**Random.entries**
-----------------------------------------------------
    Returns an iterator for the returned objects contained in this ``Random`` instance.
    Each entry will be an instance of class ``Photo``.

    ==========  ========================================
    iterator    each time an instance of class ``Photo``
    ==========  ========================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        random_results = py_pexel.random(per_page=10)
        for photo in random_results.entries:
            print(photo.id, photo.photographer, photo.url)


-----------------------------------------------------
**Random.per_page**
-----------------------------------------------------
    Current random results per_page value.

    ==========  ========================================
    int         current random results per_page value
    ==========  ========================================

-----------------------------------------------------
**Random.has_previous**
-----------------------------------------------------
    Returns always boolean **False**

    ==========  ========================================
    boolean     presence of previous page results
    ==========  ========================================

-----------------------------------------------------
**Random.has_next**
-----------------------------------------------------
    Returns always boolean **True**

    ==========  ========================================
    boolean     presence of next page results
    ==========  ========================================



------------------
**IMPORTANT NOTE**
------------------
Although this class will expose additional methods and properties from the ``PyPexels.Curated`` class, you should only
rely upon and make use of the methods and properties listed above. Remember, this is a `convenience` class that provides
some uniformity in behavior while emulating a random image generator. If you need to fully control the content and
behavior of the classes, then revert to use ``PyPexels.Curated`` class, with ``per_page=1`` and ``page=randint()`` value
directly.

