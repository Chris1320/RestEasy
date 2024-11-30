"""
MIT License

Copyright (c) 2024 Chris1320

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys

import gi
from gi.repository import GLib, Gtk

gi.require_version("Gtk", "4.0")


class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.resteasy.RestEasy")
        GLib.set_application_name("RestEasy")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Hello, RestEasy!")
        # l = Gtk.Label(label="Hello, RestEasy!")
        # window.set_child(l)
        window.present()


if __name__ == "__main__":
    app = MyApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
