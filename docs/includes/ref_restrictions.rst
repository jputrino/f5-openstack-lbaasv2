Restrictions
------------

The following restrictions apply for Neutron LBaaS objects in the v |release| release.

.. table::

    +----------------+---------------+----------------------------------------+
    | Object         | Supported     | Unsupported                            |
    +================+===============+========================================+
    | Listener       || ``HTTP``     || ``TERMINATED_HTTPS``                  |
    |                || ``HTTPS``    || ``sni_container_refs``                |
    |                || ``TCP``      || ``default_tls_container_ref``         |
    +----------------+---------------+----------------------------------------+
    | Load balancer  |               | Statistics commands                    |
    |                |               | (``neutron lbaas-loadbalancer-stats``) |
    +----------------+---------------+----------------------------------------+
