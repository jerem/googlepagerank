=================
tl.googlepagerank
=================

The googlepagerank project accesses Google's page rank data the same way the
Google toolbar does. It contains a Python package, tl.googlepagerank, and a
command line tool, googlepagerank, exercising the package's functionality.


Documentation
=============

To install googlepagerank:

- To use Python eggs, either run easy_install on a tl.googlepagerank egg you
  downloaded, or run

  easy_install tl.googlepagerank

- Not using eggs, unpack a tl.googepagerank binary distribution and copy the
  Python package and the script to appropriate places in your file system.

Then, run the script with any number of command line parameters. It takes each
parameter to be a URL to query Google for. Each query may take some time,
typically a couple of seconds. These are two sample runs, the dollar character
representing your system's command prompt:

$ googlepagerank http://www.google.com/ http://www.thomas-lotze.de/
10 http://www.google.com/
 4 http://www.thomas-lotze.de/

$ googlepagerank http://www.example.com/foobar http://foobar
   http://www.example.com/foobar
RE http://foobar

Google page ranks range from 1 (unimportant) to 10 (important).
An empty page rank means Google has not yet assigned a rank to the URL.
"IO" instead of a page rank means there was an error contacting Google.
"RE" means Google's response could not be understood.


Change log
==========

For a continuously updated change log, see
<https://svn.thomas-lotze.de/repos/public/googlepagerank/trunk/CHANGES.txt>.


Contact
=======

This package is written by Thomas Lotze. Please contact the author at
<thomas@thomas-lotze.de> to provide feedback, suggestions, or contributions.

See also <http://www.thomas-lotze.de/en/software/>.


.. Local Variables:
.. mode: rst
.. End:
