Before You Begin
----------------

For release v |release|, you will need to take the steps below *before* installing the F5® LBaaSv2 plugin packages. This adds the necessary F5® service provider package to your Neutron controller.

.. topic:: Download the F5® LBaaSv2 service provider package and add it to the python path for ``neutron_lbaas``.

    1. Download from GitHub

    .. code-block:: shell

        $ curl -O https://github.com/F5Networks/neutron-lbaas/releases/download/v2.0.1a1/f5.tgz

    .. note::

        If you get a redirect error when using the above ``curl`` command, add ``-L``.

    2a. Install on CentOS:

    .. code-block:: text

        # tar xvf f5.tgz -C /usr/lib/python2.7/site-packages/neutron_lbaas/drivers/

    2b. Install on Ubuntu:

    .. code-block:: text

        # tar xvf f5.tgz –C /usr/local/lib/python2.7/dist-packages/neutron_lbaas/drivers/
