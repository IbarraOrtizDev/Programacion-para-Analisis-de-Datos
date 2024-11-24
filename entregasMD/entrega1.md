# Tarea S25 - Evidencia de aprendizaje 1. Análisis y herramientas de extracción de datos

## Introducción

En un mercado competitivo, una adecuada estrategia de precios es fundamental para captar y retener clientes. Este proyecto plantea el uso de técnicas de web scraping para obtener información en tiempo real sobre los precios de productos similares que ofrecen los competidores. A través de la recolección y análisis de datos de precios y características de productos en diversos sitios web, se busca optimizar la estrategia de precios de una compañía comercializadora al introducir nuevos artículos al mercado.

Con esta metodología, la empresa podrá acceder a información actualizada y eficiente sobre el comportamiento de precios, identificar tendencias, y hacer ajustes en sus propios precios para ganar competitividad. Este proceso permite, además, explorar otros factores que pueden influir en las decisiones de compra, tales como descuentos, reseñas y valoraciones de los usuarios, lo cual ofrece una visión integral del mercado.

El desarrollo de esta herramienta representa una oportunidad para implementar decisiones basadas en datos y mejorar la posición de la empresa en el sector, garantizando que los productos se mantengan atractivos y competitivos en relación con los de otras marcas.

## Descripción de la pagina y articulo a analizar

Para el desarrollo del proyecto se tomaran en cuenta tres paginas las cuales son: 
- Mercado Libre
- Alkomprar
- Alkosto

El ideal es conseguir informacion detallada de los productos, como el precio, calificación, descripción y detalles del mismo

## Descripción del tema de interés que deseas desarrollar en la primera práctica.

En esta primera actividad, el objetivo es construir una funcionalidad básica que permita consultar de manera independiente diversas plataformas de comercio electrónico. Este desarrollo representa un primer acercamiento al Producto Mínimo Viable (MVP), que facilitará la recolección de datos clave, como precios y características de productos competidores, en un formato estructurado. Utilizando herramientas de web scraping, se busca obtener esta información en un formato estándar que sirva como base para análisis posteriores, asegurando flexibilidad y escalabilidad en futuras iteraciones del proyecto.

## Objetivos: formula los objetivos a partir de la siguiente pregunta: ¿por qué deseas analizar este artículo y la empresa de comercio?

### Objetivo general:

Desarrollar una plataforma que permita a la empresa de comercio ajustar sus estrategias de precios y posicionamiento en el mercado a partir de información actualizada sobre la competencia, facilitando la toma de decisiones basadas en datos.

### Objetivo especifico

- Implementar un sistema automatizado para recolectar y analizar datos de productos y precios en tiempo real desde diferentes plataformas de comercio electrónico.
- Proveer una herramienta que permita identificar y comparar productos similares, facilitando una estrategia de precios competitiva para la empresa.
- Asegurar la flexibilidad de la plataforma para incluir nuevas fuentes de datos y adaptarse a cambios en los sitios de la competencia, manteniendo la actualización continua de la información recopilada.

## Metodología empleada de scraping.

Para la recolección de datos de precios y características de productos en diversas plataformas de comercio electrónico, se utilizará Scrapy, un framework de Python diseñado para realizar scraping de manera eficiente y escalable.

## Resultados y conclusiones.

- Selenium permite conseguir el objetivo de consulta, sin embargo es notablemente lento, en comparacion con otras tecnologias. En particular he tenido la oportunidad de consultar datos de manera masiva para desarrollos de otras empresas y lo he realizado con puppeteer y siento que el proceso se hace más rápido.
- Algunos datos podrían ser conseguidos en las consultas, por ello es necesario hacer un hacer uso de estrategias de execpciones para que el aplicativo no reviente.
- Si bien Selenium demostró ser efectivo para la recolección de datos en sitios dinámicos, sería beneficioso combinarlo con un framework como Scrapy para un enfoque híbrido en futuros proyectos. Esto permitiría aprovechar la velocidad de Scrapy en los sitios que no requieren interacción dinámica, mejorando el rendimiento general y optimizando el uso de recursos.
