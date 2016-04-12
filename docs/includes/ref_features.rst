LBaaSv2 Features
----------------

The configurable options supported in release v |release| are noted below. See the agent configuration file -- :file:`/etc/neutron/services/f5/f5-openstack-agent.ini` -- for more information about each feature.

.. table:: Configurable features

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
