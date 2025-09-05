/*

Implemente un código que lea un archivo de texto y cuente cuántas líneas
tiene.

*/


#include <stdio.h>

int main (){

    char contenido [1024];                              // Uso un buffer grande para leer líneas del archivo
    FILE *archivo_nombres;                              // Puntero para el archivo
    int conteo_lineas = 0;

    archivo_nombres = fopen("texto.txt", "r");      
  
    // Abro el archivo en modo lectura de texto
    // Abro el archivo en modo lectora R porque no es un archivo binario
   
    if (!archivo_nombres) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    /*

    -   Uso fgets para leer línea por línea
    -   fgets lee hasta que encuentra un salto de línea o el final del archivo
    -   Mientras pueda leer una línea del archivo, incremento el contador
    -   fgets devuelve NULL cuando llega al final del archivo

    */

    while (fgets(contenido, sizeof(contenido), archivo_nombres) != NULL) {

        //printf(" %s", contenido);  // Imprimo la línea leída
        conteo_lineas++;

    }

    printf("\nLa cantidad de lineas en el archivo es: %d", conteo_lineas);

    return 0;
}