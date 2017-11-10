title: BIBFRAME to Schema.org Linked Data
author: http://orcid.org/0000-0002-7543-3893
category: rdf-map
date: 2017-10-30
previous: bibframe-to-dpla-map4-map
next: custom-rml-rule

Most commercial search engines like Google and Microsoft Bing, 
accept another linked-data vocabulary for indexing called
[schema.org](http://schema.org/) for structuring descriptions
that are typically embedded into a web page.

For this example we will use the BIBFRAME RDF that was generated
from the MODS to BIBFRAME example and convert it to schema.org
linked data that could be embedded in an HTML page.

Creating another `SPARQLProcessor` instance, this time we will use
the `bf-to-schema.ttl` RML rules file and original BIBFRAME Lean
graph we generated with the first `rml_processor`. 

<pre><code>
>>> bf2schema_processor = processor.SPARQLProcessor(
        rml_rules=['bf-to-schema.ttl'],
        triplestore=rml_processor.output)
</code></pre>

Using the same **instance_iri** and **item_iri** as before, we will
now run the processor.

<pre><code>
>>> bf2schema_processor.run(
	instance='http://example.org/8383316#Instance')
</code></pre>

Displaying the Schema.org as Turtle

<pre><code>
@prefix rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; .
@prefix rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; .
@prefix schema: &lt;http://schema.org/&gt; 

&lt;http://example.org/8383316#Instance&gt; a schema:CreativeWork ;
    schema:contributor "Austen, Jane, 1775-1817.",
        "C. Scribner's sons",
        "Howells, William Dean, 1837-1920." ;
    schema:datePublished "1918"^^&lt;http://id.loc.gov/datatypes/edtf&gt;,
        "c1918" ;
    schema:name "Pride and prejudice /" ;
    schema:publisher "New York, Chicago [etc.] : C. Scribner's sons, [c1918]" 

</code></pre>

The final exercise in this section will be creating a new RML `TriplesMap` and
including that rule when running an existing mapping workflow.
