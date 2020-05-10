################
API: Class Photo
################
This class is used to interact with individual ``Photo`` objects typically returned by ``PyPexels`` as part of either
``Search`` or ``Popular`` object entries.


==========
Properties
==========
Properties exposed by the ``Photo`` class.

'id', 'width', 'height', 'url', 'photographer', 'photographer_url', 'photographer_id', 'src', 'liked'

-----------------------------------------------------
**Photo.id**
-----------------------------------------------------
    Unique identifier for this photo

    ==========  ========================================
    int         Unique identifier for this photo
    ==========  ========================================

-----------------------------------------------------
**Photo.width**
-----------------------------------------------------
    Original image size width

    ==========  ========================================
    int         Original image size width
    ==========  ========================================

-----------------------------------------------------
**Photo.height**
-----------------------------------------------------
    Original image size height

    ==========  ========================================
    int         Original image size height
    ==========  ========================================

-----------------------------------------------------
**Photo.url**
-----------------------------------------------------
    URL location of Pexels web page for this photo

    ==========  ========================================
    str         Pexels.com page for this photo
    ==========  ========================================

-----------------------------------------------------
**Photo.photographer**
-----------------------------------------------------
    Name of photographer or photo source

    ==========  ========================================
    str         Name of photographer or photo source
    ==========  ========================================

-----------------------------------------------------
**Photo.photographer_url**
-----------------------------------------------------
    URL of photographer page on Pexels

    ==========  ========================================
    str         URL of photographer page on Pexels
    ==========  ========================================

-----------------------------------------------------
**Photo.photographer_id**
-----------------------------------------------------
    Unique identifier for this photographer

    ==========  ========================================
    int         Unique identifier for this photographer
    ==========  ========================================

-----------------------------------------------------
**Photo.src**
-----------------------------------------------------
    Dictionary with direct links to the image in different
    sizes and resolutions.

    ==========  =====================================================
    dict        links to the image in different sizes and resolutions
    ==========  =====================================================

    The next table details the key and their corresponding
    image size attributes.

    **Image formats**

    ==========  =====================================================================================================================
    Key         Description
    ==========  =====================================================================================================================
    original 	The size of the original image is given with the attributes width and height.
    large2x     This image has a maximum width of 1880px and a maximum height of 1300px. It has the aspect ratio of the original image.
    large 	    This image has a maximum width of 940px and a maximum height of 650px. It has the aspect ratio of the original image.
    medium 	    This image has a height of 350px and a flexible width. It has the aspect ratio of the original image.
    small 	    This image has a height of 130px and a flexible width. It has the aspect ratio of the original image.
    portrait 	This image has a width of 800px and a height of 1200px.
    landscape 	This image has a width of 1200px and height of 627px.
    tiny 	    This image has a width of 280px and height of 200px.
    ==========  =====================================================================================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        search_results = py_pexel.search(query='red flowers', per_page=40)
        for photo in search_results.entries:
            print(photo.id, photo.photographer, photo.url)
            print photo.src.get('large')
            print photo.src.get('tiny')


-----------------------------------------------------
**Photo.liked**
-----------------------------------------------------
    Unique identifier for this photographer

    ==========  ========================================
    bool        Whether liked or not by this API user
    ==========  ========================================


=======
Methods
=======
Methods exposed by the ``Photo`` class.

'get_attribution()'

----------------------------------------
**Photo.get_attribution(_format='str')**
----------------------------------------
    Generate and return a standard attribution string according to '_format' parameter.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    _format       string  optional                  Valid values: 'txt', 'html'
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ================================================
    **string**  Text or HTML standard attribution string.
    ==========  ================================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        # Retrieve a single photo, known by its ID
        photo = py_pexel.single_photo(photo_id=<ID>)
        print(photo.get_attribution('txt'))
        print(photo.get_attribution('html'))


