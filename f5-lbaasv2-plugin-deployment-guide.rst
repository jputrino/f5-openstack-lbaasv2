User Guide
==========

Release
-------

v |release|

Before You Begin
----------------
For release v |release|, you will need to install the following dependencies your Neutron controller host *before* installing the F5® LBaaSv2 plugin packages.

.. topic:: Download the F5® LBaaSv2 service provider package and add it to the python path for ``neutron_lbaas``.

    Download from GitHub

    .. code-block:: shell

        $ curl -O https://github.com/F5Networks/neutron-lbaas/releases/download/v2.0.1a1/f5.tgz

    .. note::

        If you get a redirect error when using the above ``curl`` command, add ``-L``.

    Install on CentOS:

    .. code-block:: text

        # tar xvf f5.tgz -C /usr/lib/python2.7/site-packages/neutron_lbaas/drivers/

    Install on Ubuntu:

    .. code-block:: text

        # tar xvf f5.tgz –C /usr/local/lib/python2.7/dist-packages/neutron_lbaas/drivers/


Installation
------------

.. note::

    You must have both ``pip`` and ``git`` installed on your machine in order to use these commands. It may be necessary to use ``sudo``, depending on your environment.


.. topic:: To install the lbaasv2-driver and agent packages:

    .. code-block:: text

        $ pip install git+https://github.com/F5Networks/f5-openstack-lbaasv2-driver@v2.0.1a2
        $ pip install git+https://github.com/F5Networks/f5-openstack-agent@v2.0.1a2


Configuration
-------------

Neutron
~~~~~~~

You will need to make a few configurations in your Neutron environment in order to use the F5® OpenStack LBaasv2 plugin.

1. Edit the :file:`/etc/neutron/neutron_lbaas.conf`.

In the ``[service_providers]`` section, add ``F5NetworksTest`` as the lbaasv2 service provider as shown below.

    .. code-block:: text
        :emphasize-lines: 4

        $ vi /etc/neutron/neutron_lbaas.conf
        ...
        [service_providers]
        service_provider = LOADBALANCERV2:F5NetworksTest:neutron_lbaas.drivers.f5.driver_v2.F5LBaaSV2DriverTest:default
        ...

2. Edit the ``[DEFAULT]`` section of :file:`/etc/neutron/neutron.conf` and add the ``lbaasv2`` service plugin. If there is an entry for LBaaSv1 (``lbaas``), remove it.

    .. code-block:: text

        $ vi /etc/neutron/neutron.conf
        ...
        [DEFAULT]
        service_plugins = [already defined plugins],neutron_lbaas.services.loadbalancer.plugin.LoadBalancerPluginv2
        ...

3. Restart the ``neutron-server`` service.

    .. code-block:: text

        $ service neutron-server restart // Ubuntu
        $ systemctl restart neutron-server // CentOS


F5® LBaaSv2 Plugin
~~~~~~~~~~~~~~~~~~

The configurable options supported in this release are noted below. See the agent configuration file -- :file:`/etc/neutron/services/f5/f5-openstack-agent.ini` -- for more information.

.. table::

    +---------------------------------+-----------------------------------+
    | Feature                         | Description                       |
    +=================================+===================================+
    | Global Routing Mode -           | Only global routing is supported; |
    |  ``f5_global_routed_mode``      | no L2 or L3 Segmentation.         |
    +---------------------------------+-----------------------------------+
    | Device Setting -                | External (hardware or VE) only.   |
    |  ``f5_device_type``             |                                   |
    +---------------------------------+-----------------------------------+
    | HA model -                      | Standalone only; HA is not        |
    |  ``f5_ha_type``                 | available.                        |
    +---------------------------------+-----------------------------------+
    | Sync Mode -                     | Replication only.                 |
    |  ``f5_sync_mode``               |                                   |
    +---------------------------------+-----------------------------------+


1. To use the available features, make sure the entries in the agent config file match those shown below.

.. code-block:: text

    $ vi /etc/neutron/services/f5/f5-openstack-agent.ini
    f5_global_routed_mode = True
    f5_ha_type = standalone
    f5_device_type = external
    f5_sync_mode = replication


2. Add the IP address, username and password of your BIG-IP® to the agent config file. This ensures that the agent can communicate with the BIG-IP®.

.. code-block:: text

    icontrol_hostname = <bigip_icontrol_ip_address>
    icontrol_username = <username>
    icontrol_password = <password>


3. Start the agent:

.. code-block:: text

    # systemctl enable f5-openstack-agent.service // Ubuntu
    # systemctl start f5-openstack-agent.service  // CentOS


.. tip::

    To stop the agent, run

    .. code-block:: text

        # systemctl stop f5-openstack-agent.service


.. topic:: Troubleshooting

    If the agent will not run and/or you experience errors, be sure of the following:

    - The iControl® hostname, username, and password have been entered correctly.
    - All config settings pertaining to L2 and tunneling (e.g., ``f5_vtep_folder``, ``f5_vtep_selfip_name``, tunnel types) are commented out.


Usage
-----

.. note::

    OpenStack Horizon does not currently support LBaaSv2 services. All LBaaSv2 configurations must be made via the CLI or REST API. The LBaaSv2 CLI commands all begin with ``lbaas``.

    `OpenStack CLI Documentation <http://docs.openstack.org/cli-reference/neutron.html>`_


The following restrictions apply for Neutron LBaaS objects in this release.

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

