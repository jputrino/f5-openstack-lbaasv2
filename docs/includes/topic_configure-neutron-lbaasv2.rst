Configure Neutron for LBaaSv2
-----------------------------

You will need to make a few configurations in your Neutron environment in order to use the F5® OpenStack LBaasv2 plugin.

1. Edit the Neutron LBaaS config file -- :file:`/etc/neutron/neutron_lbaas.conf`.

    In the ``[service_providers]`` section, add ``F5Networks`` as the lbaasv2 service provider as shown below.

    .. code-block:: text
        :emphasize-lines: 4

        $ vi /etc/neutron/neutron_lbaas.conf
        ...
        [service_providers]
        service_provider = LOADBALANCERV2:F5Networks:neutron_lbaas.drivers.f5.driver_v2.F5LBaaSV2Driver:default
        ...

    .. note::

        If there is an active entry for the F5® LBaaSv1 service provider driver, comment (#) it out.


2. Edit the ``[DEFAULT]`` section of the Neutron config file -- :file:`/etc/neutron/neutron.conf`.

    * Add the lbaasv2 service plugin as shown below.

    .. code-block:: text

        $ vi /etc/neutron/neutron.conf
        ...
        [DEFAULT]
        service_plugins = [already defined plugins],neutron_lbaas.services.loadbalancer.plugin.LoadBalancerPluginv2
        ...

    * Remove the entry for the LBaaSv1 service plugin (``lbaas``).

3. Restart the ``neutron-server`` service.

    .. code-block:: text

        $ service neutron-server restart    \\ Ubuntu
        $ systemctl restart neutron-server  \\ CentOS
