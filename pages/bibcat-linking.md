title: BIBCAT Linking
author: http://orcid.org/0000-0002-7543-3893
category: bc-link
date: 2017-10-30
previous: custom-rml-rule
next: loc-authorities-linker

The promise of [Library Linked Data][LLD] is the ability for libraries to
link-out to other authoritative sources instead of managing all this data
locally as with most legacy integrated library systems and even the more
modern library system platforms.

BIBCAT offers a number of `bibcat.linker` classes for establishing these
links from locally produced BIBFRAME RDF. Typically these linker classes
will attempt to retrieve the best IRI and replace locally generated IRIs
and Blank Nodes with the IRI of the source.

[LLD]: https://www.ld4l.org/

