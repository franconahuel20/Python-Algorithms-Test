# Python/algorithms Test
# [Ejercicio: La constante de Dattatreya Ramachandra Kaprekar (el mágico número: 6174)](https://en.wikipedia.org/wiki/D._R._Kaprekar)

Se debe leer un número cualquiera de 4 dígitos, y hacer la siguiente
operación inicial: tomar cada uno de los 4 dígitos del número leído, y ordenarlos de forma descendente (de mayor a menor) conformando un número al que pueden llamar ParteA y ordenarlos también de forma ascendente
(de menor a mayor) conformando otro número al que pueden llamar ParteB, y
entonces hacer la diferencia entre ParteA y ParteB.

Si la diferencia es 6174, se terminó el cálculo y solo hubo una iteración, sino, entonces iterativamente, se
debe hacer el siguiente cálculo: ordenar los dígitos de la diferencia de forma descendente (de mayor a
menor) conformando un número al que pueden llamar ParteA y ordenarlos también de forma ascendente
(de menor a mayor) conformando otro número al que pueden llamar ParteB, calcular nuevamente la
diferencia (imprimir ambas partes y la diferencia), si esta diferencia es 6174, entonces se rompe el ciclo y
se despliega al usuario en número de iteraciones.

Si la diferencia no es 6174, entonces vuelve y se repite el cálculo conformando nuevamente los dos
números ordenados, pero tomando como base la nueva diferencia calculada. Deben imprimir la
diferencia encontrada y las llamadas partes A y B en cada iteración, también el número de la iteración
(que arranca en 1). Al final deben imprimir igualmente el número de iteraciones que tardaron para
encontrar la constante de Kaprekar (6174).

- NOTA 1: No funciona cuando los 4 dígitos son iguales (Por ejemplo: 3333). Entonces, se sugiere informar al usuario.
- NOTA 2: Cuando las diferencias son números de menos de 4 dígitos (Por ejemplo: 23), se toman los ceros a la izquierda como dígitos (Así: 0023).

Los resultados de cada iteración (ParteA, ParteB, Diferencia y Observaciones) deben guardarse en un
archivo plano (.txt), separado por el carácter punto y coma (;).
IMPORTANTE: El uso de bloque de excepción para control de errores es obligatorio.
REQUISITO ADICIONAL: Debe implementarse una batería de pruebas unitarias (mínimo dos casos, los
que están representados en los siguientes ejemplos).

- Ejemplo 1:

Cálculo|ParteA|ParteB|Diferencia|Observaciones
---|---|---|---|---
Número Leído - Dígitos Núm. Leído (ASC)| 8963| 3689| 5274| Cálculo Inicial, Iteración 1
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 7542| 2457| 5085| Iteración 2
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 8550| 0558| 7992| Iteración 3
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 9972| 2799| 7173| Iteración 4
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)|7731| 1377| 6354| Iteración 5
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 6543| 3456| 3087| Iteración 6
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 8730| 0378| 8352| Iteración 7
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 8532| 2358| 6174| Iteración 8, ¡¡¡KAPREKAR Encontrado!!!.

- Ejemplo 2:

Cálculo|ParteA|ParteB|Diferencia|Observaciones
---|---|---|---|---
Número Leído - Dígitos Núm. Leído (ASC)| 1000| 0001| 999| Cálculo Inicial, Iteración 1
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 9990| 0999| 8991| Iteración 2
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 9981| 1899| 8082| Iteración 3
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 8820| 0288| 8532| Iteración 4
Diferencia iter. ant.(DESC) - Diferencia iter. ant.(ASC)| 8532| 2358| 6174| Iteración 5, ¡¡¡KAPREKAR Encontrado!!!.