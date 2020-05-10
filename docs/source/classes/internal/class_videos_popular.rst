#######################
API: Class VideoPopular
#######################
This class is used to access the **popular** videos on the ``PyPexels`` ``/videos/popular/`` REST API.

It is returned as result from a call to ``PyPexels.videos_popular(page, per_page)``


==========
Properties
==========
Properties exposed by the ``VideosPopular`` class.

-----------------------------------------------------
**VideosPopular.entries**
-----------------------------------------------------
    Iterator for the returned objects contained in this ``VideosPopular`` instance.
    Each entry will be an instance of class ``Video``.

    ==========  =========================================
    iterator    each time an instance of class ``Videos``
    ==========  =========================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        popular_videos_page = py_pexel.videos_popular(per_page=40)
        while True:
            for video in popular_videos_page.entries:
                print(video.id, video.user.get('name'), video.url)
            if not popular_videos_page.has_next:
                break
            popular_videos_page = popular_videos_page.get_next_page()

-----------------------------------------------------
**VideosPopular.page**
-----------------------------------------------------
    Current popular photos page number.

    ==========  ========================================
    int         current popular photos page number
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.per_page**
-----------------------------------------------------
    Current popular photos per_page value.

    ==========  ========================================
    int         current popular photos per_page value
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.has_previous**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a previous page to navigate to or not.

    ==========  ========================================
    boolean     presence of previous page results
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.has_next**
-----------------------------------------------------
    Returns boolean **True** or **False** depending on whether the current results page
    has a next page to navigate to or not.

    ==========  ========================================
    boolean     presence of next page results
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.body**
-----------------------------------------------------
    Returns JSON body of popular photos page.

    ==========  ========================================
    JSON        JSON converted body of results page
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.headers**
-----------------------------------------------------
    Returns response headers of popular photos page.

    ==========  ========================================
    dict        headers of results page
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.link_self**
-----------------------------------------------------
    Returns URL to current results page

    ==========  ========================================
    str         URL to current results page
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.link_next**
-----------------------------------------------------
    Returns URL to next results page

    ==========  ========================================
    str         URL to next results page
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.link_previous**
-----------------------------------------------------
    Returns URL to previous results page

    ==========  ========================================
    str         URL to previous results page
    ==========  ========================================

-----------------------------------------------------
**VideosPopular.link_first**
-----------------------------------------------------
    Returns URL to first results page

    ==========  ========================================
    str         URL to first results page
    ==========  ========================================


.. note::  ``VideosPopular.total_results`` always returns 0 (zero).
           ``VideosPopular.link_last`` always points to the first page.


=======
Methods
=======
Methods exposed by the ``VideosPopular`` class.

-----------------------------------------------------
**VideosPopular.get_page()**
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
    **Object**  Instance of class ``VideosPopular``
    ==========  ========================================================================

--------


-----------------------------------------------------
**VideosPopular.get_next_page()**
-----------------------------------------------------
    Returns next available popular photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``VideosPopular`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.videos_popular(query='red flowers', per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_next_page()

--------


-----------------------------------------------------
**VideosPopular.get_previous_page()**
-----------------------------------------------------
    Returns previous available popular photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``VideosPopular`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.videos_popular(query='red flowers', page=3, per_page=40)
        while search_results is not None:
            print 'Current page number %s' % search_results.page
            search_results = search_results.get_previous_page()

--------


-----------------------------------------------------
**VideosPopular.get_first_page()**
-----------------------------------------------------
    Returns first popular photos page with the current `query`, `page`, and `per_page` parameters.
    Returns `None` if no page is available.

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``VideosPopular`` or `None`
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_results = py_pexel.videos_popular(query='red flowers', page=3, per_page=40)
        print 'Current page number %s' % search_results.page
        # To something with search_results

        # Go back to first page
        search_results = search_results.get_first_page():
        print 'Current page number %s' % search_results.page

--------

.. note::  ``VideosPopular.get_last_page()`` always returns the first page.
