Componente	Tipo de Elemento	Responsabilidad Principal	Atributos / Variables	Métodos / Funciones Clave
Vuelo	Clase (Objeto)	Representar la información individual de cada vuelo.	codigo, origen, destino, duracion, aerolinea	mostrar() (Imprime los datos del objeto).
SistemaVuelos	Clase (Controlador)	Gestionar la colección completa de vuelos y la lógica de negocio.	vuelos (Lista de objetos Vuelo).	cargar_archivo(), detalle_vuelo(), agrupar_por_aerolinea(), ordenar_por_duracion().
menu	Función (Interfaz)	Interactuar con el usuario y dirigir el flujo del programa.	sistema (Instancia de SistemaVuelos), opcion.	input(), print() y el bucle while True.
