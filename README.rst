
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
This repo contains the documentation for F5®'s OpenStack LBaaSv2 plugin. The LBaaSv2 plugin allows you to orchestrate BIG-IP® load balancing services – including virtual IPs, pools, device service groups, and health monitoring – in an OpenStack environment.

Subprojects
-----------
The LBaaSv2 plugin comprises packages from different F5 Networks® projects:

 - `F5Networks/f5-openstack-lbaasv2-driver <https://github.com/F5Networks/f5-openstack-lbaasv2-driver>`_
 - `F5Networks/f5-openstack-agent <https://github.com/F5Networks/f5-openstack-agent>`_

Releases
--------
The latest release is v |release|. See the :ref:`Release Notes <release-notes>` for more information.

.. warning::

    Alpha and beta releases are **unsupported** development releases. We welcome feedback and bug reporting for these releases; see `For Developers <https://github.com/F5Networks/f5-openstack-lbaasv2#for-developers>`_ for more information.

Documentation
-------------
See the :doc:`Deployment Guide <deployment-guide>` for installation and configuration instructions.

Compatibility
-------------
This plugin is compatible with OpenStack |openstack|. If you are using Kilo or earlier, you'll have to use the `LBaaSv1 plugin <https://github.com/F5Networks/openstack-f5-lbaasv1>`_. See the `F5® OpenStack Releases and Support Matrix <f5-openstack-docs.rtfd.org/en/latest/releases-and-versioning.html>`_ for more information.

.. _for-developers:

For Developers:
---------------

Please note that no active development takes place in this repo. All issues and feature requests for the F5® OpenStack agent and lbaasv2 driver should be filed in the appropriate project repository:

- f5-openstack-agent_
- f5-openstack-lbaasv2-driver_


Filing Issues
-------------
If you find an issue with our documentation, we would love to hear about it. Please go to the Issues tab for this repo and open a new issue for each bug you'd like to report. We also welcome you to submit requests for new documentation as issues. For both, please be sure to complete all of the fields in the issue template.

Contributing
------------
See `Contributing <https://github.com/F5Networks/f5-openstack-lbaasv2/blob/master/CONTRIBUTING.md>`_.

.. note::

    When you open a pull request, please be sure to complete all of the
    fields in the pull request template.


Copyright
---------
Copyright 2015-2016 F5 Networks, Inc.

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

.. _f5-openstack-agent: https://github.com/F5Networks/f5-openstack-agent
.. _f5-openstack-lbaasv2-driver: https://github.com/F5Networks/f5-openstack-lbaasv2-driver
