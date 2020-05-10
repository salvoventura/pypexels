######################
API: Class SingleVideo
######################
This class is used to create an individual ``SingleVideo`` objects from its ID.


==========
Properties
==========
Properties exposed by the ``SingleVideo`` class.

'entries'

-----------------------------------------------------
**SingleVideo.entries**
-----------------------------------------------------
    Iterator for the returned objects contained in this ``SingleVideo`` instance.
    Each entry will be an instance of class ``Video``.

    **Note** You should not use this class directly. Use PyPexels.single_video() instead.

    ==========  ========================================
    iterator    each time an instance of class ``Video``
    ==========  ========================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        video = py_pexel.single_video(video_id=<ID>)
        print(video.id, video.user.get('name'), video.url)

