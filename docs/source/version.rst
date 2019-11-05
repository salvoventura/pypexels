Version
=======
**PyPexels v1.0.0b4 (beta, v4)**

    Fourth beta release introduces bugfix for `Issue#7 AttributeError raised on Search.entries <https://github.com/salvoventura/pypexels/issues/7>`_.
    REST API calls could fail silently making `body` an object of type `None`. With this fix,
    failing REST API calls will raise a **PexelsError** exception instead.

    Note that using this library you still need to abide to Pexels Guidelines, which
    are explained on `Pexels API page <https://www.pexels.com/api/>`_
