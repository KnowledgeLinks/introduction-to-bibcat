author: http://orcid.org/0000-0002-7543-3893
category: bc-link
date: 2017-11-10
next: bibcat-future
previous: loc-authorities-linker
title: Geonames.org Linker

Like the Library of Congress Linker, the `bibcat.linker.geonames` 
submodule connects to the [Geonames](http://www.geonames.org/) API
and returns an IRI and label. Before you can use this API, you'll
need to register for an account at the 
<a href="http://www.geonames.org/login">login</a> page. 

To use `bibcat.linker.geonames` submodule, first import, then we'll
test with some common place names and see what is returned.

<pre><code>
>>> import bibcat.linkers.geonames as geonames
>>> denver_iri = geonames.link_iri("Denver", "your-user-name")
{'adminCode1': 'CO', 'lng': '-104.9847', 'geonameId': 5419384, 
'toponymName': 'Denver', 'countryId': '6252001', 'fcl': 'P', 
'population': 682545, 'countryCode': 'US', 'name': 'Denver', 
'fclName': 'city, village,...', 'countryName': 'United States', 
'fcodeName': 'seat of a first-order administrative division',
 'adminName1': 'Colorado', 'lat': '39.73915', 'fcode': 'PPLA'}
>>> denver_iri
rdflib.term.URIRef('http://www.geonames.org/5419384/')
</code></pre>

The geonames works great for unique geographical names, the difficultly with 
using this API is that it expects specific formats to distinguish between
different places with the same name and your incoming data may not be in the
expected format.

<pre><code>
>>> geonames.link_iri("Springfield", "jermnelson")
{'adminCode1': 'IL', 'lng': '-89.64371', 'geonameId': 4250542, 
'toponymName': 'Springfield', 'countryId': '6252001', 
'fcl': 'P', 'population': 116565, 'countryCode': 'US', 
'name': 'Springfield', 'fclName': 'city, village,...', 
'countryName': 'United States', 'fcodeName': 'seat of a first-order administrative division',
 'adminName1': 'Illinois', 'lat': '39.80172', 'fcode': 'PPLA'}
rdflib.term.URIRef('http://www.geonames.org/4250542/')
>>> geonames.link_iri("Springfield, MA", "jermnelson")
{'adminCode1': 'MA', 'lng': '-72.58981', 'geonameId': 4951788, 
'toponymName': 'Springfield', 'countryId': '6252001', 
'fcl': 'P', 'population': 154341, 'countryCode': 'US',
 'name': 'Springfield', 'fclName': 'city, village,...',
 'countryName': 'United States', 'fcodeName': 'populated place', 
'adminName1': 'Massachusetts', 'lat': '42.10148', 'fcode': 'PPL'}
rdflib.term.URIRef('http://www.geonames.org/4951788/')
>>></code></pre>


