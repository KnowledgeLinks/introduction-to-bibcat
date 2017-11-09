author: http://orcid.org/0000-0002-7543-3893
title: RDF Mapping Language (RML)
category: rdf-map
date: 2017-10-30
previous: marc2bibframe2
next: filtering-bibframe

[RDF Mapping Language](http://rml.io) or RML is a specification for creating rules or
mappings between different input data sources like XML, JSON, CSV, Relational 
Databases, and even other RDF triplestores through SPARQL to RDF triples. 

RML itself is constructed using RDF so knowing how to write RDF (Turtle is usually easier
to write and comprehend for RML maps) allows you to create mappings between the input
data and your target RDF. 

<p>
<img src="/static/img/RMLmappingMethod.png">
</p>
<em>Source:</em> <a href="http://rml.io/">http://rml.io/</a>

Each rule is a `TriplesMap` class that contains

*  A `logicalSource` predicate containing what type of input data source.
*  A `subjectMap` predicate that allows you to assign a subject IRI
   or blank node and to make a RDF Class assignment
*  One or more `predicateObjectMap` that allow to assign a predicate
   to the subject using a number of different methods for matching
   data from the input as a RDF object.


The `bibcat.rml.processor` submodule has a base RML Processor 
 [Processor](https://github.com/KnowledgeLinks/bibcat/blob/0e0cc35fd0d906ebaaf306e7050ea74b60ea09c6/bibcat/rml/processor.py#L36) 

<pre><code>
>>> import bibcat.rml.processor as processor
INFO:rdflib:RDFLib Version: 4.2.2
>>> processor.Processor
&lt;class 'bibcat.rml.processor.Processor'&gt;
</code></pre>

This class is extended for specific kinds of data
sub-classes like [CSVRowProcessor](https://github.com/KnowledgeLinks/bibcat/blob/0e0cc35fd0d906ebaaf306e7050ea74b60ea09c6/bibcat/rml/processor.py#L393) for common-separated values data inputs 
such as spreadsheets

<pre><code>
>>> processor.CSVRowProcessor
&lt;class 'bibcat.rml.processor.CSVRowProcessor'&gt;
</code></pre>

A [JSONProcessor](https://github.com/KnowledgeLinks/bibcat/blob/0e0cc35fd0d906ebaaf306e7050ea74b60ea09c6/bibcat/rml/processor.py#L481) for JSON data sources,

<pre><code>
>>> processor.JSONProcessor
&lt;class 'bibcat.rml.processor.JSONProcessor'&gt;
</code></pre>

A [SPARQLProcessor](https://github.com/KnowledgeLinks/bibcat/blob/0e0cc35fd0d906ebaaf306e7050ea74b60ea09c6/bibcat/rml/processor.py#L772) for mapping RDF triples to RDF triples, 

<pre><code>
>>> processor.SPARQLProcessor
&lt;class 'bibcat.rml.processor.SPARQLProcessor'&gt;
</code></pre>

And a 
[XMLProcessor](https://github.com/KnowledgeLinks/bibcat/blob/0e0cc35fd0d906ebaaf306e7050ea74b60ea09c6/bibcat/rml/processor.py#L591).

<pre><code>
>>> processor.XMLProcessor
&lt;class 'bibcat.rml.processor.XMLProcessor'&gt;
</code></pre>

In the first example will take the BIBFRAME RDF produced by the `marc2bibframe2`,
create an instance of the `SPARQLProcessor` class to demonstrate the use of
the RML Processor.

