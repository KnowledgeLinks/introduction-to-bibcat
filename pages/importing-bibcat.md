author: http://orcid.org/0000-0002-7543-3893
category: bc-qs
date: 2017-10-30
next: marc2bibframe2
previous: install
title: Importing BIBCAT and Overview of Functions

## Importing BIBCAT
To import [BIBCAT][BC], first activate your Virtual Environment and then launch 
the Python [IDLE]() program with this command `(bibcat-env) $ python -m idlelib`.

<pre><code>
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import bibcat
INFO:rdflib:RDFLib Version: 4.2.2
>>> bibcat.__version__
'1.18.1'
</code></pre>

## Setup for Exercises
Before we explore `bibcat`, we'll create a minimal RDF environment to use 
through-out this tutorial.

1.  Import `rdflib` module 
    <pre><code>>>> import rdflib</code></pre>

1.  Create a BIBFRAME 2.0 Namespace `BF`

    <pre><code>>>> BF = rdflib.Namespace("http://id.loc.gov/ontologies/bibframe/")</code></pre>


1.  Create a test RDF graph
    <pre><code>>>> test_graph = bibcat.rdflib.Graph()</code></pre>


1.  BIND BIBFRAME namespace in graph
    <pre><code>>>> test_graph.namespace_manager.bind("bf", BF)</code></pre>

## Overview of BIBCAT Functions
The base `bibcat` module has a number of helpful RDF functions when building Semantic
Web and Linked Data applications 

### _is_valid_uri, clean_uris, create_rdf_list
The `bibcat._is_valid_uri` function is used internally by other functions in the base
bibcat module. This function uses `rdflib` internal functions for validating 
URIs. 

<pre><code>
>>> bibcat._is_valid_uri("http://bibcat.org/")
True
>>> bibcat._is_valid_uri("http://bibcat.org/ ")
False
>>>
</code></pre>

The `bibcat.clean_uris` function is used in post-processing the RDF produced by
the Library of Congress's [marc2bibframe2][MRC2BF2] XSLT 
process which sometimes includes URIs that are invalid and cause errors
when trying to process further with either `bibcat.rml.processor` 
or `bibcat.linkers` classes.

The `bibcat.create_rdf_list` function creates a RDF List that preserves the
order of the elements in RDF. Many of the complex subjects that result
from the MARC XML-to-BIBFRAME 2.0 [marc2bibframe2][MRC2BF2] XSLT 
transform. 

### delete_bnode, delete_iri, replace_iri
The `delete_bnode`, `delete_iri`, and `replace_iri` helper functions are used
by multiple `bibcat` submodules. These helper functions allow for easier manipulation
of RDF Graphs to link-out and replace local instances of a RDF entity with a linked
URI that exists locally or through an external linking entity like the Library of Congress
or Geonames. 

### slugify and wikify
The `bibcat.slugify` and `bibcat.wikify` allow you to create human-readable but valid
URIs for use in your Linked Data applications.

The `bibcat.slugify` function takes a string, lowercases all characters, replaces 
spaces with dashes, and removes any punctuation.

<pre><code>
>>> bibcat.slugify("A short message.")
'a-short-message'
>>> bibcat.slugify("A Very Long Title by Dr. First name Second name")
'a-very-long-title-by-dr-first-name-second-name'
</code></pre>
 
The `bibcat.wikify` is similar function but converts a string that follows 
[Wikipedia][https://en.wikipedia.org/wiki/Main_Page] patter of keeping capitalization
and replacing punctuation and spaces with underscores.

<pre><code>
>>> bibcat.wikify("A short message.")
'A_short_message'
>>> bibcat.wikify("A Very Long Title by Dr. First name Second name")
'A_Very_Long_Title_by_Dr_First_name_Second_name'</code></pre>

Now that we have had a quick overview of some of the base `bibcat` functions,
we'll [next](/topic/marc2bibframe2) use the Library of Congress `marc2bibframe2` to 
transform MARC XML records to BIBFRAME 2.0 RDF XML.
 
[BC]: https://github.com/KnowledgeLinks/bibcat
[MRC2BF2]: /topic/marc2bibframe2
