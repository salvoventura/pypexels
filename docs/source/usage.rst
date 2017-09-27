#####
Usage
#####

Creating an instance
====================
::

    import pypexels
    pp = pypexels.PyPexels(api_key='YOUR_API_KEY')

API keys can be obtained from `Pexels API page <https://www.pexels.com/api/>`_.

--------------------------------------------------------------------------------

Library logging
===============
The PyPexels library internal logging subsystem is driven by the application.
The default logging level of the library is set to be **logging.ERROR**.
If you want to access the library logging subsystem, you can fine-tune the logger
with id **PyPexels.logger_name** as per the following example:

.. code-block:: python

    from pypexels import PyPexels

    # Initialize app logging
    logger = logging.getLogger()
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    # pypexels logger defaults to level logging.ERROR
    # If you need to change that, use getLogger/setLevel
    # on the module logger, like this:
    logging.getLogger(PyPexels.logger_name).setLevel(logging.DEBUG)

    py_pexels = PyPexels(api_key='YOUR_API_KEY')
    # ... continue

