
.. raw:: html

   <!--
   Copyright 2015 F5 Networks Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   -->

.. _readme:

f5-openstack-lbaasv2
====================

|Docs Build Status| |slack badge|

Introduction
------------
This repo contains the code for F5®'s OpenStack LBaaSv2 plugin. The LBaaSv2
plugin allows you to orchestrate BIG-IP® load balancing services – including
virtual IPs, pools, device service groups, and health monitoring – in an
OpenStack environment.

Releases
--------
The latest release is v |release|. See the :ref:`Release Notes <release-notes>` for more information.

.. warning::

    Alpha and beta releases are **unsupported** development releases. We welcome feedback and bug reporting for these releases; see `Filing Issues <https://github.com/F5Networks/f5-openstack-lbaasv2#filing-issues>`_ for more information.


Documentation
-------------
See the `Documentation <http://f5-openstack-lbaasv2.rtfd.org/en/>`_ for installation and configuration instructions.

Compatibility
-------------
This plugin can be used with OpenStack releases from Liberty forward. If you are using an earlier release, you'll have to use the `LBaaSv1 plugin <https://github.com/F5Networks/openstack-f5-lbaasv1>`_.

Subprojects
-----------
The LBaaSv2 plugin comprises packages from different F5 Networks® projects:

 - `F5Networks/f5-openstack-lbaasv2-driver <https://github.com/F5Networks/f5-openstack-lbaasv2-driver>`_
 - `F5Networks/f5-openstack-agent <https://github.com/F5Networks/f5-openstack-agent>`_

Before You Begin
----------------
For release |release|, you will need to install the following dependencies your Neutron controller host *before* installing the F5® LBaaSv2 plugin packages.

.. topic:: Download the F5® LBaaSv2 service provider package and add it to the python path for ``neutron_lbaas``.

    Download from GitHub

    .. code-block:: shell

        $ curl -O https://github
        .com/F5Networks/neutron-lbaas/releases/download/v2.0.1a2/f5.tgz

    .. note::

        If you get a redirect error when using the above ``curl`` command,
        add ``-L``.

    Install on CentOS:

    .. code-block:: text

        # tar xvf f5.tgz -C /usr/lib/python2.7/site-packages/neutron_lbaas/drivers/

    Install on Ubuntu:

    .. code-block:: text

        # tar xvf f5.tgz –C /usr/local/lib/python2.7/dist-packages/neutron_lbaas/drivers/


Installation
------------

You can download the driver and agent release packages directly from F5 Networks' GitHub repos using pip.

.. note::

    You must have both ``pip`` and ``git`` installed on your machine in order to use these commands. It may be necessary to use ``sudo``, depending on your environment.


.. code-block:: text

    $ pip install git+https://github.com/F5Networks/f5-openstack-lbaasv2-driver@v2.0.1a2
    $ pip install git+https://github.com/F5Networks/f5-openstack-agent@v2.0.1a2


Configuration
-------------

Neutron
~~~~~~~

You will need to make a few configurations in your Neutron environment in order to use the F5® OpenStack LBaasv2 plugin.

1. Edit the ``[service_providers]`` section of :file:`/etc/neutron/neutron_lbaas.conf` and add ``F5`` as the service provider. Comment out, or remove the default tag from, any other ``LOADBALANCERV2`` entries.

    .. code-block:: text

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

    # systemctl enable f5-openstack-agent.service
    # systemctl start f5-openstack-agent.service



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

    OpenStack Horizon does not currently support LBaaSv2 services. All LBaaSv2
    configurations must be made via the CLI or REST API. The LBaaSv2 CLI commands all begin with ``lbaas``.

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



.. _filing-issues:
Filing Issues
-------------
If you find an issue we would love to hear about it. Please go to the
Issues tab for this repo and open a new issue for each bug you'd
like to report. We also welcome you to submit feature requests as issues.
For both, please be sure to complete all of the fields in the issue template.

Contributing
------------
See `Contributing <https://github.com/F5Networks/f5-openstack-lbaasv2/blob/experimental/CONTRIBUTING.md>`_.

.. note::

    When you open a pull request, please be sure to complete all of the
    fields in the pull request template.


Build
-----
To make a PyPI package:

.. code-block:: text

    $ python setup.py sdist


Test
----
Before you open a pull request, your code must have passing
`pytest <http://pytest.org>`__ unit tests. In addition, you should
include a set of functional tests written to use a real BIG-IP® device
for testing. Information on how to run our set of tests is included
below.

Unit Tests
~~~~~~~~~~

We use pytest for our unit tests.

1. If you haven't already, install the required test packages and the requirements.txt in your virtual
environment.

.. code-block:: text

    $ pip install hacking pytest pytest-cov
    $ pip install -r requirements.txt

2. Run the tests and produce a coverage report. The ``--cov-report=html``
   will create a ``htmlcov/`` directory that you can view in your
   browser to see the missing lines of code.

.. code-block:: text

    $ py.test --cov ./icontrol --cov-report=html
    $ open htmlcov/index.html


Style Checks
~~~~~~~~~~~~

We use the hacking module for our style checks (installed as part of
step 1 in the Unit Test section).

.. code-block:: text

    $ flake8 ./


Copyright
---------
Copyright 2015-2016 F5 Networks Inc.

Support
-------
See `Support <https://github.com/F5Networks/f5-openstack-lbaasv2/blob/experimental/SUPPORT.md>`_.


License
-------

Apache V2.0
~~~~~~~~~~~
Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Contributor License Agreement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Individuals or business entities who contribute to this project must
have completed and submitted the `F5® Contributor License
Agreement <http://f5-openstack-docs.rtfd.org/en/latest/cla_landing.html>`_
to Openstack_CLA@f5.com prior to their code submission being included
in this project.


.. |Docs Build Status| image:: https://readthedocs.org/projects/f5-openstack-lbaasv2/badge/?version=latest
    :target: http://f5-openstack-lbaasv2.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. |slack badge| image:: https://f5-openstack-slack.herokuapp.com/badge.svg
    :target: https://f5-openstack-slack.herokuapp.com/
    :alt: Slack
