##################
API: Class Curated
##################
This class is used to access the **curated** photos on the ``PyPexels`` ``/curated/`` REST API.

It is returned as result from a call to ``PyPexels.curated(page, per_page)``


==========
Properties
==========
Properties exposed by the ``Curated`` class.

-----------------------------------------------------
**Curated.entries**
-----------------------------------------------------
    Iterator for the returned objects contained in this ``Curated`` instance.
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
        curated_photos_page = py_pexel.curated(per_page=40)
        for photo in curated_photos_page.entries:
            print(photo.id, photo.photographer, photo.url)
            # no need to specify per_page: will take from original object
            curated_photos_page = curated_photos_page.get_next_page()
        curated_results = py_pexel.curated(per_page=40)
        for photo in curated_results.entries:
            print(photo.id, photo.photographer, photo.url)

-----------------------------------------------------
**Curated.page**
-----------------------------------------------------
    Current curated photos page number.

    ==========  ========================================
    int         current curated photos page number
    ==========  ========================================

-----------------------------------------------------
**Curated.per_page**
-----------------------------------------------------
    Current curated photos per_page value.

    ==========  ========================================
    int         current curated photos per_page value
    ==========  ========================================

-----------------------------------------------------
**Curated.has_previous**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a previous page to navigate to or not.

    ==========  ========================================
    boolean     presence of previous page results
    ==========  ========================================

-----------------------------------------------------
**Curated.has_next**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a next page to navigate to or not.

    ==========  ========================================
    boolean     presence of next page results
    ==========  ========================================

-----------------------------------------------------
**Curated.body**
-----------------------------------------------------
    Returns JSON body of curated photos page.

    ==========  ========================================
    JSON        JSON converted body of results page
    ==========  ========================================

-----------------------------------------------------
**Curated.headers**
-----------------------------------------------------
    Returns response headers of curated photos page.

    ==========  ========================================
    dict        headers of results page
    ==========  ========================================

-----------------------------------------------------
**Curated.link_self**
-----------------------------------------------------
    Returns URL to current results page

    ==========  ========================================
    str         URL to current results page
    ==========  ========================================

-----------------------------------------------------
**Curated.link_next**
-----------------------------------------------------
    Returns URL to next results page

    ==========  ========================================
    str         URL to next results page
    ==========  ========================================

-----------------------------------------------------
**Curated.link_previous**
-----------------------------------------------------
    Returns URL to previous results page

    ==========  ========================================
    str         URL to previous results page
    ==========  ========================================

-----------------------------------------------------
**Curated.link_first**
-----------------------------------------------------
    Returns URL to first results page

    ==========  ========================================
    str         URL to first results page
    ==========  ========================================


.. note::  ``curated.total_results`` always returns 0 (zero).
           ``curated.link_last`` always points to the first page.


=======
Methods
=======
Methods exposed by the ``Curated`` class.

-----------------------------------------------------
**Curated.get_page()**
-----------------------------------------------------
    Returns the requested curated photos page with the current `query` and `per_page` parameters.
    The returned page may not contain `entries` if the page is out of boundaries.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **page**      number  required                     Page number to retrieve.
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Curated``
    ==========  ========================================================================

--------


-----------------------------------------------------
**Curated.get_next_page()**
-----------------------------------------------------
    Returns next available curated photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Curated`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.curated(query='red flowers', per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_next_page()

--------


-----------------------------------------------------
**Curated.get_previous_page()**
-----------------------------------------------------
    Returns previous available curated photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Curated`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.curated(query='red flowers', page=3, per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_previous_page()

--------


-----------------------------------------------------
**Curated.get_first_page()**
-----------------------------------------------------
    Returns first curated photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Curated`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.curated(query='red flowers', page=3, per_page=40)
        print 'Current page number %s' % search_results.page
        # To something with search_results

        # Go back to first page
        search_results = search_results.get_first_page():
        print 'Current page number %s' % search_results.page

--------

.. note::  ``curated.get_last_page()`` always returns the first page.
