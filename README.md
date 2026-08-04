# Static Pages
## Misago Plugin
A simple plugin for the forum software Misago, that allows to add "static" pages via the admin control panel. Those can be used for purely informational pages that don't make sense to create a forum thread for.

## Features
In the admin control panel the plugin adds a new side menu entry "Static Pages". Here you can add, edit and delete your pages.\
The page editor is [Quill](https://quilljs.com/) and thus allows direct formatting. Currently, adding images is not supported.\
In the acp the link to the page is shown and can be copied, for example to add a custom menu entry on your misago forum.\
Pages are always registered under …/pages/slug.\
The static pages blend in seemlessly into your misago forum and can be used for additional information, e.g. the "Impressum" page, that is mandatory for German websites.

### Localisation
- English (default)
- German (fully translated)

## Installation
For Misago Docker:
- Clone this repository into the plugins directory of your Misago installation.
- Then run \
`./appctl manage.py collectstatic`\
and \
`./appclt rebuild`
- Done.

## Bugs
If you encounter any bugs, you can open an issue here on GitHub or post it into the corresponding thread in the official Misago forum.

## Copyright and license
Misago Static Pages Plugin - Copyright © 2026 Rolf T. Meles
This program comes with ABSOLUTELY NO WARRANTY.

This is free software and you are welcome to modify and redistribute it under the conditions described in the license. For the complete license, refer to LICENSE.rst
