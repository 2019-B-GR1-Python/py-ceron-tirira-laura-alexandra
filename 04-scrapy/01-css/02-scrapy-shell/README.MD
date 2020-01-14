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


### scrapy shell url

permite interactual con la repsuesta del scrapy


scrapy shell http://quotes.toscrape.com/ 

se abre un archivo donde se puede programar con python 

ahi se aplica los siguientes comandos

scrapy shell http://quotes.toscrape.com/ 
response.css('title').extrac()
response.css('.title::text').extract()

response.css('author').extrac()
response.css('.author::text').extract()
type(response.css('.author::text'))

response.css('.author::text').extract()[0]


response.css('span.text::text').extract()

response.css('.tag::text').extract()


response.css('.row > div > div:nth-child(2) > .text::text').extract()

xpath

obtener el titulo.

response.xpath('/html/head/title').extract()

response.xpath('//title').extract()

extraer el primero de la lista 

response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()


response.xpath('/html/body/div/div[2]/div[2]/h2').extract()

response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()

response.xpath("//div[@class='quote']/span/a/@href").extract_first()


 response.xpath("//div[@class='quote']/span/a/@href/text()").extract_first()

scrapy shell http://quotes.toscrape.com/
response.xpath('/html/head/title').extract()
response.xpath('//title').extract()
response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
//div[@class='quote']/span/a/@href").extract_first()


## scrapy startproject 'nombre'

```
scrapy startproject arania_basica
```

