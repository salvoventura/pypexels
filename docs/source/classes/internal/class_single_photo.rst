######################
API: Class SinglePhoto
######################
This class is used to create an individual ``SinglePhoto`` objects from its ID.


==========
Properties
==========
Properties exposed by the ``SinglePhoto`` class.

'entries'

-----------------------------------------------------
**SinglePhoto.entries**
-----------------------------------------------------
    Iterator for the returned objects contained in this ``SinglePhoto`` instance.
    Each entry will be an instance of class ``Photo``.

    **Note** You should not use this class directly. Use PyPexels.single_photo() instead.

    ==========  ========================================
    iterator    each time an instance of class ``Photo``
    ==========  ========================================

    **Example**
    ::

        import pypexels
        py_pexel = pypexels.PyPexels(api_key='YOUR_API_KEY')

        #
        #
        photo = py_pexel.single_photo(photo_id=<ID>)
        print(photo.id, photo.photographer, photo.url)

