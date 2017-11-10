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
the `bf-to-schema.ttl` RML rules file.

<pre><code>
>>> bf2schema_processor = processor.SPARQLProcessor(
        rml_rules=['bf-to-schema.ttl'],
        triplestore=)
</code></pre>

Using the same **instance_iri** and **item_iri** as before, we will
now run the processor.

<pre><code>
>>> bf2schema_processor.run(
        item_iri='http://hermes.cde.state.co.us/drupal/islandora/object/co:21951/',
        instance=instance_iri)
</code></pre>

Displaying the Schema.org as Turtle

<pre><code>
