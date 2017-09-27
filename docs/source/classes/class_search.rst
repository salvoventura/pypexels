#################
API: Class Search
#################
This class is used to access the results of a **search** on the ``PyPexels`` ``/search/`` REST API.

It is returned as result from a call to ``PyPexels.search(query, page, per_page)``


==========
Properties
==========
Properties exposed by the ``Search`` class.

-----------------------------------------------------
**Search.entries**
-----------------------------------------------------
    Returns an iterator for the returned objects contained in this ``Search`` instance.
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
        search_results = py_pexel.search(query='red flowers', per_page=40)
        for photo in search_results.entries:
            print(photo.id, photo.photographer, photo.url)

-----------------------------------------------------
**Search.page**
-----------------------------------------------------
    Current search results page number.

    ==========  ========================================
    int         current search results page number
    ==========  ========================================

-----------------------------------------------------
**Search.per_page**
-----------------------------------------------------
    Current search results per_page value.

    ==========  ========================================
    int         current search results per_page value
    ==========  ========================================

-----------------------------------------------------
**Search.total_results**
-----------------------------------------------------
    Total results count, number of photos found

    ==========  ===========================================
    int         total results count, number of photos found
    ==========  ===========================================

-----------------------------------------------------
**Search.has_previous**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a previous page to navigate to or not.

    ==========  ========================================
    boolean     presence of previous page results
    ==========  ========================================

-----------------------------------------------------
**Search.has_next**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a next page to navigate to or not.

    ==========  ========================================
    boolean     presence of next page results
    ==========  ========================================

-----------------------------------------------------
**Search.body**
-----------------------------------------------------
    Returns JSON body of search results page.

    ==========  ========================================
    JSON        JSON converted body of results page
    ==========  ========================================

-----------------------------------------------------
**Search.headers**
-----------------------------------------------------
    Returns response headers of search results page.

    ==========  ========================================
    dict        headers of results page
    ==========  ========================================

-----------------------------------------------------
**Search.link_self**
-----------------------------------------------------
    Returns URL to current results page

    ==========  ========================================
    str         URL to current results page
    ==========  ========================================

-----------------------------------------------------
**Search.link_next**
-----------------------------------------------------
    Returns URL to next results page

    ==========  ========================================
    str         URL to next results page
    ==========  ========================================

-----------------------------------------------------
**Search.link_previous**
-----------------------------------------------------
    Returns URL to previous results page

    ==========  ========================================
    str         URL to previous results page
    ==========  ========================================

-----------------------------------------------------
**Search.link_first**
-----------------------------------------------------
    Returns URL to first results page

    ==========  ========================================
    str         URL to first results page
    ==========  ========================================

-----------------------------------------------------
**Search.link_last**
-----------------------------------------------------
    Returns URL to last results page

    ==========  ========================================
    str         URL to last results page
    ==========  ========================================

=======
Methods
=======
Methods exposed by the ``Search`` class.

-----------------------------------------------------
**Search.get_page()**
-----------------------------------------------------
    Returns the requested search results page with the current `query` and `per_page` parameters.
    The returned page may not contain `entries` if the page is out of boundaries.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **page**      number  required                     Page number to retrieve.
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Search``
    ==========  ========================================================================


-----------------------------------------------------
**Search.get_next_page()**
-----------------------------------------------------
    Returns next available search results page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Search`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.search(query='red flowers', per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_next_page()

--------


-----------------------------------------------------
**Search.get_previous_page()**
-----------------------------------------------------
    Returns previous available search results page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Search`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.search(query='red flowers', page=3, per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_previous_page()

--------


-----------------------------------------------------
**Search.get_first_page()**
-----------------------------------------------------
    Returns first search results page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Search`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.search(query='red flowers', page=3, per_page=40)
        print 'Current page number %s' % search_results.page
        # To something with search_results

        # Go back to first page
        search_results = search_results.get_first_page():
        print 'Current page number %s' % search_results.page

--------


-----------------------------------------------------
**Search.get_last_page()**
-----------------------------------------------------
    Returns last search results page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Search`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.search(query='red flowers', per_page=40)

        # Go to last results page
        search_results = search_results.get_last_page():
        print 'Current page number %s' % search_results.page

