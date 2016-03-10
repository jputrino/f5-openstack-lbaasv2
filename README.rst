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

Introduction
------------
This repo contains the code for F5's OpenStack LBaaSv2 plugin. The LBaaSv2
plugin allows you to orchestrate BIG-IP load balancing services – including
virtual IPs, pools, device service groups, and health monitoring – in an
OpenStack environment.

.. warning::

    Alpha and beta releases are **unsupported** development releases. We
    welcome feedback and bug reporting for these releases; see `Filing Issues <https://github.com/F5Networks/f5-openstack-lbaasv2/blob/experimental/README.md#filing-issues>`
    for more information.

Compatibility
-------------
This plugin can be used with OpenStack releases from Liberty forward. If
you are using an earlier release, you'll have to use the `LBaaSv1
plugin <https://github.com/F5Networks/openstack-f5-lbaasv1>`__.

Installation
------------

All of the pieces of the F5 LBaaSv2 plugin can be downloaded from PyPi. Be
sure to install each piece, as they are all required to use the plugin.

.. code-block:: text

    $ pip install f5-lbaasv2-plugin
    $ pip install f5-agent
    $ pip install f5-driver


.. add in the correct names when they are available.

Installing directly from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download the source code directly from GitHub.

.. code-block:: text

    $ curl -o https://github.com/F5Networks/f5-openstack-lbaasv2/????
    f5_os_lbaasv2_alpha1.tgz


.. add in the correct download URL and filename when they're available.


Configuration
-------------

Neutron
~~~~~~~

You will need to make a few configurations in your Neutron environment to
use the F5 OpenStack LBaasv2 plugin.

    1. Edit :file:`/etc/neutron/neutron_lbaas.conf` and add F5 as the service
    provider:

    .. code-block:: text

        $ vi /etc/neutron/neutron_lbaas.conf
        ...
        service_provider = LOADBALANCERV2:F5:neutron_lbaas.
        drivers.f5.driver.F5Driver:default
        ...


    .. add info about the service provider tarball.


    2. Edit :file:`/etc/neutron/neutron.conf` and add the ``lbaasv2``
    service plugin:

    .. code-block:: text

        $ vi /etc/neutron/neutron.conf
        ...
        service_plugins = [already defined plugins],lbaasv2
        ...


    3. Restart the ``neutron-server`` service.

    4. Make sure that the ``enable_lb`` option in :file:`local_settings.py` is
    set to ``True``.

    .. code-block:: text

        OPENSTACK_NEUTRON_NETWORK = {
        'enable_lb': True,
        ...
        }



F5 LBaaSv2 Plugin
~~~~~~~~~~~~~~~~~
You can configure a variety of options in
:file:`/etc/neutron/f5-oslbaasv1-agent.ini`. The options supported in this
release are noted below.

.. table::

    +----------------------------+-------------------------------+
    | Feature                    | Description                   |
    +============================+===============================+
    | global traffic routed mode |                               |
    +----------------------------+-------------------------------+


Once your configurations are complete, restart the agent:

.. code-block:: text

    $ service f5-oslbaasv2-agent restart


Usage
-----

OpenStack Horizon does not currently support LBaaSv2 services. All LBaaSv2
configurations must be made via the CLI or REST API.

`OpenStack CLI Documentation <http://docs.openstack.org/cli-reference/neutron.html>`_

.. note::

    The LBaaSv2 commands all begin with ``lbaas``.


Documentation
-------------

See `Documentation <http://f5-openstack-lbaasv2.rtfd.org/en/>`_.


Filing Issues
-------------
If you find an issue we would love to hear about it. Please go to the
:guilabel:`Issues` tab for this repo and open a new issue for each bug you'd
like to report. We also welcome you to submit feature requests as issues.
For both, please be sure to complete all of the fields in the issue template.


Contributing
------------
See `Contributing <CONTRIBUTING.md>`_.

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
include a set of functional tests written to use a real BIG-IP device
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

    flake8 ./


Contact
-------
f5_openstack_lbaasv2@f5.com

Copyright
---------
Copyright 2015-2016 F5 Networks Inc.

Support
-------
See `Support <SUPPORT.md>`_.

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
have completed and submitted the `F5 Contributor License
Agreement <http://f5-openstack-docs.rtfd.org/en/latest/cla_landing.html>`_
to Openstack_CLA@f5.com prior to their code submission being included
in this project.
