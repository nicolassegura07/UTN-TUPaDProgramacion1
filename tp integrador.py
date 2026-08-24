# 1. Pedir nombre del cliente (solo letras, no vacío)
nombre = input("Cliente: ").strip()
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no puede estar vacío.")
    nombre = input("Cliente: ").strip()

# 2. Pedir cantidad de productos (entero positivo > 0)
cantidad_str = input("Cantidad de productos: ").strip()
while not (cantidad_str.isdigit() and int(cantidad_str) > 0):
    print("Error: Ingrese un número entero válido mayor a 0.")
    cantidad_str = input("Cantidad de productos: ").strip()

cantidad = int(cantidad_str)

# Acumuladores
total_sin_descuentos = 0
total_con_descuentos = 0.0

# 3. Procesar cada producto con ciclo for
for i in range(1, cantidad + 1):
    # Pedir y validar precio
    precio_str = input(f"Producto {i} - Precio: ").strip()
    while not precio_str.isdigit():
        print("Error: El precio debe ser un número entero positivo.")
        precio_str = input(f"Producto {i} - Precio: ").strip()
    
    precio = int(precio_str)
    
    # Pedir y validar respuesta de descuento (S/N)
    descuento_opcion = input("Descuento (S/N): ").strip().lower()
    while descuento_opcion not in ['s', 'n']:
        print("Error: Ingrese 'S' para sí o 'N' para no.")
        descuento_opcion = input("Descuento (S/N): ").strip().lower()
    
    # Aplicar descuento si corresponde (10%)
    if descuento_opcion == 's':
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio
        
    total_sin_descuentos += precio
    total_con_descuentos += precio_con_descuento

# 4. Cálculos finales
ahorro_total = total_sin_descuentos - total_con_descuentos
promedio_por_producto = total_con_descuentos / cantidad

# Salida de resultados
print(f"\nTotal sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")



# 1. Credenciales fijas
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

# Variables para el control de acceso
intentos_maximos = 3
intento_actual = 1
acceso_concedido = False

# 2. Control de Login (máximo 3 intentos)
while intento_actual <= intentos_maximos and not acceso_concedido:
    print(f"\nIntento {intento_actual}/{intentos_maximos}")
    usuario_ingresado = input("Usuario: ").strip()
    clave_ingresada = input("Clave: ").strip()

    if usuario_ingresado == USUARIO_CORRECTO and clave_ingresada == CLAVE_CORRECTA:
        acceso_concedido = True
        print("\nAcceso concedido.")
    else:
        print("Error: credenciales inválidas.")
        intento_actual += 1

# 3. Verificar si se bloqueó la cuenta
if not acceso_concedido:
    print("\nCuenta bloqueada.")
else:
    # 4. Menú interactivo (solo si el login fue exitoso)
    opcion = ""
    while opcion != "4":
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) Estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mensaje motivacional")
        print("4) Salir")

        opcion_input = input("Opción: ").strip()

        # 5. Validaciones del menú (.isdigit() y rango 1-4)
        if not opcion_input.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion_input) < 1 or int(opcion_input) > 4:
            print("Error: opción fuera de rango.")
        else:
            opcion = opcion_input

            # Lógica según la opción elegida
            if opcion == "1":
                print("\nEstado: Inscripto")

            elif opcion == "2":
                # Cambio de clave con confirmación y longitud mínima
                nueva_clave = input("Ingrese la nueva clave: ").strip()
                
                while len(nueva_clave) < 6:
                    print("Error: La nueva clave debe tener al menos 6 caracteres.")
                    nueva_clave = input("Ingrese la nueva clave: ").strip()

                confirmacion = input("Confirme la nueva clave: ").strip()

                if nueva_clave == confirmacion:
                    CLAVE_CORRECTA = nueva_clave
                    print("¡Clave actualizada con éxito!")
                else:
                    print("Error: Las claves no coinciden. Cambio cancelado.")

            elif opcion == "3":
                print("\n«El éxito es la suma de pequeños esfuerzos repetidos día tras día.»")

            elif opcion == "4":
                print("\nHasta luego. ¡Sesión finalizada!")




# Variables para los turnos del Lunes (4 cupos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Variables para los turnos del Martes (3 cupos)
martes1 = ""
martes2 = ""
martes3 = ""

# 1. Validación del nombre del operador
operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    operador = input("Nombre del operador: ").strip()

print(f"\n¡Bienvenido/a, {operador}!")

# 2. Menú principal repetitivo
opcion = ""
while opcion != "5":
    print("\n" + "=" * 30)
    print("      AGENDA DE TURNOS")
    print("=" * 30)
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    
    opcion_input = input("Opción: ").strip()
    
    # Validar entrada del menú
    if not opcion_input.isdigit():
        print("Error: Ingrese un número válido.")
    elif int(opcion_input) < 1 or int(opcion_input) > 5:
        print("Error: Opción fuera de rango.")
    else:
        opcion = opcion_input

        # -------------------------------------------------------------
        # OPCIÓN 1: RESERVAR TURNO
        # -------------------------------------------------------------
        if opcion == "1":
            # Selección y validación del día
            dia = input("Seleccione día (1=Lunes, 2=Martes): ").strip()
            while dia not in ["1", "2"]:
                print("Error: Ingrese 1 para Lunes o 2 para Martes.")
                dia = input("Seleccione día (1=Lunes, 2=Martes): ").strip()
            
            # Nombre del paciente
            paciente = input("Nombre del paciente: ").strip()
            while not paciente.isalpha():
                print("Error: El nombre debe contener solo letras.")
                paciente = input("Nombre del paciente: ").strip()

            # Lógica para Lunes
            if dia == "1":
                # Verificar si ya tiene un turno reservado el mismo día
                if paciente.lower() in [lunes1.lower(), lunes2.lower(), lunes3.lower(), lunes4.lower()] and paciente != "":
                    print(f"Error: El paciente '{paciente}' ya tiene un turno reservado el Lunes.")
                else:
                    # Asignar en el primer espacio disponible
                    if lunes1 == "":
                        lunes1 = paciente
                        print(f"✓ Turno 1 del Lunes asignado a {paciente}.")
                    elif lunes2 == "":
                        lunes2 = paciente
                        print(f"✓ Turno 2 del Lunes asignado a {paciente}.")
                    elif lunes3 == "":
                        lunes3 = paciente
                        print(f"✓ Turno 3 del Lunes asignado a {paciente}.")
                    elif lunes4 == "":
                        lunes4 = paciente
                        print(f"✓ Turno 4 del Lunes asignado a {paciente}.")
                    else:
                        print("Error: No hay cupos disponibles para el Lunes.")

            # Lógica para Martes
            elif dia == "2":
                # Verificar si ya tiene un turno reservado el mismo día
                if paciente.lower() in [martes1.lower(), martes2.lower(), martes3.lower()] and paciente != "":
                    print(f"Error: El paciente '{paciente}' ya tiene un turno reservado el Martes.")
                else:
                    # Asignar en el primer espacio disponible
                    if martes1 == "":
                        martes1 = paciente
                        print(f"✓ Turno 1 del Martes asignado a {paciente}.")
                    elif martes2 == "":
                        martes2 = paciente
                        print(f"✓ Turno 2 del Martes asignado a {paciente}.")
                    elif martes3 == "":
                        martes3 = paciente
                        print(f"✓ Turno 3 del Martes asignado a {paciente}.")
                    else:
                        print("Error: No hay cupos disponibles para el Martes.")

        # -------------------------------------------------------------
        # OPCIÓN 2: CANCELAR TURNO
        # -------------------------------------------------------------
        elif opcion == "2":
            dia = input("Seleccione día (1=Lunes, 2=Martes): ").strip()
            while dia not in ["1", "2"]:
                print("Error: Ingrese 1 para Lunes o 2 para Martes.")
                dia = input("Seleccione día (1=Lunes, 2=Martes): ").strip()

            paciente = input("Nombre del paciente a cancelar: ").strip()
            while not paciente.isalpha():
                print("Error: El nombre debe contener solo letras.")
                paciente = input("Nombre del paciente a cancelar: ").strip()

            encontrado = False

            if dia == "1":
                if lunes1.lower() == paciente.lower():
                    lunes1 = ""
                    encontrado = True
                elif lunes2.lower() == paciente.lower():
                    lunes2 = ""
                    encontrado = True
                elif lunes3.lower() == paciente.lower():
                    lunes3 = ""
                    encontrado = True
                elif lunes4.lower() == paciente.lower():
                    lunes4 = ""
                    encontrado = True

            elif dia == "2":
                if martes1.lower() == paciente.lower():
                    martes1 = ""
                    encontrado = True
                elif martes2.lower() == paciente.lower():
                    martes2 = ""
                    encontrado = True
                elif martes3.lower() == paciente.lower():
                    martes3 = ""
                    encontrado = True

            if encontrado:
                print(f"✓ Turno de '{paciente}' cancelado exitosamente.")
            else:
                print(f"Error: No se encontró a '{paciente}' en el día seleccionado.")

        # -------------------------------------------------------------
        # OPCIÓN 3: VER AGENDA DEL DÍA
        # -------------------------------------------------------------
        elif opcion == "3":
            dia = input("Seleccione día para consultar (1=Lunes, 2=Martes): ").strip()
            while dia not in ["1", "2"]:
                print("Error: Ingrese 1 para Lunes o 2 para Martes.")
                dia = input("Seleccione día para consultar (1=Lunes, 2=Martes): ").strip()

            if dia == "1":
                print("\n--- AGENDA LUNES ---")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")

            elif dia == "2":
                print("\n--- AGENDA MARTES ---")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

        # -------------------------------------------------------------
        # OPCIÓN 4: RESUMEN GENERAL
        # -------------------------------------------------------------
        elif opcion == "4":
            # Conteo individual para Lunes
            ocupados_lunes = 0
            if lunes1 != "": ocupados_lunes += 1
            if lunes2 != "": ocupados_lunes += 1
            if lunes3 != "": ocupados_lunes += 1
            if lunes4 != "": ocupados_lunes += 1
            libres_lunes = 4 - ocupados_lunes

            # Conteo individual para Martes
            ocupados_martes = 0
            if martes1 != "": ocupados_martes += 1
            if martes2 != "": ocupados_martes += 1
            if martes3 != "": ocupados_martes += 1
            libres_martes = 3 - ocupados_martes

            print("\n--- RESUMEN GENERAL ---")
            print(f"Lunes : {ocupados_lunes} ocupados / {libres_lunes} disponibles")
            print(f"Martes: {ocupados_martes} ocupados / {libres_martes} disponibles")

            # Comparación del día con más demanda
            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos ocupados: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos ocupados: Martes")
            else:
                print("Día con más turnos ocupados: Empate entre Lunes y Martes")

        # -------------------------------------------------------------
        # OPCIÓN 5: CERRAR SISTEMA
        # -------------------------------------------------------------
        elif opcion == "5":
            print(f"\nCerrando el sistema de la agenda. ¡Hasta luego, {operador}!")



# Variables iniciales (NO se piden por teclado)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Control de la regla anti-spam
forzar_seguidas = 0

# 1. Pedir nombre del agente y validar
agente = input("Nombre del agente: ").strip()
while not agente.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    agente = input("Nombre del agente: ").strip()

print(f"\n¡Misión iniciada, Agente {agente}! Objetivo: Abrir 3 cerraduras.")

# 2. Bucle principal del juego
# Continúa mientras energia > 0, tiempo > 0, cerraduras_abiertas < 3
# y no ocurra la condición de bloqueo por alarma (alarma==True y tiempo <= 3).
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # Verificar regla de bloqueo por alarma antes de mostrar el turno
    if alarma and tiempo <= 3:
        break

    # Mostrar estado del turno
    print("\n" + "=" * 40)
    print(f"ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'Inactiva'} | Código Hackeo: [{codigo_parcial}] (largo: {len(codigo_parcial)})")
    print("=" * 40)
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía [máx 100], -1 tiempo)")

    # Pedir y validar opción del menú (debe ser número entre 1 y 3)
    opcion_input = input("Seleccione acción (1-3): ").strip()
    while not (opcion_input.isdigit() and 1 <= int(opcion_input) <= 3):
        print("Error: Seleccione un número válido entre 1 y 3.")
        opcion_input = input("Seleccione acción (1-3): ").strip()

    opcion = int(opcion_input)

    # -------------------------------------------------------------
    # OPCIÓN 1: FORZAR CERRADURA
    # -------------------------------------------------------------
    if opcion == 1:
        # Se incrementa la racha anti-spam
        forzar_seguidas += 1

        # Cobro de costos
        energia -= 20
        tiempo -= 2

        print("\n Intentando forzar la cerradura...")

        # Evaluar la Regla Anti-Spam (3er intento seguido)
        if forzar_seguidas == 3:
            alarma = True
            print(" ¡ALERTA ANTI-SPAM! Forzaste 3 veces seguidas. La cerradura se trabó y activó la alarma.")
            # NO abre cerradura
        else:
            # Riesgo de alarma por baja energía (energía < 40)
            # Nota: Se evalúa la energía restante después del cobro o el estado actual
            if energia < 40 and not alarma:
                print(" ¡PRECAUCIÓN! Energía baja (<40). Hay riesgo de activar la alarma.")
                num_input = input("Ingrese un número de seguridad (1-3): ").strip()
                while not (num_input.isdigit() and 1 <= int(num_input) <= 3):
                    print("Error: Debe ingresar un número entero entre 1 y 3.")
                    num_input = input("Ingrese un número de seguridad (1-3): ").strip()
                
                if int(num_input) == 3:
                    alarma = True
                    print(" ¡Error al manipular la cerradura! La alarma ha sido ACTIVADA.")

            # Si la alarma no se activó en este turno, abre la cerradura
            if forzar_seguidas < 3:
                cerraduras_abiertas += 1
                print(f" ✓ ¡Cerradura forzada con éxito! Total abiertas: {cerraduras_abiertas}/3.")

    # -------------------------------------------------------------
    # OPCIÓN 2: HACKEAR PANEL
    # -------------------------------------------------------------
    elif opcion == 2:
        # Corta la racha anti-spam
        forzar_seguidas = 0

        # Cobro de costos
        energia -= 10
        tiempo -= 3

        print("\n Hackeando panel de control...")
        # Bucle for de 4 pasos para simular progreso y sumar caracteres
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"  > Progreso hackeo: Paso {paso}/4 | Código: {codigo_parcial}")

        # Si el código tiene longitud >= 8, abre 1 cerradura (si faltan)
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(f" ¡Código de hackeo completo! Se abrió automáticamente 1 cerradura ({cerraduras_abiertas}/3).")
            else:
                print(" El código es correcto, pero ya están todas las cerraduras abiertas.")

    # -------------------------------------------------------------
    # OPCIÓN 3: DESCANSAR
    # -------------------------------------------------------------
    elif opcion == 3:
        # Corta la racha anti-spam
        forzar_seguidas = 0

        # Costo base
        tiempo -= 1
        
        # Recuperación de energía (máximo 100)
        energia_recuperada = 15
        
        # Penalización si la alarma está activada
        if alarma:
            print("\n Descansando con la alarma encendida (-10 energía extra por estrés)...")
            energia_recuperada -= 10

        energia += energia_recuperada
        if energia > 100:
            energia = 100

        print(f" Restableciendo fuerzas... Energía actual: {energia}")

# =================================================================
# CONDICIONES DE FIN DE JUEGO
# =================================================================
print("\n" + "*" * 40)
print("             FIN DEL JUEGO")
print("*" * 40)

if cerraduras_abiertas == 3:
    print(f" ¡VICTORIA! El Agente {agente} abrió la bóveda y completó la misión.")
elif alarma and tiempo <= 3:
    print(f" DERROTA POR BLOQUEO: La alarma sonó y el tiempo de seguridad expiró ({tiempo} turnos restantes). La bóveda se selló.")
elif energia <= 0:
    print(f" DERROTA: El Agente {agente} se quedó sin energía ({energia}).")
elif tiempo <= 0:
    print(f" DERROTA: Se agotó el tiempo disponible ({tiempo}).")



# =================================================================
# PASO 1: CONFIGURACIÓN DEL PERSONAJE
# =================================================================
print("--- BIENVENIDO A LA ARENA ---")

# Validación del nombre (solo letras y no vacío) - String
nombre_jugador = input("Nombre del Gladiador: ").strip()
while not nombre_jugador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_jugador = input("Nombre del Gladiador: ").strip()

# =================================================================
# PASO 2: INICIALIZACIÓN DE ESTADÍSTICAS
# =================================================================
# Int: Vida, pociones y daños base
hp_jugador = 100
hp_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo_base = 12

# Boolean: Control de juego / turno del jugador
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

# =================================================================
# PASO 3: EL CICLO DE COMBATE
# =================================================================
while hp_jugador > 0 and hp_enemigo > 0:

    # -------------------------------------------------------------
    # TURNO DEL JUGADOR
    # -------------------------------------------------------------
    if turno_gladiador:
        print(f"\n{nombre_jugador} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        # Validación estricta de la opción del menú
        opcion_input = input("Opción: ").strip()
        while not (opcion_input.isdigit() and 1 <= int(opcion_input) <= 3):
            print("Error: Ingrese un número válido.")
            opcion_input = input("Opción: ").strip()

        opcion = int(opcion_input)

        # ---------------------------------------------------------
        # ACCIÓN A: ATAQUE PESADO (Opción 1)
        # ---------------------------------------------------------
        if opcion == 1:
            # Float: Cálculo del daño (golpe crítico a x1.5 si HP del enemigo < 20)
            if hp_enemigo < 20:
                dano_realizado = float(ataque_pesado_base * 1.5)
                print(f" ¡GOLPE CRÍTICO!")
            else:
                dano_realizado = float(ataque_pesado_base)

            hp_enemigo -= int(dano_realizado)
            print(f"¡Atacaste al enemigo por {dano_realizado:.1f} puntos de daño!")

        # ---------------------------------------------------------
        # ACCIÓN B: RÁFAGA VELOZ (Opción 2)
        # ---------------------------------------------------------
        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            # Uso obligatorio de ciclo for
            for golpe in range(3):
                hp_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")

        # ---------------------------------------------------------
        # ACCIÓN C: CURAR (Opción 3)
        # ---------------------------------------------------------
        elif opcion == 3:
            if pociones > 0:
                hp_jugador += 30
                pociones -= 1
                print(f" Restauraste 30 puntos de vida. Te quedan {pociones} pociones.")
            else:
                print(" ¡No quedan pociones!")

        # El turno pasa al enemigo (si sigue vivo)
        turno_gladiador = False

    # -------------------------------------------------------------
    # TURNO DEL ENEMIGO
    # -------------------------------------------------------------
    if hp_enemigo > 0 and not turno_gladiador:
        hp_jugador -= ataque_enemigo_base
        print(f">> ¡El enemigo contraataca por {ataque_enemigo_base} puntos de daño!")
        
        # El turno vuelve al jugador
        turno_gladiador = True

# =================================================================
# PASO 4: FIN DEL JUEGO
# =================================================================
print("\n" + "=" * 40)
print("             FIN DEL COMBATE")
print("=" * 40)

if hp_jugador > 0:
    print(f" ¡VICTORIA! {nombre_jugador} ha ganado la batalla.")
else:
    print(f" DERROTA. Has caído en combate.")