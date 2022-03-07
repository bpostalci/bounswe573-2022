
# Wikidata

Wikidata is an editable knowledge base which provides data to [Wikipedia](https://en.wikipedia.org/) and other projects. Anyone can use data from Wikidata as long as conforming its license. 

Now I will describe how to use Wikidata API to fetch and read data from its services. I will use [wikibase-cli](https://github.com/maxlath/wikibase-cli) CLI tool to yse Wikidata API.

## Installation

To install [wikibase-cli](https://github.com/maxlath/wikibase-cli) make sure npm (node package manager) is installed in your system

* Install via npm
	
	~~~
	$ npm install -g wikibase-cli 
	~~~
	
* Control it is installed properly
* 
	~~~
	$ wd summary Q1
	~~~
	
>after running above command you need to see some output

## API Usage Examples

* wd search

	> Search anything in Wikidata by specifying a keyword  

	Example search with "berat" keyword 
	
	~~~
	$ wd search berat
	Q170244    Berat town located in south-central Albania
	Q396112    Berat Wikimedia disambiguation page
	Q3737373   Berat male given name
	Q829346    Berat license issued by the ottoman authorities
	Q48807770  Berat locality in Southern Downs, Queensland, Australia
	Q1467107   Bérat commune in Haute-Garonne, France
	Q189296    Berat County county of Albania
	Q202981    Berat District former geographic subdivision of Albania
	Q429492    Beratzhausen municipality of Germany
	Q63087514  Bérat family name
	Q15938798  Bérat Wikimedia disambiguation page
	Q16350054  Berat Municipality municipality in Albania
	Q830206    Beratón municipality of Spain
	Q6052158   Berat Albayrak Turkish businessman
	Q15197300  Berat Djimsiti Albanian footballer
	Q771813    Berat Sadik Finnish footballer
	Q2968550   Berat Castle cultural heritage monument of Albania
	Q89072921  Berat Demir researcher
	Q12474076  Kuçovë Air Base air base in Albania
	Q4830734   Beratlı village in Artvin Province, Turkey
	~~~

* wd summary

	> In the above "wd search" command it outputs search results beginning with an id like "Q189296". You use "wd summary" command to fetch a brief summary about an ID

	Example summary of "Q189296" ID
	
	~~~
	$ wd summary Q189296
	id Q189296
	Label Berat County
	Description county of Albania
	instance of (P31): county of Albania (Q104251)
	~~~

* wd data

	> Fetch raw data (in JSON format) by specifying an ID

	Example data of "Q189296" ID (just showing a few lines of the actual output)
	
	~~~
	$ wd data Q189296
	{"pageid":187841,"ns":0,"title":"Q189296","lastrevid":1569601598,"modified":"2022-01-29T07:29:59Z","type":"item",
	"id":"Q189296","labels":{"zh-hans":{"language":"zh-hans","value":"培拉特州"},"zh-hant":
	{"language":"zh-hant","value":"培拉特州"},"zh-hk":{"language":"zh-hk","value":"培拉特州"}
	~~~

* wd open
	> Open the web page of specified ID

	Below command will open web page of the specified ID "Q189296" in your default browser

	~~~
	wd open Q189296
	~~~