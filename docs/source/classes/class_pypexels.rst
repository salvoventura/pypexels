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


Methods related to Photos
=========================


-----------------------------------------------------
**PyPexels.popular(page, per_page)**
-----------------------------------------------------
    Allows to list ``popular`` images from Pexels.

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
            print(photo.id, photo.photographer, photo.url, photo.get_attribution('txt'))


-----------------------------------------------------
**PyPexels.curated(page, per_page)**
-----------------------------------------------------
    Allows to list ``curated`` images from Pexels.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 15)       Number of items per page (max: 40)
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Curated``
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        curated_photos = py_pexel.curated(per_page=40)
        for photo in curated_photos.entries:
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

-----------------------------------------------------
**PyPexels.random(page, per_page)**
-----------------------------------------------------
    Retrieves ``random`` images from Pexels.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 15)       Number of items per page (max: 40)
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Random``
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        random_photos_page = py_pexel.random(per_page=7)
        for photo in random_photos_page.entries:
            print(photo.id, photo.photographer, photo.url)


-----------------------------------------------------
**PyPexels.single_photo(photo_id)**
-----------------------------------------------------
    Retrieve a single photo, known by its ID.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **photo_id**  str     required                     Image to retrieve.
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Photo``
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        # Retrieve a single photo, known by its ID
        photo = py_pexel.single_photo(photo_id=415071)
        print(photo.id, photo.photographer, photo.url)
        print(photo.get_attribution('txt'))
        print(photo.get_attribution('html'))

---

Methods related to Videos
=========================

-----------------------------------------------------
**PyPexels.videos_popular(page, per_page)**
-----------------------------------------------------
    Allows to list ``popular`` videos from Pexels.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 15)       Number of items per page (max: 40)
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``VideosPopular``
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        popular_videos_page = py_pexel.videos_popular(per_page=40)
        while True:
            for video in popular_videos_page.entries:
                print(video.id, video.user.get('name'), video.url)
            if not popular_videos_page.has_next:
                break
            popular_videos_page = popular_videos_page.get_next_page()


-----------------------------------------------------
**PyPexels.videos_search(query, page, per_page)**
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
    **Object**  Instance of class ``VideosSearch``
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        while True:
            for video in search_videos_page.entries:
                print(video.id, video.user.get('name'), video.url)
            if not search_videos_page.has_next:
                break
            search_videos_page = search_videos_page.get_next_page()


-----------------------------------------------------
**PyPexels.single_video(video_id)**
-----------------------------------------------------
    Retrieve a single video, known by its ID.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **video_id**  str     required                     Video to retrieve.
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Video``
    ==========  ========================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        # Retrieve a single video, known by its ID
        video = py_pexel.single_video(video_id=415071)
        print(video.id, video.user.get('name'), video.url)
        print(video.get_attribution('txt'))
        print(video.get_attribution('html'))

