from django.shortcuts import render

def home(request):
    contexto = {
        "nombre_tienda": "tienda libre",
        "productos_destacados": [
            {
                "nombre": "A1 Combo",
                "precio": 1363990.00,
                "descripcion": "Impresora 3D FDM de estructura abierta tipo bedslinger que destaca por su alta velocidad, calibración completamente automática y capacidad de impresión multicolor gracias al sistema AMS Lite incluido.",
            },            
            {
                "nombre": "P2S Combo",
                "precio": 2944990.00,
                "descripcion": "Impresora 3D CoreXY cerrada de gama media alta que incluye el sistema automático de filamentos AMS 2 Pro para imprimir hasta en 4 colores o materiales de forma automatizada",
            },
            {
                "nombre": "Freidora de Aire Philips NA231/00",
                "precio": 199999.00,
                "descripcion": "Electrodoméstico de 6,2 litros de capacidad y 1700 W de potencia que cocina de forma rápida y saludable utilizando aire caliente.",
            },
            {
                "nombre": "Antiparras Arena Cobra Ultra Mirror Swipe Color Yellow Copper Black 350",
                "precio": 124900.00,
                "descripcion": "Gafas de natación de competición de élite, diseñadas bajo los más altos estándares hidrodinámicos y aprobadas por la World Aquatics (FINA).",
            },
            {
                "nombre": "El Principito - Antoine de Saint-Exupéry - Tapa dura",
                "precio": 31900.00,
                "descripcion": "Edición premium de tapa dura, ideal para regalo o colección. Incluye la historia completa y las ilustraciones a color originales del autor.",
            },
            {
                "nombre": "Zapatillas Samba OG",
                "precio": None,
                "descripcion": "Combinan una parte superior de cuero texturizado, puntera de gamuza sintética y la mítica suela de caucho marrón, ofreciendo el estilo retro urbano definitivo.",
            },
        ],
    }
    return render(request, "productos/home.html", contexto)

def acerca_de(request):
    return render(request, 'productos/acerca-de-mi.html')