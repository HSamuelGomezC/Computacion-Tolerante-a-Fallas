# DATOS DE ENTRADA
# Peso (kilogramos)
# Altura (centimetros)
# Fecha de Nacimiento (año)

# CLASIFICACION

# Jugador Promedio (JP)
# Peso entre los 85 kilos
# Altura entre los 180 cm
# Año de nacimiento entre 1998 y 2004

# Jugador Malo (JM)
# Peso menor a 70 kilos
# Altura menor a 170 cm
# Año de nacimiento menor al 2005 y mayor 1993 aproximadamente

# Jugador Bueno (JB)
# Peso de 90 kilos o más
# Altura de 185 cm o más
# Año de nacimiento entre 2001 y 1996 aproximadamente

# El factor mas importante para la clasificacion es el año de nacimiento, ya que se quiere que los datos se centren mas en la edad de los jugadores por referirse a un equipo de Rugby
# universitario, asi que si en un caso, por ejemplo, un jugador cumple con los rangos para ser clasificador como JB pero el año de nacimiento no cumple con los rangos especificados,
# no se clasificara como JB

# JB = 2
# JP = 1
# JM = 0

#Conexion de la BD

import pymysql
import tensorflow as tf
#import matplotlib.pyplot as plt
import subprocess


def RedNeuronal():
    # Configurar la información de conexión
    host = '82.180.172.103'  # Cambia esto al host de tu base de datos
    user = 'u292477693_root'    # Cambia esto al usuario de tu base de datos
    password = 'LJwG?Ub7.'  # Cambia esto a la contraseña de tu base de datos
    db_name = 'u292477693_rugby'  # Cambia esto al nombre de tu base de datos

    # Conectar a la base de datos
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
     # Crear un objeto cursor
     datos = 0
     with connection.cursor() as cursor:
            # Ejecutar una consulta SQL
         sql_query = "SELECT peso, altura, anio_nac, rank FROM usuarios"
         cursor.execute(sql_query)
         features = [] #Arreglo de peso, altura y año de nacimiento
         targets = []#Arreglo de ranks

         # Obtener los resultados
         results = cursor.fetchall()
         for row in results:
             datos += 1
             features.append((row['peso'],row['altura'],row['anio_nac']))
             targets.append(row['rank'])
            
         mensaje = str(datos) + ': datos cargados de la BD'
         print("\n" + mensaje + '\n')
    finally:
    # Cerrar la conexión
        connection.close()


    capaEntrada = tf.keras.layers.Dense(units=3, input_shape=[3]) # Capa de entrada con 3 neuronas, una para cada entrada que en este caso son 3 (peso,altura,año de nacimiento)
    capaOculta  = tf.keras.layers.Dense(units=4) # Capa oculta con 3 neuronas para los calculos
    capaSalida  = tf.keras.layers.Dense(units=1) # Capa de salida con una sola neurona, que se encargara de mostrar la clasificacion (JP,JM o JB)

    modelo = tf.keras.Sequential([capaEntrada, capaOculta, capaSalida]) # Modelo secuencial para este sistema, e indicando el orden de las capas

    modelo.compile( #Compilar el modelo para preparar su aprendizaje
        optimizer = tf.keras.optimizers.Adam(0.1), # Optimizador, que recibe su tasa de aprendizaje, para que sea lo mas preciso posible
        loss = 'mean_squared_error' # Perdida, en este caso se utilizo el error cuadratico medio para obtener un resultado optimo
    )

    print('Inicio de entrenamiento...') # Print para iniciar el entrenamiento

    modelo.fit(features,targets, epochs = 500, verbose = False) # Almacenar el resulta dodel entrenamiento, que le pasaremos las entradas, salidas y la repeticion de entrenamiento
    
    loss = modelo.evaluate(features, targets)
    print("Pérdida en el conjunto de prueba:", loss)

    #Para gráfica
    '''
    historial = modelo.fit(features,targets, epochs = 600, verbose = False) # Almacenar el resulta dodel entrenamiento, que le pasaremos las entradas, salidas y la repeticion de entrenamiento
    
    plt.xlabel('#Época') # Graficar la magnitud de pertida ha decrecido
    plt.ylabel('Magnitud de perdida')
    plt.plot(historial.history['loss'])
    plt.show() #Mostrar la grafica 
    '''

    print('Modelo Entrenado!') # Print para termino del entrenamiento
    modelo.save('Datos_jugadores.h5') #Exportar el modelo en formato h5 


    comando = f"tensorflowjs_converter --input_format keras Datos_jugadores.h5 ." #Variable que se utiliza para guardar el comando que se quiere utilizar
    subprocess.run(comando, shell=True, check= True)#Utilizando la libreria subprocess se ejecuta el comando ya definido, 'shell' permite que el comando se ejecute en una shell y 'check' garantiza que el proceso se detenga si se encuentra algun error en la ejecucion del comando

RedNeuronal()
