from colorama import init, Fore, Back, Style

# Inicializa Colorama (para Windows)
init()

# Imprimir con diferentes colores de texto
print(Fore.RED + 'Texto en rojo')
print(Fore.GREEN + 'Texto en verde')
print(Fore.BLUE + 'Texto en azul')

# Imprimir con diferentes colores de fondo
print(Back.YELLOW + 'Fondo amarillo')
print(Back.CYAN + 'Fondo cian')

# Imprimir con diferentes estilos
print(Style.DIM + 'Texto atenuado')
print(Style.BRIGHT + 'Texto brillante')
print(Style.NORMAL + 'Texto normal')

# Restablecer a los valores por defecto
print(Style.RESET_ALL)

# Imprimir texto con combinaciones de estilos
print(Fore.RED + Back.WHITE + Style.BRIGHT + 'Texto rojo con fondo blanco y estilo brillante' + Style.RESET_ALL)

# Siempre restablece el estilo después de imprimir con color para evitar que los colores se propaguen a otras líneas
