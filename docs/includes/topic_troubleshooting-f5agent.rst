Troubleshooting the F5® OpenStack Agent
---------------------------------------

The ``f5-openstack-agent`` is not running
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the ``f5-openstack-agent`` doesn't appear in the Horizon agent list or when you run ``neutron agent-list``, the agent is not running.

Here are a few things you can try:

1. Check the logs:

    .. code-block:: text

        # less /var/log/neutron/f5-openstack-agent.log

2. Check the status of the f5-openstack-agent service:

    .. code-block:: text

        # service f5-openstack-agent status           \\ Debian/Ubuntu
        # systemctl status f5-openstack-agent.service \\ RedHat/CentOS


3. Make sure you don't have more than one agent with the same ``environment_prefix`` running on the same host.

    .. code-block:: text

        # environment_prefix = uuid \\ This is the default setting


4. Make sure you can connect to the BIG-IP® and that the iControl® hostname, username, and password in the config file are correct.


5. If you're not using vtep, comment out (#) the lines shown below in the agent config file.

    .. code-block:: text

        #
        #f5_vtep_folder = 'Common'
        #f5_vtep_selfip_name = 'vtep'
        #
