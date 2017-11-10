author: http://orcid.org/0000-0002-7543-3893
category: rdf-map
date: 2017-11-09
next: mods-to-bibframe-map
previous: rdf-mapping
title: Filtering BIBFRAME 2.0

All `Processor` classes have a **source** property that stores the data.
Using the `bf_rdf` RDF graph from the `marc2bibframe2` XSLT process as a triplestore parameter,
we will create an instance of a `SPARQLProcessor` Python class and pass
in a Python list made up of a RML Turtle file, `loc-bf-to-lean-bf.ttl` that is a RML mapping rule
set included in `bibcat`. 

<pre><code>
>>> rml_processor = processor.SPARQLProcessor(
        triplestore=bf_rdf,
        rml_rules=['loc-bf-to-lean-bf.ttl'])
</code></pre>

Next we will call the `rml_processor.run` method that takes the mapping rules
and applies them to the source, in the case of the `SPARQLProcessor` class, the `bf_rdf`
graph. For other RML `Processor` subclasses, the `run` method requires keyword 
parameters depending on what is found in the RML rules. The resulting RDF
triples that are generated from the RML mapping during the `run` method
execution is stored in a instance property called `output`.

<pre><code>
>>> rml_processor.output
>>> rml_processor.run()
>>> rml_processor.output
<Graph identifier=N4c335c76cd1c4e238de89f90b5296b6a (<class 'rdflib.graph.Graph'>)>
>>> len(rml_processor.output)
45
</code></pre>

The new lean BIBFRAME graph has 45 triples verses the original source RDF graph
that had 120 triples.

Now, we see the resulting lean BIBFRAME 2.0 graph by printing the `rml_processor.output`
graph as turtle:

<pre><code>
@prefix adms: &lt;http://www.w3.org/ns/adms#&gt; .
@prefix bc: &lt;http://knowledgelinks.io/ns/bibcat/&gt; .
@prefix bf: &lt;http://id.loc.gov/ontologies/bibframe/&gt; .
@prefix dcterms: &lt;http://purl.org/dc/terms/&gt; .
@prefix kds: &lt;http://knowledgelinks.io/ns/data-structures/&gt; .
@prefix locn: &lt;http://www.w3.org/ns/locn#&gt; .
@prefix oslo: &lt;http://purl.org/oslo/ns/localgov#&gt; .
@prefix ql: &lt;http://semweb.mmlab.be/ns/ql#&gt; .
@prefix rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; .
@prefix rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; .
@prefix relators: &lt;http://id.loc.gov/vocabulary/relators/&gt; .
@prefix rml: &lt;http://semweb.mmlab.be/ns/rml#&gt; .
@prefix rr: &lt;http://www.w3.org/ns/r2rml#&gt; .
@prefix schema: &lt;http://schema.org/&gt; .
@prefix skos: &lt;http://www.w3.org/2004/02/skos/core#&gt; .
@prefix vcard: &lt;http://www.w3.org/2006/vcard/ns#&gt; .
@prefix xml: &lt;http://www.w3.org/XML/1998/namespace&gt; .
@prefix xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt; .

&lt;http://example.org/8383316#Instance&gt; a bf:Instance ;
    rdfs:label "Pride and prejudice /" ;
    bf:dimensions "18 cm." ;
    bf:instanceOf &lt;http://example.org/8383316#Work&gt; ;
    bf:issuance &lt;http://id.loc.gov/vocabulary/issuance/mono&gt; ;
    bf:note [ a bf:Note ;
            rdfs:label "Series title also at head of t.-p." ] ;
    bf:provisionActivity [ a bf:ProvisionActivity,
                bf:Publication ;
            bf:date "c1918" ;
            bf:place "New York, Chicago [etc." ],
        [ a bf:ProvisionActivity,
                bf:Publication ;
            bf:date "1918"^^&lt;http://id.loc.gov/datatypes/edtf&gt; ;
            bf:place &lt;http://id.loc.gov/vocabulary/countries/nyu&gt; ] ;
    bf:provisionActivityStatement "New York, Chicago [etc.] : C. Scribner's sons, [c1918]" ;
    bf:responsibilityStatement "by Jane Austen; with an introduction by William Dean Howells" ;
    bf:title [ a bf:Title ;
            rdfs:label "Pride and prejudice /" ;
            bf:mainTitle "Pride and prejudice" ] .

&lt;http://example.org/8383316#Work&gt; a bf:Text,
        bf:Work ;
    bf:contribution [ a bf:Contribution ;
            bf:agent _:ub1bL38C22,
                &lt;http://example.org/8383316#Agent100-11&gt;,
                &lt;http://example.org/8383316#Agent700-17&gt; ;
            bf:role relators:ctb ],
        [ a bf:Contribution ;
            bf:agent _:ub1bL38C22,
                &lt;http://example.org/8383316#Agent100-11&gt;,
                &lt;http://example.org/8383316#Agent700-17&gt; ;
            bf:role relators:ctb ] .

&lt;http://example.org/8383316#Agent100-11&gt; a bf:Agent ;
    rdfs:label "Austen, Jane, 1775-1817." .

&lt;http://example.org/8383316#Agent700-17&gt; a bf:Agent ;
    rdfs:label "Howells, William Dean, 1837-1920." .

relators:ctb a bf:Role .

_:ub1bL38C22 a bf:Agent ;
    rdfs:label "C. Scribner's sons" .
</code></pre>

This lean BIBFRAME can still reference and use the original Library of Congress
because the subject URIs are the same. The reasoning behind this mapping is to 
simplify the BIBFRAME 2.0 mappings to other vocabularies and to tune the triplestore 
for performance.
