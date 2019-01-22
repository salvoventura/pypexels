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

