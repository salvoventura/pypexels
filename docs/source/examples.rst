########
Examples
########
These example shows how the interaction with the paging functionality of the Pexels API is greatly abstracted and
simplified.


=======
Popular
=======
The code below will iterate through all popular photos in pages of 30 items each, retrieve each photo
in there, and print some of their attributes.

.. code-block:: python

    from pypexels import PyPexels
    api_key = 'YOUR_API_KEY'

    # instantiate PyPexels object
    py_pexel = PyPexels(api_key=api_key)

    popular_photos = py_pexel.popular(per_page=30)
    while True:
        for photo in popular_photos.entries:
            print(photo.id, photo.photographer, photo.url)
        if not popular_photos.has_next:
            break
        popular_photos = popular_photos.get_next_page()


======
Search
======
The code below will perform a search based on a query string, then iterate through all the results pages of 40 photos
each, retrieve each photo in there, and print some of their attributes.

.. code-block:: python

    from pypexels import PyPexels
    api_key = 'YOUR_API_KEY'

    # instantiate PyPexels object
    py_pexel = PyPexels(api_key=api_key)

    search_results = py_pexel.search(query='red flowers', per_page=40)
    while True:
        for photo in search_results.entries:
            print(photo.id, photo.photographer, photo.url)
        if not search_results.has_next:
            break
        search_results = search_results.get_next_page()


======
Random
======
The code below will return random images. Use the parameter ``per_page`` to specify how many random images the iterator
will allow.

.. code-block:: python

    from pypexels import PyPexels
    api_key = 'YOUR_API_KEY'

    # instantiate PyPexels object
    py_pexel = PyPexels(api_key=api_key)

    random_photos_page = py_pexel.random(per_page=3)
    for photo in random_photos_page.entries:
        print(photo.id, photo.photographer, photo.url)


============
Single Photo
============
The code below will return an image object. Use the parameter ``photo_id`` to specify the ID of the image.

.. code-block:: python

    from pypexels import PyPexels
    api_key = 'YOUR_API_KEY'

    # instantiate PyPexels object
    py_pexel = PyPexels(api_key=api_key)

    # access single photo by its ID
    photo = py_pexel.single_photo(photo_id=415071)
    print(photo.id, photo.photographer, photo.url)


==============
Popular Videos
==============
The code below will iterate through all popular videos in pages of 40 items each, retrieve each video
in there, and print some of their attributes.

.. code-block:: python

    from pypexels import PyPexels
    api_key = 'YOUR_API_KEY'

    # instantiate PyPexels object
    py_pexel = PyPexels(api_key=api_key)

    popular_videos_page = py_pexel.videos_popular(per_page=40)
    while True:
        for video in popular_videos_page.entries:
            print(video.id, video.user.get('name'), video.url)
        if not popular_videos_page.has_next:
            break
        popular_videos_page = popular_videos_page.get_next_page()


=============
Search Videos
=============
The code below will perform a search of videos based on a query string, then iterate through all the results pages of 40
videos each, retrieve each video in there, and print some of their attributes.

.. code-block:: python

    from pypexels import PyPexels
    api_key = 'YOUR_API_KEY'

    # instantiate PyPexels object
    py_pexel = PyPexels(api_key=api_key)

    search_videos_page = py_pexel.videos_search(query="red+flower", per_page=40)
    while True:
        for video in search_videos_page.entries:
            print(video.id, video.user.get('name'), video.url)
        if not search_videos_page.has_next:
            break
        search_videos_page = search_videos_page.get_next_page()


============
Single Video
============
The code below will return a video object. Use the parameter ``video_id`` to specify the ID of the video.

.. code-block:: python

    from pypexels import PyPexels
    api_key = 'YOUR_API_KEY'

    # instantiate PyPexels object
    py_pexel = PyPexels(api_key=api_key)

    # access single video by its ID
    video = py_pexel.single_video(video_id=1448735)
    print(video.id, video.user.get('name'), video.url)


