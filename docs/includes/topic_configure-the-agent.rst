Configure the F5® OpenStack Agent
---------------------------------

1. Edit the agent configuration file -- :file:`/etc/neutron/services/f5/f5-openstack-agent.ini` -- as appropriate for your environment.

    * To use the features available in v |release|, make sure the entries for the following options match those shown below.

    .. code-block:: text

        $ vi /etc/neutron/services/f5/f5-openstack-agent.ini
        f5_global_routed_mode = True
        f5_ha_type = standalone
        f5_device_type = external
        f5_sync_mode = replication



    * Add the IP address, username and password of your BIG-IP®. This ensures that the agent can communicate with the BIG-IP®.

    .. code-block:: text

        icontrol_hostname = <bigip_icontrol_ip_address>
        icontrol_username = <username>
        icontrol_password = <password>


2. Start the agent:

.. code-block:: text

    # service f5-openstack-agent enable            \\ Debian/Ubuntu
    # systemctl start f5-openstack-agent           \\ RedHat/CentOS


