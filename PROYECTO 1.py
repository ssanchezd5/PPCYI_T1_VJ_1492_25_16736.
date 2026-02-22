import xml.etree.ElementTree as ET


# ----------------- CLASE VUELO -----------------
class Vuelo:
    def __init__(self, codigo, origen, destino, duracion, aerolinea):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.duracion = int(duracion)
        self.aerolinea = aerolinea

    def mostrar(self):
        print("\n--- DETALLE DEL VUELO ---")
        print("Código:", self.codigo)
        print("Origen:", self.origen)
        print("Destino:", self.destino)
        print("Duración:", self.duracion)
        print("Aerolínea:", self.aerolinea)


# ----------------- SISTEMA -----------------
class SistemaVuelos:
    def __init__(self):
        self.vuelos = []

    # 1️⃣ Cargar XML
    def cargar_archivo(self, ruta):
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()

            self.vuelos.clear()

            codigos = set()

            for vuelo_xml in root.findall("vuelo"):
                codigo = vuelo_xml.find("codigo").text

                if codigo in codigos:
                    print("Error: Código repetido:", codigo)
                    continue

                codigos.add(codigo)

                origen = vuelo_xml.find("origen").text
                destino = vuelo_xml.find("destino").text
                duracion = vuelo_xml.find("duracion").text
                aerolinea = vuelo_xml.find("aerolinea").text

                vuelo = Vuelo(codigo, origen, destino, duracion, aerolinea)
                self.vuelos.append(vuelo)

            print("Archivo cargado correctamente.")

        except Exception as e:
            print("Error al cargar archivo:", e)

    # 2️⃣ Buscar vuelo
    def detalle_vuelo(self, codigo):
        for vuelo in self.vuelos:
            if vuelo.codigo == codigo:
                vuelo.mostrar()
                return
        print("Vuelo no encontrado.")

    # 3️⃣ Agrupar por aerolínea
    def agrupar_por_aerolinea(self):
        grupos = {}

        for vuelo in self.vuelos:
            if vuelo.aerolinea not in grupos:
                grupos[vuelo.aerolinea] = []
            grupos[vuelo.aerolinea].append(vuelo.codigo)

        for aerolinea, codigos in grupos.items():
            print("\nAerolínea:", aerolinea)
            for c in codigos:
                print(" -", c)

    # 4️⃣ Ordenar por duración
    def ordenar_por_duracion(self):
        ordenados = sorted(self.vuelos, key=lambda x: x.duracion, reverse=True)

        print("\n--- Vuelos ordenados (Mayor a menor duración) ---")
        for vuelo in ordenados:
            print(vuelo.codigo, "-", vuelo.duracion, "horas")


# ----------------- MENÚ -----------------
def menu():
    sistema = SistemaVuelos()

    while True:
        print("\n------ MENÚ AEROLÍNEA ------")
        print("1. Cargar Archivo")
        print("2. Detalle de vuelo específico")
        print("3. Agrupar vuelos por aerolínea")
        print("4. Ordenar más duración a menor duración")
        print("5. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            ruta = input("Ingrese ruta del archivo XML: ")
            sistema.cargar_archivo(ruta)

        elif opcion == "2":
            codigo = input("Ingrese código del vuelo: ")
            sistema.detalle_vuelo(codigo)

        elif opcion == "3":
            sistema.agrupar_por_aerolinea()

        elif opcion == "4":
            sistema.ordenar_por_duracion()

        elif opcion == "5":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()