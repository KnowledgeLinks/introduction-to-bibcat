title: BIBFRAME 2.0 to DP.LA MAPv4
author: http://orcid.org/0000-0002-7543-3893
category: rdf-map
date: 2017-10-30
previous: dublin-core-to-bibframe-map
next: bibframe-to-schema-org-map

For the [Plains2Peaks.org](https://plains2peaks.org/) [DP.LA][DPLA] regional service
hub for Colorado and Wyoming, a RML rules map `bf-to-map4.ttl` takes BIBFRAME 2.0
RDF and processes to a new JSON-LD for ingestion into [DP.LA][DPLA] using a 
[ResourceSync][RESYNC] feed and dump.

First, we will create an another instance of `SPARQLProcessor` and use a
different RML map `bf-to-map4.ttl`. For the source RDF triples, we will use
the previous topic's BIBFRAME RDF,

<pre><code>
>>> bf2map_processor = processor.SPARQLProcessor(
	rml_rules=['bf-to-map4.ttl'],
	triplestore=dc_processor.output)
</code></pre>

Now, we will use the **item_iri** and **instance_iri** to run the
mapping from BIBFRAME to MAPv4

<pre><code>
>>> bf2map_processor.run(
        instance_iri='https://www.denverlibrary.org/57154f74-c5cb-11e7-9f30-ac87a3129ce6',
        item_iri='http://cdm16079.contentdm.oclc.org:80/cdm/ref/collection/p15330coll22/id/68544')
</code></pre>

To see the resulting MAPv4 RDF Graph, we will serialize as turtle:
 <pre><code> >>> print(bf2map_processor.output.serialize(format='turtle').decode())
</code></pre>

<pre><code>
@prefix bf: &lt;http://id.loc.gov/ontologies/bibframe/&gt; .
@prefix dc: &lt;http://purl.org/dc/elements/1.1/&gt; .
@prefix dpla: &lt;http://dp.la/about/map/&gt; .
@prefix edm: &lt;http://www.europeana.eu/schemas/edm/&gt; .
@prefix kds: &lt;http://knowledgelinks.io/ns/data-structures/&gt; .
@prefix locn: &lt;http://www.w3.org/ns/locn#&gt; .
@prefix ore: &lt;http://www.openarchives.org/ore/terms/&gt; .
@prefix oslo: &lt;http://purl.org/oslo/ns/localgov#&gt; .
@prefix ql: &lt;http://semweb.mmlab.be/ns/ql#&gt; .
@prefix rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; .
@prefix rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; .
@prefix vcard: &lt;http://www.w3.org/2006/vcard/ns#&gt; .
@prefix xml: &lt;http://www.w3.org/XML/1998/namespace&gt; .
@prefix xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt; .

&lt;https://www.denverlibrary.org/57154f74-c5cb-11e7-9f30-ac87a3129ce6#Work&gt; a ore:Aggregation ;
    edm:aggregatedCHO &lt;https://www.denverlibrary.org/57154f74-c5cb-11e7-9f30-ac87a3129ce6&gt; ;
    edm:dataProvider &lt;https://www.denverlibrary.org/&gt; ;
    edm:isShownAt &lt;http://cdm16079.contentdm.oclc.org:80/cdm/ref/collection/p15330coll22/id/68544&gt; .

&lt;http://cdm16079.contentdm.oclc.org:80/cdm/ref/collection/p15330coll22/id/68544&gt; a edm:WebResource .

&lt;https://www.denverlibrary.org/57154f74-c5cb-11e7-9f30-ac87a3129ce6&gt; a dpla:SourceResource ;
    dc:date "12/23/2010" ;
    dcterms:creator "N31e3e5a7f2cd40ed96fce3bfd50aa901" ;
    dcterms:description "Major John M. Burke, head and shoulders studio portrait, wearing hat, suit jacket and vest; Wild West promoter and Indian Agent."^^xsd:string ;
    dcterms:extent "1 copy photonegative ; 15 x 11 cm. (5 3/4 x 4 1/4 in.); 1 photonegative : glass ; 26 x 21 cm. (10 x 8 in.); 1 photoprint ; 24 x 18 cm. (9 1/4 x 7 in.)"^^xsd:string ;
    dcterms:identifier "34837596"^^xsd:string,
        "B-529"^^xsd:string ;
    dcterms:title "Major John Burke, bust"^^xsd:string .


</code></pre>

Switching to a different output vocabulary is the focus on the next exercise.

[DPLA]: https://dp.la
[RESYNC]: http://resource.io
