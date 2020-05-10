#######################
API: Class VideosSearch
#######################
This class is used to access the results of a **search** on the ``PyPexels`` ``/videos/search/`` REST API.

It is returned as result from a call to ``PyPexels.videos_search(query, page, per_page)``


==========
Properties
==========
Properties exposed by the ``VideosSearch`` class.

-----------------------------------------------------
**VideoSearch.entries**
-----------------------------------------------------
    Returns an iterator for the returned objects contained in this ``VideosSearch`` instance.
    Each entry will be an instance of class ``Video``.

    ==========  ========================================
    iterator    each time an instance of class ``Video``
    ==========  ========================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.video_search(query='red flowers', per_page=40)
        for video in search_results.entries:
            print(video.id, video.user.get('name'), video.url)

-----------------------------------------------------
**VideoSearch.page**
-----------------------------------------------------
    Current search results page number.

    ==========  ========================================
    int         current search results page number
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.per_page**
-----------------------------------------------------
    Current search results per_page value.

    ==========  ========================================
    int         current search results per_page value
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.total_results**
-----------------------------------------------------
    Total results count, number of photos found

    ==========  ===========================================
    int         total results count, number of photos found
    ==========  ===========================================

-----------------------------------------------------
**VideoSearch.has_previous**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a previous page to navigate to or not.

    ==========  ========================================
    boolean     presence of previous page results
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.has_next**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a next page to navigate to or not.

    ==========  ========================================
    boolean     presence of next page results
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.body**
-----------------------------------------------------
    Returns JSON body of search results page.

    ==========  ========================================
    JSON        JSON converted body of results page
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.headers**
-----------------------------------------------------
    Returns response headers of search results page.

    ==========  ========================================
    dict        headers of results page
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.link_self**
-----------------------------------------------------
    Returns URL to current results page

    ==========  ========================================
    str         URL to current results page
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.link_next**
-----------------------------------------------------
    Returns URL to next results page

    ==========  ========================================
    str         URL to next results page
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.link_previous**
-----------------------------------------------------
    Returns URL to previous results page

    ==========  ========================================
    str         URL to previous results page
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.link_first**
-----------------------------------------------------
    Returns URL to first results page

    ==========  ========================================
    str         URL to first results page
    ==========  ========================================

-----------------------------------------------------
**VideoSearch.link_last**
-----------------------------------------------------
    Returns URL to last results page

    ==========  ========================================
    str         URL to last results page
    ==========  ========================================

=======
Methods
=======
Methods exposed by the ``VideosSearch`` class.

-----------------------------------------------------
**VideoSearch.get_page()**
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
    **Object**  Instance of class ``VideosSearch``
    ==========  ========================================================================


-----------------------------------------------------
**VideoSearch.get_next_page()**
-----------------------------------------------------
    Returns next available search results page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``VideosSearch`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.video_search(query='red flowers', per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_next_page()

--------


-----------------------------------------------------
**VideoSearch.get_previous_page()**
-----------------------------------------------------
    Returns previous available search results page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``VideosSearch`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.video_search(query='red flowers', page=3, per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_previous_page()

--------


-----------------------------------------------------
**VideoSearch.get_first_page()**
-----------------------------------------------------
    Returns first search results page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``VideosSearch`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.video_search(query='red flowers', page=3, per_page=40)
        print 'Current page number %s' % search_results.page
        # To something with search_results

        # Go back to first page
        search_results = search_results.get_first_page():
        print 'Current page number %s' % search_results.page

--------


-----------------------------------------------------
**VideoSearch.get_last_page()**
-----------------------------------------------------
    Returns last search results page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``VideosSearch`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.video_search(query='red flowers', per_page=40)

        # Go to last results page
        search_results = search_results.get_last_page():
        print 'Current page number %s' % search_results.page

