1 class A { int x }

¿Qué error lanza ANTLR?
-no viable alternative at input 'intx}'
Esto significa que ANTLR no pudo encontrar una forma válida de interpretar el fragmento de código intx

¿En qué línea y columna ocurre?
-Línea 1, columna 16.

¿Cuál es la posible causa?
-Falta un punto y coma (;) después de la declaración del atributo int x

¿Cuál sería la corrección?
-class A { int x; }




2 class { int x; }

¿Qué error lanza ANTLR?
missing ID at '{'

¿En qué línea y columna ocurre?
Línea 1, columna 6

¿Cuál es la posible causa?
Falta el nombre de la clase después de la palabra clave class

¿Cuál sería la corrección?
Agregar un identificador para la clase, por ejemplo:

¿Cuál sería la corrección?
class A { int x; }



3 class B { int f() { x = 3; } }

¿Qué error lanza ANTLR?
missing ID at ')'

¿En qué línea y columna ocurre?
Línea 1, columna 16

¿Cuál es la posible causa?
El método f no tiene parámetros, pero el parser esperaba un identificador entre los paréntesis

¿Cuál sería la corrección?
Agregar paréntesis vacíos válidos

¿Cuál sería la corrección?
class B { int f(j) { x = 3; } }


4 class C { int f(a) { x 3; } }

¿Qué error lanza ANTLR?
no viable alternative at input 'x3'

¿En qué línea y columna ocurre?
Línea 1, columna 23

¿Cuál es la posible causa?
Falta el operador de asignación (=) entre x y 3

¿Cuál sería la corrección?
class C { int f(a) { x = 3; } }



5 class D { int f(a) { f(3; } }

¿Qué error lanza ANTLR?
missing ')' at ';'

¿En qué línea y columna ocurre?
Línea 1, columna 24

¿Cuál es la posible causa?
Falta el paréntesis de cierre ) en la llamada al método f

¿Cuál sería la corrección?
class D { int f(a) { f(3); } }


6 class E { int f(a) { x = 3 4 5; } }


¿Qué errores lanza ANTLR?

missing ';' at '4'

extraneous input '5' expecting ';'

¿En qué línea y columna ocurren?

Línea 1, columna 27

Línea 1, columna 29

¿Cuál es la posible causa?
Se están colocando múltiples valores (3 4 5) en una asignación sin separadore ;

¿Cuál sería la corrección?
Asignar un Mas a cada uno.
class E { int f(a) { x = 3 + 4 + 5; } }



7 class F { int f(a) { x = 1; } 

¿Qué error lanza ANTLR?
extraneous input '<EOF>' expecting {'}', 'int'}

¿En qué línea y columna ocurre?
Línea 1, columna 29

¿Cuál es la posible causa?
Falta la llave de cierre } del método o de la clase

¿Cuál sería la corrección?
Cerrar correctamente todas las llaves abiertas
class F { int f(a) { x = 1; } }


8 class G { x int; }

¿Qué errores lanza ANTLR?

extraneous input 'x' expecting 'int'

no viable alternative at input 'int;'

¿En qué línea y columna ocurren?

Línea 1, columna 10

Línea 1, columna 15

¿Cuál es la posible causa?
El tipo y el identificador están en orden incorrecto; se escribió x int en lugar de int x

¿Cuál sería la corrección?
Escribir primero el tipo y luego el nombre de la variable
class G { int x; }



9 class H { }

¿Qué error lanza ANTLR?
mismatched input '}' expecting 'int'

¿En qué línea y columna ocurre?
Línea 1, columna 10

¿Cuál es la posible causa?
La gramática exige que una clase tenga al menos una declaración de tipo int en su cuerpo, y actualmente está vacío

¿Cuál sería la corrección?
Agregar al menos una declaración de atributo o método con tipo int dentro de la clase
class H { int x; }


10 class I { int f(x) { a = 1; } } 


¿Qué error lanza ANTLR?
mismatched input '}' expecting {'(', INT, ID}

¿En qué línea y columna ocurre?
Línea 1, columna 21

¿Cuál es la posible causa?
El parámetro x no tiene tipo declarado, y la gramática espera un tipo antes del identificador

¿Cuál sería la corrección?
class I { int f(x) { a = 1; } }