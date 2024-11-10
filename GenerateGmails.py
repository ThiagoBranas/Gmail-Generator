import random
import string
import smtplib
import dns.resolver

def generar_correo(dominio="gmail.com"):
    """Genera una dirección de correo electrónico aleatoria con un dominio especificado."""
    nombres = set(["juan", "maria", "pedro", "laura", "carlos", "ana", "jose", "susana", "manuel", "rosa", 
                   "miguel", "elena", "fernando", "luis", "adriana", "roberto", "alicia", "ramon", "martina", 
                   "emilio", "clara", "eduardo", "mercedes", "nicolas", "silvia", "juanita", "leonardo", "amparo", 
                   "raul", "cecilia", "hector", "carmen", "jorge", "ines", "ricardo", "elisa", "francisco", 
                   "marina", "oscar", "veronica", "daniel", "isabel", "pablo", "graciela", "marcelo", "juana", 
                   "matias", "estela", "angel", "lucia", "sergio", "valentina", "ruben", "natalia", "gregorio", 
                   "patricia", "felipe", "adolfo", "rosario", "juanita", "alejandro", "andrea", "gustavo", "rocio", 
                   "martin", "luciana", "juan carlos", "ana maria", "omar", "leticia", "alberto", "luisa", 
                   "carlosalberto", "pilar", "antonio", "flavia", "enrique", "marcela", "adolfo", "rosario", 
                   "rafael", "constanza", "esteban", "carolina", "gonzalo", "dolores", "lucas", "renata", "beatriz", 
                   "agustin", "teresa", "guillermo", "monica", "hugo", "camila", "felix", "claudia", "dario", "nora", 
                   "javier", "valeria", "maximiliano", "sofia", "raul", "ines", "rodrigo", "liliana", "juan pablo", 
                   "susana", "omar", "carina", "dante", "elena", "osvaldo", "luciana", "ruben", "mariana", "gerardo", 
                   "nadia", "alejandro", "graciela", "julian", "ana clara", "agustin", "claudia", "martin", "julieta"])

    apellidos = set(["gomez", "rodriguez", "fernandez", "perez", "lopez", "gonzalez", "martinez", "sanchez", 
                     "ramirez", "garcia", "silva", "ruiz", "martin", "sosa", "morales", "aguilar", "castro", "vera", 
                     "dominguez", "soto", "bustos", "mendez", "arias", "paredes", "fernando", "olivera", "bravo", 
                     "romero", "padilla", "herrera", "guerrero", "vasquez", "cabrera", "gutierrez", "medina"])

    numero = random.randint(200, 1998)
    nombre = random.choice(list(nombres))
    apellido = random.choice(list(apellidos))

    correo = f"{nombre}{apellido}{numero}@{dominio}"
    return correo

def verificar_correo(correo):
    """Verifica si un correo electrónico existe en el servidor SMTP."""
    try:
        # Extraemos el dominio del correo y buscamos los registros MX.
        dominio = correo.split('@')[1]
        registros_mx = dns.resolver.resolve(dominio, 'MX')
        servidor_mx = str(registros_mx[0].exchange)

        # Conexión al servidor SMTP para verificar la existencia del correo.
        with smtplib.SMTP(servidor_mx) as conexion_smtp:
            conexion_smtp.set_debuglevel(0)  # Desactiva la depuración del servidor SMTP
            conexion_smtp.ehlo_or_helo_if_needed()
            conexion_smtp.mail('tu_correo@dominio.com')  # Usar un correo de remitente válido
            codigo, mensaje = conexion_smtp.rcpt(correo)

            # Si el código es 250, el correo es válido.
            if codigo == 250:
                return True
    except dns.resolver.NoAnswer as e:
        print(f"No se encontró respuesta DNS para el dominio {dominio}: {e}")
    except smtplib.SMTPException as e:
        print(f"Error SMTP al verificar el correo {correo} en el servidor {servidor_mx}: {e}")
    except Exception as e:
        print(f"Error inesperado al verificar el correo {correo}: {e}")
    return False

def generar_y_verificar_correos(cantidad=100):
    """Genera y verifica una cantidad especificada de correos electrónicos."""
    for _ in range(cantidad):
        correo = generar_correo()
        if verificar_correo(correo):
            print(f"\033[92m{correo}\033[0m")  # Verde (Correo válido)
        else:
            print(f"\033[91m{correo}\033[0m")  # Rojo (Correo no válido)

if __name__ == '__main__':
    generar_y_verificar_correos(100)  # Cambia la cantidad si es necesario
