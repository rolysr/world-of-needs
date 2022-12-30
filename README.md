# world-of-needs
# Integrantes
 - David Manuel García Aguilera (@dmga44)
 - Rolando Sánchez Ramos (@rolysr)
 - Andry Rosquet Rodríguez (@aXoXoR2)
# Repositorio
 - https://github.com/rolysr/world-of-needs
# Descripción
World of Needs(WON):

En las sociedades humanas actuales se manifiestan diariamente procesos de movimientos de personas con diversos objetivos. Un ejemplo bastante importante es el que realizan algunos actores sociales con el fin de buscar víveres y realizar trámites de manera general para satisfacer una serie de necesidades personales o de su hogar.

Las instituciones encargadas de velar por la satisfacción de los pedidos básicos de los habitantes de una zona determinada, invierten en recursos y medios correspondientes a estos pedidos, además de planificar la forma de acceso a los mismos por parte de los pobladores.

El objetivo de este proyecto es permitir simular un sistema que defina el comportamiento de una sociedad o conjunto de personas distribuidas a lo largo de una zona acotada, donde existen una serie de centros especiales a los que estos humanos deben trasladarse para satisfacer sus necesidades.

## Componentes del sistema:
Para ejecutar una simulación es necesario definir inicialmente las características del ambiente donde se colocarán los agentes (los cuales harán el papel de las personas), las características de estos, así como aquellas referentes a las localizaciones de los lugares a los que deben dirigirse para cumplir sus demandas. Por lo tanto, se tienen como componentes principales del sistema:

•	Ambiente: Representa el medio sobre el cual se llevarán a cabo los sucesos de la simulación. El mismo deberá tener una forma de almacenar o representar el estado geográfico de los componentes que este contiene y de los hechos que en él ocurren. Una forma de representación de este pudiese ser a partir de una matriz bidimensional con celdas que representen una unidad de espacio que puede ser válida o no para la presencia y recorrido de los agentes o la creación de centros posibles de destino para estos.

El ambiente debe tener funcionalidades como:

  o	Añadir agentes y centros en posiciones válidas y almacenar datos referentes a estos de alguna forma.
  
  o	Ofrecer datos suficientes del estado geográfico para ser utilizados por un framework dedicado a la visualización de mapas o zonas.
  
  o	Calcular y llevar internamente estadísticas que permitan describir el estado de los componentes y hechos en el sistema como por ejemplo el tiempo transcurrido.

•	Lugares de destino: Estos componentes pueden representar desde una tienda de productos hasta un centro para que los agentes realicen algún trámite. Los mismo deben estar ubicados en zonas específicas del mapa y ofrecer una descripción de las necesidades que pueden ser satisfechas ahí. 

Para cada necesidad posible en un lugar de destino habrá una forma específica de tratar a los agentes que arriban. Un ejemplo de esto puede ser un lugar de destino D1, al cual se le define una necesidad N1 con ciertas características como límite de disponibilidad, el cual atiende a los clientes en forma de colas en orden de llegada.

Las posibles funcionalidades de los lugares de destino son:

  o	Llevar un estado interno del sistema siendo simulado y que contenga estadísticas que permitan analizar el estado actual.
  
  o	Definir una política mediante la cual serán atendidos los clientes, por ejemplo, la cantidad de servidores de atención, si estos servidores son en serie o paralelo.
  
  o	Definir una forma mínima de almacenamiento del estado de los clientes inmersos en el proceso de espera.

•	Agentes: Son aquellos integrantes del sistema que tienen como objetivo simular el comportamiento humano y tomar decisiones en base a una serie de objetivos predefinidos en los mismo. Estos pueden tener una serie de límites como dinero disponible, cantidad de necesidades a cumplir. 

Las funcionalidades que pueden tener estos son:

  o	Definir límites de los mismo en cuanto a diversos parámetros como capacidad monetaria y necesidades.
  
  o	Definir política o forma de comportamiento, lo cual influye en el proceso de toma de decisiones como decidir a dónde moverse etc.

  o	Tener formas de mostrar el estado de su satisfacción en base a los objetivos cumplido y que se pueda conocer los que le faltan por  cumplir

## Proceso de ejecución del sistema:
Una vez inicializado un ambiente con dimensiones, zonas correctamente especificadas, posicionamiento de agentes y lugares de destino se procede a iniciar la simulación. En este caso, todo el proceso se realiza a lo largo de un tiempo especificado a partir de cual el ambiente estará funcionando y se estarán actualizando los estados de sus componentes, por lo que existirá una forma de cada cierto tiempo poder consultar el estado del medio en ejecución.

Inicialmente cada agente parte de un punto donde fue colocado al configurar el ambiente, el cual puede ser entendido como su hogar. Para cada agente existen una serie de necesidades y lugares donde pueden ir a satisfacerlas, por lo que estos se empezarán a mover de manera tal que sea lo más factible posible de acuerdo a su política para sus intereses y el tiempo disponible, el cual incluye desde el tiempo de la simulación, hasta el tiempo que conlleva ser atendido en un centro determinado dado su estado (por ejemplo un agente puede no decidir hacer la cola si el tiempo que le toma hacerla afecta negativamente cumplir con la mayoría de sus necesidades o si está muy llena o si hay necesidades que son más importantes). Hay que tener en cuenta también factores como el horario de atención de los destinos y la capacidad de disponibilidad de los mismo en cuanto a cantidad de recursos.

Una vez finalizado el tiempo de ejecución del sistema, los agentes detienen su proceso de seguir tratando de satisfacer sus necesidades y vuelven a sus hogares. Por ejemplo, si en algún momento dado un ciudadano cumple con todas sus necesidades, el sistema actualiza sus estadísticas globales para tener en cuenta este suceso y se podría considerar que a partir de ese momento no es necesario tener seguimiento de este.

## Utilidad de la simulación:
Uno de los objetivos de las simulaciones es lograr llevar a cabo procesos a pequeña escala, de bajo costo, rápidos y eficientes que permitan analizar de manera objetiva una serie de sucesos que serían muy difíciles de llevar a la práctica. Por lo tanto, se espera con esta simulación dar respuestas a cuestiones como: ¿De qué forma se pudiera distribuir un presupuesto inicial para construir lugares de destinos en un ambiente dado con el fin de satisfacer la mayor cantidad de necesidades de los agentes en este? ¿Cuánto presupuesto haría falta para satisfacer la necesidad de todos? ¿Cuál es el mínimo presupuesto para satisfacer a una cantidad especificada de ciudadanos? Por lo tanto, podemos ver inicialmente la utilidad de esta propuesta.

## Uso de la Inteligencia Artificial: 
El comportamiento de los agentes, la lógica bajo la cual deciden a dónde y cómo moverse, la forma de responder las preguntas en la sección anterior son ejemplos de problemas que pueden ser resueltos a partir de algoritmos e búsqueda con heurísticas, satisfacción de restricciones e incluso algoritmos genéticos.

## Uso de la Simulación:
El comportamiento de las colas, servidores u otras formas de gestión de los centros de destino, el conjunto de agentes en general, el tiempo transcurrido etc. Pueden ser tratados con teoría de colas, generación de variables aleatorias con varias distribuciones y simulación basada en agentes.

## Requerimientos:
Revisar el archivo [requirements.txt](https://github.com/rolysr/world-of-needs/requirements.txt) e instalar dichas dependencias con sus versiones estables para el 30 de enero de 2022.

