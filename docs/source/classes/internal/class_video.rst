################
API: Class Video
################
This class is used to interact with individual ``Video`` objects typically returned by ``PyPexels`` as part of either
``VideosSearch`` or ``VideosPopular`` object entries.


==========
Properties
==========
Properties exposed by the ``Video`` class.

'id', 'width', 'height', 'url', 'image', 'full_res', 'tags', 'duration', 'user', 'video_files', 'video_pictures'.

-----------------------------------------------------
**Video.id**
-----------------------------------------------------
    Unique identifier for this photo

    ==========  ========================================
    int         Unique identifier for this video
    ==========  ========================================

-----------------------------------------------------
**Video.width**
-----------------------------------------------------
    Original video size width

    ==========  ========================================
    int         Original video size width
    ==========  ========================================

-----------------------------------------------------
**Video.height**
-----------------------------------------------------
    Original video size height

    ==========  ========================================
    int         Original video size height
    ==========  ========================================

-----------------------------------------------------
**Video.url**
-----------------------------------------------------
    URL location of Pexels web page for this video

    ==========  ========================================
    str         Pexels.com page for this video
    ==========  ========================================

-----------------------------------------------------
**Video.image**
-----------------------------------------------------
    URL location of Pexels front image for this video

    ==========  ========================================
    str         Pexels.com front image for this video
    ==========  ========================================

-----------------------------------------------------
**Video.full_res**
-----------------------------------------------------
    Full resolution

    ==========  ========================================
    null        Undocumented/unused
    ==========  ========================================

-----------------------------------------------------
**Video.tags**
-----------------------------------------------------
    Tags (unused?)

    ==========  ========================================
    list        List of tags (str)
    ==========  ========================================

-----------------------------------------------------
**Video.duration**
-----------------------------------------------------
    Duration of video in seconds

    ==========  ========================================
    int         Duration of video in seconds
    ==========  ========================================

-----------------------------------------------------
**Video.user**
-----------------------------------------------------
    Information about the user uploading this video.

    ============  =======================================
    dict          Information of user uploading the video
    ============  =======================================

-----------------------------------------------------
**Video.video_files**
-----------------------------------------------------
    List of videos generated from resampling/resizing the original.
    Each entry is a dict with keys (id, quality, file_type, width, height, link).

    ==========  ========================================
    list        List of resampled video files
    ==========  ========================================

-----------------------------------------------------
**Video.video_pictures**
-----------------------------------------------------
    DEPRECATED


=======
Methods
=======
Methods exposed by the ``Video`` class.

'get_attribution()'

----------------------------------------
**Video.get_attribution(_format='str')**
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

        # Retrieve a single video, known by its ID
        video = py_pexel.single_video(video_id=<ID>)
        print(video.get_attribution('txt'))
        print(video.get_attribution('html'))

