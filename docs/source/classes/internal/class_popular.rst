##################
API: Class Popular
##################
This class is used to access the **popular** photos on the ``PyPexels`` ``/popular/`` REST API.

It is returned as result from a call to ``PyPexels.popular(page, per_page)``


==========
Properties
==========
Properties exposed by the ``Popular`` class.

-----------------------------------------------------
**Popular.entries**
-----------------------------------------------------
    Iterator for the returned objects contained in this ``Popular`` instance.
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
        popular_photos_page = py_pexel.popular(per_page=40)
        for photo in popular_photos_page.entries:
            print(photo.id, photo.photographer, photo.url)
            # no need to specify per_page: will take from original object
            popular_photos_page = popular_photos_page.get_next_page()
        popular_results = py_pexel.popular(per_page=40)
        for photo in popular_results.entries:
            print(photo.id, photo.photographer, photo.url)

-----------------------------------------------------
**Popular.page**
-----------------------------------------------------
    Current popular photos page number.

    ==========  ========================================
    int         current popular photos page number
    ==========  ========================================

-----------------------------------------------------
**Popular.per_page**
-----------------------------------------------------
    Current popular photos per_page value.

    ==========  ========================================
    int         current popular photos per_page value
    ==========  ========================================

-----------------------------------------------------
**Popular.has_previous**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a previous page to navigate to or not.

    ==========  ========================================
    boolean     presence of previous page results
    ==========  ========================================

-----------------------------------------------------
**Popular.has_next**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a next page to navigate to or not.

    ==========  ========================================
    boolean     presence of next page results
    ==========  ========================================

-----------------------------------------------------
**Popular.body**
-----------------------------------------------------
    Returns JSON body of popular photos page.

    ==========  ========================================
    JSON        JSON converted body of results page
    ==========  ========================================

-----------------------------------------------------
**Popular.headers**
-----------------------------------------------------
    Returns response headers of popular photos page.

    ==========  ========================================
    dict        headers of results page
    ==========  ========================================

-----------------------------------------------------
**Popular.link_self**
-----------------------------------------------------
    Returns URL to current results page

    ==========  ========================================
    str         URL to current results page
    ==========  ========================================

-----------------------------------------------------
**Popular.link_next**
-----------------------------------------------------
    Returns URL to next results page

    ==========  ========================================
    str         URL to next results page
    ==========  ========================================

-----------------------------------------------------
**Popular.link_previous**
-----------------------------------------------------
    Returns URL to previous results page

    ==========  ========================================
    str         URL to previous results page
    ==========  ========================================

-----------------------------------------------------
**Popular.link_first**
-----------------------------------------------------
    Returns URL to first results page

    ==========  ========================================
    str         URL to first results page
    ==========  ========================================


.. note::  ``Popular.total_results`` always returns 0 (zero).
           ``Popular.link_last`` always points to the first page.


=======
Methods
=======
Methods exposed by the ``Popular`` class.

-----------------------------------------------------
**Popular.get_page()**
-----------------------------------------------------
    Returns the requested popular photos page with the current `query` and `per_page` parameters.
    The returned page may not contain `entries` if the page is out of boundaries.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **page**      number  required                     Page number to retrieve.
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Popular``
    ==========  ========================================================================

--------


-----------------------------------------------------
**Popular.get_next_page()**
-----------------------------------------------------
    Returns next available popular photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Popular`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.popular(query='red flowers', per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_next_page()

--------


-----------------------------------------------------
**Popular.get_previous_page()**
-----------------------------------------------------
    Returns previous available popular photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Popular`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.popular(query='red flowers', page=3, per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_previous_page()

--------


-----------------------------------------------------
**Popular.get_first_page()**
-----------------------------------------------------
    Returns first popular photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Popular`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.popular(query='red flowers', page=3, per_page=40)
        print 'Current page number %s' % search_results.page
        # To something with search_results

        # Go back to first page
        search_results = search_results.get_first_page():
        print 'Current page number %s' % search_results.page

--------

.. note::  ``Popular.get_last_page()`` always returns the first page.
