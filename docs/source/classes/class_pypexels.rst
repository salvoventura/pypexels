###################
API: Class PyPexels
###################
This is the main class used to interact with the ``Pexels`` REST API.

=======================
**PyPexels(api_key)**
=======================
    Create an instance of class ``PyPexels``.
    The ``api_key`` parameter is required.
    API keys can be obtained from `Pexels API page <https://www.pexels.com/api/>`_.

    **Parameters**

    ===============  ======  ========================  ====================================
    Argument         Type    Optional/Required         Notes
    ===============  ======  ========================  ====================================
    **api_key**      string  required                  Your API key
    **api_version**  string  optional                  API version to use. Default: 'v1'
    ===============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``PyPexels``
    ==========  =======================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

---------


=======
Methods
=======
Methods exposed by the ``PyPexels`` class.

-----------------------------------------------------
**PyPexels.popular(page, per_page)**
-----------------------------------------------------
    Allows to list ``popular`` images from PyPexels.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 15)       Number of items per page (max: 40)
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Popular``
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        popular_photos = py_pexel.popular(per_page=40)
        for photo in popular_photos.entries:
            print(photo.id, photo.photographer, photo.url)


-----------------------------------------------------
**PyPexels.search(query, page, per_page)**
-----------------------------------------------------
    Allows to perform ``search`` based on a string query.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **query**     string  required                     Search terms
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 15)       Number of items per page (max: 40)
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Search``
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        search_photos = py_pexel.search(query='red flowers', per_page=40)
        for photo in search_photos.entries:
            print(photo.id, photo.photographer, photo.url)

