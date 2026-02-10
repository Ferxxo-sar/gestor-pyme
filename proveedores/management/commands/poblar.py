# proveedores/management/commands/poblar.py
import requests
from django.core.management.base import BaseCommand
from proveedores.models import Pais, Estado, Ciudad, CodigoPostal

class Command(BaseCommand):
    help = 'Pobla la base de datos con datos reales de GeoRef API'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--limpiar',
            action='store_true',
            help='Eliminar datos existentes antes de poblar'
        )
        parser.add_argument(
            '--tipo',
            type=str,
            choices=['municipios', 'localidades', 'ambos'],
            default='ambos',
            help='Tipo de datos a cargar: municipios, localidades o ambos'
        )

    def handle(self, *args, **options):
        self.limpiar = options['limpiar']
        self.tipo = options['tipo']
        
        if self.limpiar:
            self.limpiar_datos()
        
        self.poblar_datos_georef()

    def limpiar_datos(self):
        """Elimina datos existentes de ubicaciones"""
        self.stdout.write("Limpiando datos existentes...")
        CodigoPostal.objects.all().delete()
        Ciudad.objects.all().delete()
        Estado.objects.all().delete()
        Pais.objects.filter(nombre='Argentina').delete()
        self.stdout.write(self.style.SUCCESS("Datos limpiados exitosamente"))

    def poblar_datos_georef(self):
        """Pobla la base de datos usando GeoRef API"""
        self.stdout.write("=== POBLANDO BASE DE DATOS CON GEOREF API ===")
        
        # 1. Crear país Argentina
        pais = self.crear_pais_argentina()
        
        # 2. Obtener provincias
        provincias_data = self.obtener_provincias_georef()
        self.crear_provincias(provincias_data, pais)
        
        # 3. Obtener ciudades según el tipo seleccionado
        estados_creados = Estado.objects.all()
        for estado in estados_creados:
            if self.tipo in ['municipios', 'ambos']:
                self.obtener_municipios(estado)
            if self.tipo in ['localidades', 'ambos']:
                self.obtener_localidades(estado)
        
        # 4. Agregar ciudades específicas que sabemos que queremos
        self.agregar_ciudades_especificas()
        
        # 5. Crear códigos postales
        self.crear_codigos_postales_seguro()
        
        self.mostrar_resumen()

    def crear_pais_argentina(self):
        """Crea el país Argentina"""
        pais, created = Pais.objects.get_or_create(nombre='Argentina')
        if created:
            self.stdout.write(self.style.SUCCESS(f"✓ País creado: {pais.nombre}"))
        else:
            self.stdout.write(f"✓ País existente: {pais.nombre}")
        return pais

    def obtener_provincias_georef(self):
        """Obtiene las provincias desde GeoRef API"""
        self.stdout.write("\n1. Obteniendo provincias desde GeoRef...")
        
        url = "https://apis.datos.gob.ar/georef/api/provincias"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'provincias' in data:
                self.stdout.write(self.style.SUCCESS(f"✓ Obtenidas {len(data['provincias'])} provincias"))
                return data['provincias']
            else:
                raise ValueError("Formato de respuesta inválido")
                
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Error al conectar con GeoRef: {e}"))
            return []

    def crear_provincias(self, provincias_data, pais):
        """Crea las provincias en la base de datos"""
        self.stdout.write("\n2. Creando provincias...")
        
        for prov_data in provincias_data:
            try:
                estado, created = Estado.objects.get_or_create(
                    nombre=prov_data['nombre'],
                    pais=pais
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"  ✓ Provincia: {estado.nombre}"))
            except Exception as e:
                self.stdout.write(f"  ✗ Error con provincia {prov_data['nombre']}: {e}")

    def obtener_municipios(self, estado):
        """Obtiene municipios desde GeoRef API"""
        self.stdout.write(f"\n3. Obteniendo MUNICIPIOS para {estado.nombre}...")
        
        url = f"https://apis.datos.gob.ar/georef/api/municipios?provincia={estado.nombre}&max=100"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'municipios' in data:
                creados = 0
                for mun_data in data['municipios']:
                    try:
                        ciudad, created = Ciudad.objects.get_or_create(
                            nombre=mun_data['nombre'],
                            estado=estado
                        )
                        if created:
                            creados += 1
                    except:
                        # Si hay duplicado, continuar
                        continue
                
                self.stdout.write(self.style.SUCCESS(f"  ✓ {creados} municipios para {estado.nombre}"))
                    
        except requests.RequestException:
            self.stdout.write(f"  ⚠ No se pudieron obtener municipios para {estado.nombre}")

    def obtener_localidades(self, estado):
        """Obtiene localidades desde GeoRef API (aquí está Berisso!)"""
        self.stdout.write(f"\n4. Obteniendo LOCALIDADES para {estado.nombre}...")
        
        url = f"https://apis.datos.gob.ar/georef/api/localidades?provincia={estado.nombre}&max=150"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'localidades' in data:
                creados = 0
                localidades_importantes = 0
                
                for loc_data in data['localidades']:
                    # Filtrar solo localidades importantes (ciudades, no pueblos pequeños)
                    if self.es_localidad_importante(loc_data):
                        try:
                            ciudad, created = Ciudad.objects.get_or_create(
                                nombre=loc_data['nombre'],
                                estado=estado
                            )
                            if created:
                                creados += 1
                                localidades_importantes += 1
                                if localidades_importantes <= 5:  # Mostrar primeras 5
                                    self.stdout.write(f"    • {loc_data['nombre']}")
                        except:
                            continue
                
                self.stdout.write(self.style.SUCCESS(f"  ✓ {creados} localidades para {estado.nombre}"))
                    
        except requests.RequestException:
            self.stdout.write(f"  ⚠ No se pudieron obtener localidades para {estado.nombre}")

    def es_localidad_importante(self, localidad_data):
        """Determina si una localidad es lo suficientemente importante para incluir"""
        nombre = localidad_data['nombre'].lower()
        
        # Excluir localidades muy pequeñas o específicas
        excluir = [
            'estación', 'colonia', 'villa', 'pueblo', 'paraje', 
            'comandante', 'general', 'doctor', 'sanatorio', 'hospital'
        ]
        
        for palabra in excluir:
            if palabra in nombre:
                return False
        
        # Incluir estas específicamente (como Berisso)
        incluir = ['berisso', 'ensenada', 'brandsen', 'magdalena', 'punta indio']
        
        for palabra in incluir:
            if palabra in nombre:
                return True
        
        # Por defecto, incluir localidades con categoría de ciudad
        categoria = localidad_data.get('categoria', '').lower()
        if categoria in ['ciudad', 'localidad simple']:
            return True
            
        return False

    def agregar_ciudades_especificas(self):
        """Agrega ciudades específicas que sabemos que queremos"""
        self.stdout.write("\n5. Agregando ciudades específicas...")
        
        ciudades_especificas = [
            # Buenos Aires - Partidos/Localidades importantes
            ('Berisso', 'Buenos Aires'),
            ('Ensenada', 'Buenos Aires'),
            ('Brandsen', 'Buenos Aires'),
            ('Magdalena', 'Buenos Aires'),
            ('Punta Indio', 'Buenos Aires'),
            ('Florencio Varela', 'Buenos Aires'),
            ('Berazategui', 'Buenos Aires'),
            ('Ezpeleta', 'Buenos Aires'),
            ('Guernica', 'Buenos Aires'),
            ('Longchamps', 'Buenos Aires'),
            ('Rafael Calzada', 'Buenos Aires'),
            ('Adrogué', 'Buenos Aires'),
            ('Burzaco', 'Buenos Aires'),
            ('Claypole', 'Buenos Aires'),
            ('Glew', 'Buenos Aires'),
            ('José Mármol', 'Buenos Aires'),
            ('San Francisco Solano', 'Buenos Aires'),
            ('San José', 'Buenos Aires'),
            ('Wilde', 'Buenos Aires'),
            ('Don Bosco', 'Buenos Aires'),
        ]
        
        agregadas = 0
        for ciudad_nombre, provincia_nombre in ciudades_especificas:
            try:
                estado = Estado.objects.get(nombre=provincia_nombre)
                ciudad, created = Ciudad.objects.get_or_create(
                    nombre=ciudad_nombre,
                    estado=estado
                )
                if created:
                    agregadas += 1
                    self.stdout.write(f"  ✓ {ciudad_nombre}")
            except:
                continue
        
        if agregadas > 0:
            self.stdout.write(self.style.SUCCESS(f"✓ {agregadas} ciudades específicas agregadas"))

    def crear_codigos_postales_seguro(self):
        """Crea códigos postales"""
        self.stdout.write("\n6. Creando códigos postales...")
        
        codigos_postales = {
            'Berisso': '1923',
            'Ensenada': '1925',
            'La Plata': '1900',
            'Mar del Plata': '7600', 
            # ... (el resto de tus códigos postales)
        }
        
        cp_creados = 0
        for ciudad_nombre, codigo in codigos_postales.items():
            try:
                ciudad = Ciudad.objects.filter(nombre=ciudad_nombre).first()
                if ciudad:
                    cp, created = CodigoPostal.objects.get_or_create(codigo=codigo)
                    if created:
                        cp_creados += 1
                        self.stdout.write(f"  ✓ CP {codigo} para {ciudad_nombre}")
            except:
                continue
        
        self.stdout.write(self.style.SUCCESS(f"✓ {cp_creados} códigos postales creados"))

    def mostrar_resumen(self):
        """Muestra un resumen de los datos cargados"""
        self.stdout.write("\n" + "="*50)
        self.stdout.write(self.style.SUCCESS("=== RESUMEN FINAL ==="))
        self.stdout.write(f"Países: {Pais.objects.count()}")
        self.stdout.write(f"Provincias/Estados: {Estado.objects.count()}")
        self.stdout.write(f"Ciudades: {Ciudad.objects.count()}")
        self.stdout.write(f"Códigos Postales: {CodigoPostal.objects.count()}")
        
        # Mostrar algunas ciudades de Buenos Aires como ejemplo
        bsas = Estado.objects.filter(nombre='Buenos Aires').first()
        if bsas:
            ciudades_bsas = Ciudad.objects.filter(estado=bsas)[:10]
            self.stdout.write(f"\n--- Primeras 10 ciudades de Buenos Aires ---")
            for ciudad in ciudades_bsas:
                self.stdout.write(f"  • {ciudad.nombre}")
            
        self.stdout.write("="*50)