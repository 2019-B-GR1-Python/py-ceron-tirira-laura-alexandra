# Srapy
## Srapy instalacion

Ejecutar dentro del anaconda prompt

comandos generales.
```
$ pip install scrapy
```
da las caracteristicas para poder hacer web scraping o web crawling de ese computador
```
$ scrapy bench
```
Visualizar las configuraciones extras
```
$ scrapy settings
```
visualizamos la version de scrapy
```
$ scrapy version
```

### Scrapy view url
para ver si se carga el contenido en html 

no carga el contenido

```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT

```
carga todo el contenido

$ scrapy view https://www.pluralsight.com/authors


### crapy shell url

permite interactual con la repsuesta del scrapy


crapy shell http://quotes.toscrape.com/ 

se abre un archivo donde se puede programar con python 

ahi se aplica los siguientes comandos

crapy shell http://quotes.toscrape.com/ 
response.css('title').extrac()
response.css('.title::text').extract()

response.css('author').extrac()
response.css('.author::text').extract()
type(response.css('.author::text'))

response.css('.author::text').extract()[0]


response.css('span.text::text').extract()

response.css('.tag::text').extract()

