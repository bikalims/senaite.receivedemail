## senaite.receivedemail

### Overview

`senaite.receivedemail` extends **Senaite** (the modern core of Bika LIMS) with 

If you have product installed, an email is posted to the Client Contacts, that their Samples were received at the lab. The email text can be configured in the setup and Sample and their Batches hyperlinked

### Requirements

- **Senaite** (recommended latest version) or **Ingwe Bika LIMS 4**

### Installation

#### Using Buildout (Classic Plone/Senaite)

Add the following to your `buildout.cfg`:

cfg
[buildout]
eggs =
    ...
    senaite.receivedemail

Then run:
Bashbin/buildout

#### Docker (Recommended for Ingwe Bika LIMS 4)

Add senaite.receivedemail to your custom add-ons list in the Docker-based Ingwe Bika distribution.

### User Manual

### License
This project is licensed under the GNU General Public License v2.0 (GPL-2.0).

Support & Professional Services
[Bika Lab Systems](www.bikalabs.com) offers professional implementation, training, custom development, and support for bika.concrete.

Website: [https://www.bikalims.org](https://www.bikalims.org)
Email: info@bikalims.org (or contact Lemoene directly)

Made with ❤️ in Cape Town, South Africa
