import random
import string

class GeneradorContrasena:
    """
    Clase encargada de la lógica de generación de contraseñas seguras.
    Permite personalizar la longitud y los tipos de caracteres incluidos.
    """

    def __init__(self):
        # Config
        self.textos = {
            "preg_longitud": "Introduce la longitud de la contraseña (mínimo 8): ",
            "err_numero": "Error: Debe ingresar un número entero.",
            "err_minimo": "Por seguridad, la longitud mínima es 8.",
            "preg_mayus": "¿Incluir mayúsculas? (s/n): ",
            "preg_num": "¿Incluir números? (s/n): ",
            "preg_sym": "¿Incluir símbolos? (s/n): ",
            "resultado": "\nTu contraseña generada es: "
        }

    def obtener_configuracion_usuario(self) -> dict:
        """
        Interactúa con el usuario para obtener los parámetros de la contraseña.
        
        Returns:
            dict: Un diccionario con las preferencias del usuario.
        """
        while True:
            try:
                largo = int(input(self.textos["preg_longitud"]))
                if largo >= 8: break
                print(self.textos["err_minimo"])
            except ValueError:
                print(self.textos["err_numero"])

        config = {
            "longitud": largo,
            "mayus": input(self.textos["preg_mayus"]).lower() == 's',
            "nums": input(self.textos["preg_num"]).lower() == 's',
            "syms": input(self.textos["preg_sym"]).lower() == 's'
        }
        return config

    def construir_pool_caracteres(self, usar_mayus: bool, usar_nums: bool, usar_syms: bool) -> str:
        """
        Crea una cadena de texto con todos los caracteres posibles según la elección.

        Args:
            usar_mayus (bool): Indica si se incluyen letras mayúsculas.
            usar_nums (bool): Indica si se incluyen dígitos.
            usar_syms (bool): Indica si se incluyen signos de puntuación.

        Returns:
            str: Conjunto total de caracteres disponibles para la contraseña.
        """
        caracteres = string.ascii_lowercase
        if usar_mayus:
            caracteres += string.ascii_uppercase
        if usar_nums:
            caracteres += string.digits
        if usar_syms:
            caracteres += string.punctuation
        return caracteres

    def generar(self, parametros: dict) -> str:
        """
        Realiza la selección aleatoria de caracteres mediante un bucle repetitivo.

        Args:
            parametros (dict): Diccionario con longitud y booleanos de configuración.

        Returns:
            str: La contraseña final generada.
        """
        pool = self.construir_pool_caracteres(
            parametros["mayus"], 
            parametros["nums"], 
            parametros["syms"]
        )
        
        contrasena = "".join(random.choice(pool) for _ in range(parametros["longitud"]))
        return contrasena

if __name__ == "__main__":
    app = GeneradorContrasena()
    
    print("==============================================")
    print("SISTEMA DE CIBERSEGURIDAD UIDE")
    print("Tema: Impacto de las Tecnologías en la Sociedad")
    print("==============================================\n")
    
    ajustes = app.obtener_configuracion_usuario()
    password_final = app.generar(ajustes)
    
    print(f"{app.textos['resultado']}{password_final}")
    print("\nReflexión: Una sociedad digital segura empieza con una contraseña robusta.")