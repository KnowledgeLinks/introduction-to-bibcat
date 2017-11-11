author: http://orcid.org/0000-0002-7543-3893
category: bc-link
date: 2017-11-10
next: geonames-linker
previous: bibcat-linking
title: Library of Congress Authorities Linker

The `bibcat.linker.loc` submodule is provides an API wrapper around
the Library of Congress [search service](http://id.loc.gov/search/) that
we try to link out to external Library of Congress 
authoritative name and subject IRIs for local IRIs and blank nodes.

<pre><code>>>> import bibcat.linkers.loc as loc
>>> loc
&lt;module 'bibcat.linkers.loc' from '/Users/jeremynelson/2017/bibcat/bibcat/linkers/loc.py'&gt;
</code></pre>

We will test the `loc.link_term` function that takes a term and searches all
of the Library of Congress available data sets. Much like the functions in the 
base `bibcat` module, the `loc.link_term` is a more primitive function that
is meant to used in application workflows.

Using the original Library of Congress RDF Graph, we'll create a `for` loop
and iterate through all of the `bf:Agent` entities and run the `loc.link_term`
to see what the top result is for each term.

<pre><code>
>>> for agent in pp4_loc.subjects(predicate=rdflib.RDF.type,
			      object=BF.Agent):
	label = pp4_loc.value(subject=agent,
			      predicate=rdflib.RDFS.label)
	if label is not None:
		print("Original label: {}".format(label))
		result = loc.link_term(str(label))
		for row in result:
			print("\tIRI: {}\n\ttitle {}\n".format(row.get('iri'),
							    row.get('title')))

			
Original label: DLC
	IRI: http://id.loc.gov/authorities/names/n2015048683
	title DLC eng rda DLC

Original label: ZMM
	IRI: http://id.loc.gov/authorities/names/no2004035637
	title ZMM-GT Coordinating Secretariat

Original label: C. Scribner's sons
	IRI: http://id.loc.gov/authorities/names/n81050810
	title Charles Scribner's Sons

Original label: ZMM
	IRI: http://id.loc.gov/authorities/names/no2004035637
	title ZMM-GT Coordinating Secretariat

Original label: Howells, William Dean, 1837-1920.
	IRI: http://id.loc.gov/authorities/names/n87874580
	title Howells, William Dean, 1837-1920. Novels. Selections

Original label: Austen, Jane, 1775-1817.
	IRI: http://id.loc.gov/authorities/names/n81061267
	title Austen, Jane, 1775-1817. Novels

>>> 
</code></pre>
