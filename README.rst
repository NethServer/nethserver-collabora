====================
nethserver-collabora
====================

This package provide Nethserver integration of `Collabora Online Development Edition`_.

.. _Collabora Online Development Edition: https://www.collaboraoffice.com/code/

First configuration
===================

Collabora Online requires a dedicated virtual host and it's only accessible from HTTPS with a valid certificate.

To configure Collobora Online, execute: ::

  config setprop coolwsd VirtualHost collabora.yourdomain.com
  signal-event nethserver-collabora-update

After virtual host configuration, obtain a valid HTTPS certificate via Let's encrypt from ``Server certificate`` section of Server Manager interface.

The package does the following:

* Add server FQDN and Nextcloud custom virtual host, if present, to the trusted domains allowed to access to Collabora Online
* If nethserver-nextcloud is installed, and the prop ``VirtualHost`` is set, nethserver-collabora-event will automatically enable
  Nextcloud for use Collabora Online.

Database
========

The configuration is stored inside the ``configuration`` db, under the ``coolwsd`` key. To show it: ::

 config show coolwsd

Properties:

* ``AllowWopiHost``: additional trusted domain allowed to access to Collabora Online, only needed if nextcloud instance is on separate server.
* ``VirtualHost``: set dedicated virtual host for Collabora Online

examples: ::

  config setprop coolwsd VirtualHost coolwsd-dev.nethserver.net AllowWopiHost nextcloud-office.yourdomain.com
  config show coolwsd
  coolwsd=service
    AllowWopiHost=nextcloud-office.yourdomain.com
    VirtualHost=coolwsd-dev.nethserver.net
    status=enable


Admin user
==========

After installation, admin dashboard can be enable with ``coolconfig set-admin-password`` and accessible at: ::

  https://collabora.yourdomain.com/browser/dist/admin/admin.html


Collabora repository
====================

Update from CODE (collabora office developement edition) repository: ::

  yum update --enablerepo=collaboraoffice
