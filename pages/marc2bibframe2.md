author: http://orcid.org/0000-0002-7543-3893
category: bc-qs
date: 2017-11-30
next: rdf-mapping
previous: importing-bibcat
title: Using marc2bibframe2 XSLT

Last year the [Library of Congress](http://loc.gov) released an official 
MARCXML-to-BIBFRAME 2.0 RDF XML project on Github at [https://github.com/](https://github.com/)
We'll now go through the steps of converting MARC 21 to MARC XML, and then create an 
XSLT transform script to convert the MARC record to BIBFRAME 2.0 RDF XML.

### Clone or Download marc2bibframe2
Open up a new command-line to set-up `marc2bibframe2` environment.
If you have [git](https://git-scm.com/) installed, you can clone the Library of 
Congress [marc2bibframe2][MRC2BF] project directly from Github.

<pre><code>(bibcat-env) $ git clone https://github.com/lcnetdev/marc2bibframe2.git</code></pre>

If you don't have [git](https://git-scm.com/) on your system, you can still download a zip file of the 
latest release from [https://github.com/lcnetdev/marc2bibframe2/releases/latest][MRC2BF_LATEST],
unzip the file, and then for convenience later on, rename the directory to `marc2bibframe2`..

<pre><code>(bibcat-env)$ wget https://github.com/lcnetdev/marc2bibframe2/archive/v1.3.1.zip
(bibcat-env)$ unzip v1.3.1.zip
(bibcat-env)$ mv marc2bibframe2-1.3.1/ marc2bibframe2</code></pre>

## Opening MARC 21 file with pymarc
If you have a MARC21 file already, use that file. Otherwise, you can 
download a sample [MARC21 file](/static/data/pride-and-prejudice.mrc) made up of a collection of Jane Austen
MARC21 records from Colorado College.

**First**, go back to your Python IDLE program and import [`pymarc`][PYMRC]
and create a MARC Reader class using your MARC 21 file. 

<pre><code>>>> import pymarc
>>> marc_reader = pymarc.MARCReader(open("/path/to/pride-and-prejudice.mrc", "rb"), 
                                to_unicode=True)
</code></pre>

Now we will read all of the MARC 21 records into a Python list and see 
how many MARC records are in the list.

<pre><code>>>>> marc_records = []
>>> for row in marc_reader:
	marc_records.append(row)
	
>>> len(marc_records)
30</code></pre> 

With the [`pymarc.Record`][PYMRC], we can print out any of these 30 MARC records

<pre><code>>>> print(marc_records[4])
=LDR  00961nam  2200289Ia 4500
=001  8383316
=003  OCoLC
=005  19981012112243.0
=008  820430s1918\\\\nyu\\\\\\\\\\\000\1\eng\\
=010  \\$a18007296
=040  \\$aDLC$cZMM$dZMM
=049  \\$aCOCA
=090  \\$aPR4034$b.P7 1918
=090  \\$aPR4034$b.P7 1918
=100  1\$aAusten, Jane,$d1775-1817.
=245  10$aPride and prejudice /$cby Jane Austen; with an introduction by William Dean Howells.
=260  \\$aNew York, Chicago [etc.] :$bC. Scribner's sons,$c[c1918]
=300  \\$axxiii, 401 p. ;$c18 cm.
=490  1\$aThe modern student's library.
=500  \\$aSeries title also at head of t.-p.
=700  1\$aHowells, William Dean,$d1837-1920.
=830  \0$aModern student's library.
=907  \\$a.b13290083
=902  \\$a130106
=999  \\$b1$c981012$dm$ea$f-$g0
=994  \\$atbp
=945  \\$aPR4034$b.P7 1918$g1$i33027003636366$j0$ltbp  $h0$oh$p$0.00$q $r-$s-$t1$u5$v0$w0$x0$y.i13884177$z981012
</code></pre> 

## Creating an XSLT Transformation to BIBFRAME RDF 
Using the `lxml.etree` module, we will create an XLST instance

<pre><code>>>> import lxml.etree
>>>> marc2bibframe2 = lxml.etree.XSLT(
	lxml.etree.parse("/path/to/marc2bibframe2/xsl/marc2bibframe2.xsl"))
</code></pre>

Using `pymarc`, we will convert a MARC record to an XML string and then 
parse it with `lxml.etree.XML` function call.

<pre><code>>>> raw_xml = pymarc.record_to_xml(marc_records[4], namespace=True)
>>> marc_xml = lxml.etree.XML(raw_xml)
>>> marc_xml
&lt;Element {http://www.loc.gov/MARC21/slim}record at 0x105d5ee08&gt;
</code></pre>
 
Then running the transform, convert the `marc_xml` to BIBFRAME RDF XML

<pre><code>>>> bf_rdf_xml = marc2bibframe2(marc_xml)
>>> raw_rdf_xml = lxml.etree.tostring(bf_rdf_xml)</code></pre>

Our final step is parse the `raw_rdf_xml` to a `rdflib.Graph` and
then print the output as RDF Turtle format:

<pre><code>>>> bf_rdf = rdflib.Graph()
>>> bf_rdf.parse(data=raw_rdf_xml, format='xml')
<Graph identifier=N8100f11eb0fd48d0a805d91f03d6af94 (<class 'rdflib.graph.Graph'>)>
>>> print(bf_rdf.serialize(format='turtle').decode())
@prefix bf: &lt;http://id.loc.gov/ontologies/bibframe/&gt; .
@prefix bflc: &lt;http://id.loc.gov/ontologies/bflc/&gt; .
@prefix madsrdf: &lt;http://www.loc.gov/mads/rdf/v1#&gt; .
@prefix rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; .
@prefix rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; .
@prefix xml: &lt;http://www.w3.org/XML/1998/namespace&gt; .
@prefix xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt; .

&lt;http://example.org/8383316#Agent100-11&gt; a bf:Agent,
        bf:Person ;
    rdfs:label "Austen, Jane, 1775-1817." ;
    bflc:name00MarcKey "1001 $aAusten, Jane,$d1775-1817." ;
    bflc:name00MatchKey "Austen, Jane, 1775-1817." ;
    bflc:primaryContributorName00MatchKey "Austen, Jane, 1775-1817." .

&lt;http://example.org/8383316#Agent700-17&gt; a bf:Agent,
        bf:Person ;
    rdfs:label "Howells, William Dean, 1837-1920." ;
    bflc:name00MarcKey "7001 $aHowells, William Dean,$d1837-1920." ;
    bflc:name00MatchKey "Howells, William Dean, 1837-1920." .

&lt;http://example.org/8383316#Instance&gt; a bf:Instance ;
    rdfs:label "Pride and prejudice /" ;
    bf:dimensions "18 cm." ;
    bf:extent [ a bf:Extent ;
            rdfs:label "xxiii, 401 p." ] ;
    bf:hasSeries [ a bf:Instance ;
            rdfs:label "The modern student's library." ;
            bf:instanceOf &lt;http://example.org/8383316#Work830-18&gt; ;
            bf:seriesStatement "The modern student's library." ] ;
    bf:identifiedBy [ a bf:Lccn ;
            rdf:value "18007296" ] ;
    bf:instanceOf &lt;http://example.org/8383316#Work&gt; ;
    bf:issuance &lt;http://id.loc.gov/vocabulary/issuance/mono&gt; ;
    bf:note [ a bf:Note ;
            rdfs:label "Series title also at head of t.-p." ] ;
    bf:provisionActivity [ a bf:ProvisionActivity,
                bf:Publication ;
            bf:agent [ a bf:Agent ;
                    rdfs:label "C. Scribner's sons" ] ;
            bf:date "c1918" ;
            bf:place [ a bf:Place ;
                    rdfs:label "New York, Chicago [etc." ] ],
        [ a bf:ProvisionActivity,
                bf:Publication ;
            bf:date "1918"^^&lt;http://id.loc.gov/datatypes/edtf&gt; ;
            bf:place &lt;http://id.loc.gov/vocabulary/countries/nyu&gt; ] ;
    bf:provisionActivityStatement "New York, Chicago [etc.] : C. Scribner's sons, [c1918]" ;
    bf:responsibilityStatement "by Jane Austen; with an introduction by William Dean Howells" ;
    bf:title [ a bf:Title ;
            rdfs:label "Pride and prejudice /" ;
            bflc:titleSortKey "Pride and prejudice /" ;
            bf:mainTitle "Pride and prejudice" ] .

&lt;http://example.org/8383316#Work&gt; a bf:Text,
        bf:Work ;
    rdfs:label "Pride and prejudice /" ;
    bf:adminMetadata [ a bf:AdminMetadata ;
            bflc:encodingLevel [ a bflc:EncodingLevel ;
                    bf:code "u" ] ;
            bf:changeDate "1998-10-12T11:22:43"^^xsd:dateTime ;
            bf:creationDate "1982-04-30"^^xsd:date ;
            bf:descriptionConventions [ a bf:DescriptionConventions ;
                    bf:code "aacr" ] ;
            bf:descriptionModifier [ a bf:Agent ;
                    rdfs:label "ZMM" ] ;
            bf:generationProcess [ a bf:GenerationProcess ;
                    rdfs:label "DLC marc2bibframe2 v1.4.0-SNAPSHOT: 2017-10-29T16:53:00-06:00" ] ;
            bf:identifiedBy [ a bf:Local ;
                    rdf:value "8383316" ] ;
            bf:source [ a bf:Agent,
                        bf:Source ;
                    rdfs:label "ZMM" ],
                [ a bf:Source ;
                    bf:code "OCoLC" ],
                [ a bf:Agent,
                        bf:Source ;
                    rdfs:label "DLC" ] ;
            bf:status [ a bf:Status ;
                    bf:code "n" ] ] ;
    bf:contribution [ a bf:Contribution ;
            bf:agent &lt;http://example.org/8383316#Agent700-17&gt; ;
            bf:role &lt;http://id.loc.gov/vocabulary/relators/ctb&gt; ],
        [ a bflc:PrimaryContribution,
                bf:Contribution ;
            bf:agent &lt;http://example.org/8383316#Agent100-11&gt; ;
            bf:role &lt;http://id.loc.gov/vocabulary/relators/ctb&gt; ] ;
    bf:genreForm &lt;http://id.loc.gov/vocabulary/marcgt/fic&gt; ;
    bf:hasInstance &lt;http://example.org/8383316#Instance&gt; ;
    bf:language &lt;http://id.loc.gov/vocabulary/languages/eng&gt; ;
    bf:title [ a bf:Title ;
            rdfs:label "Pride and prejudice /" ;
            bflc:titleSortKey "Pride and prejudice /" ;
            bf:mainTitle "Pride and prejudice" ] .

&lt;http://example.org/8383316#Work830-18&gt; a bf:Work ;
    rdfs:label "Modern student's library." ;
    bf:title [ a bf:Title ;
            rdfs:label "Modern student's library." ;
            bflc:title30MarcKey "830 0$aModern student's library." ;
            bflc:title30MatchKey "Modern student's library." ;
            bflc:titleSortKey "Modern student's library." ;
            bf:mainTitle "Modern student's library" ] .

&lt;http://id.loc.gov/vocabulary/countries/nyu&gt; a bf:Place .

&lt;http://id.loc.gov/vocabulary/issuance/mono&gt; a bf:Issuance .

&lt;http://id.loc.gov/vocabulary/languages/eng&gt; a bf:Language .

&lt;http://id.loc.gov/vocabulary/marcgt/fic&gt; a bf:GenreForm ;
    rdfs:label "fiction" .

&lt;http://id.loc.gov/vocabulary/relators/ctb&gt; a bf:Role .</code></pre>

## Next: Uing RDF Mapping Language

In the next series of topics, we will introduce the [RDF Mapping Language](/topic/rdf-mapping) and
show how using `bibcat.rml`, we can convert a [simplified BIBFRAME 2.0](/topic/filtering-bibframe) 
graph for use in a production application. 

[MRC2BF]: https://github.com/lcnetdev/marc2bibframe2.git
[MRC2BF_LATEST]: https://github.com/lcnetdev/marc2bibframe2/releases/latest
[PYMRC]: https://github.com/edsu/pymarc



