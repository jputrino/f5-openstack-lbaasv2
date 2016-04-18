Before You Begin
----------------

For release |release|, you will need to take the steps below *before* installing the F5® LBaaSv2 plugin packages. This adds the necessary F5® service provider package to your Neutron controller.

.. topic:: Download the F5® LBaaSv2 service provider package and add it to the python path for ``neutron_lbaas``.

    1. Download from GitHub

    .. code-block:: shell

        $ curl -O -L https://github.com/F5Networks/neutron-lbaas/releases/download/v8.0.1RC1/f5.tgz


    2a. Install on CentOS:

    .. code-block:: text

        # tar xvf f5.tgz -C /usr/lib/python2.7/site-packages/neutron_lbaas/drivers/

    2b. Install on Ubuntu:

    .. code-block:: text

        # tar xvf f5.tgz –C /usr/local/lib/python2.7/dist-packages/neutron_lbaas/drivers/
