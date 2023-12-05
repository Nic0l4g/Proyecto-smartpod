# Proyecto-smartpod

Este proyecto contiene el código para el funcionamiento del dispositivo Smartpod, que es un sistema de monitoreo y cuidado de plantas basado en micro python y la ESP32. También contiene el código y las instrucciones para la creación de la aplicación móvil que se comunica con el dispositivo y muestra los datos de los sensores en una interfaz de usuario.

## Requisitos

Para utilizar el dispositivo, es necesario contar con:

- Un IDE que soporte micro python y la ESP32. En este caso, se usó Thonny para desarrollar el dispositivo.
- Un driver para que el computador reconozca el dispositivo micro python. El driver se puede descargar de la carpeta de archivos necesarios.
- Un archivo .bin para cargar micro python en la ESP32. El archivo también está en la carpeta de archivos necesarios.
- Tres archivos .py que contienen el código principal y las bibliotecas necesarias para el funcionamiento del dispositivo. Los archivos se pueden encontrar en la carpeta de código del dispositivo de este repositorio.
- Cuatro sensores: DHT11 (humedad y temperatura ambiente), sensor de humedad del suelo capacitivo, sensor de luz y pantalla oled de 4 pines.
- Una base de datos en Firebase para almacenar y enviar los datos de los sensores. Se debe crear un proyecto en la página de Firebase y enlazarlo con la aplicación móvil siguiendo los pasos que se muestran en la documentación de Firebase.
- Android Studio para la creación de la aplicación móvil. Se debe importar el código de la aplicación que se encuentra en la carpeta de código de la aplicación de este repositorio.

## Instalación

Para instalar el dispositivo, se debe seguir los siguientes pasos:

- Conectar la ESP32 al computador por medio de un cable USB.
- Abrir el IDE Thonny y seleccionar la ruta de “Herramientas - Opciones - Intérprete".
- Elegir el archivo .bin que contiene micro python y cargarlo al dispositivo.
- Descargar los 3 archivos .py que contienen el código del dispositivo y guardarlos en la memoria de la ESP32.
- Modificar el main en las líneas 13 y 14 del código con el SSID y la contraseña de la red a la que se desea conectar el dispositivo.
- Conectar los sensores a la placa de desarrollo siguiendo el esquema de conexión que se muestra en la figura 1 de la página web.
- Ejecutar el código en el dispositivo y verificar que se conecte a la red wifi y a la base de datos de Firebase.

Para instalar la aplicación móvil, se debe seguir los siguientes pasos:

- Abrir Android Studio e importar el código de la aplicación que se encuentra en la carpeta de código de la aplicación de este repositorio.
- Enlazar la aplicación con el proyecto de Firebase siguiendo los pasos que se muestran en la documentación de Firebase [3].
- Habilitar la opción de entrada de variables de tipo int, char y string en la base de datos de Firebase para la autenticación de usuarios.
- Ejecutar la aplicación en un emulador o en un dispositivo móvil y verificar que se pueda acceder a la pantalla de login, sign in, menú home y estado de las plantas.

## Uso

Para usar el dispositivo, se debe colocar cerca de la planta que se desea monitorear y cuidar. El dispositivo leerá los valores de los sensores de humedad y temperatura ambiente, humedad del suelo y luz, y los enviará a la base de datos de Firebase cada cierto tiempo. El dispositivo también mostrará en la pantalla oled una expresión que indica el estado de la planta según los valores de los sensores.

Para usar la aplicación móvil, se debe crear una cuenta de usuario con un correo electrónico y una contraseña. Luego, se podrá acceder al menú home, donde se podrá ver un botón que habilita/actualiza la lectura de los sensores. Al presionar el botón, se podrá acceder a la pantalla del estado de las plantas, donde se mostrarán los valores de los sensores en una barra de progreso y en porcentaje, así como el estado de la planta en color.

## Autores
° Nicolas Garcia Guerrero - Estudiante de ingenieria electronica - Universidad Nacional de Colombia (sede Bogota).

° Juan Felipe Velasquez Jaramillo - Estudiante de ingenieria electronica - Universidad Nacional de Colombia (sede Bogota).

