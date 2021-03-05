; Ejercicio 01 - Diego
; Con la funcion de inserte se debe poder insertar valores a la lista ya existente y ordenarlos de manera accendente, 
;   primero se agrega el nuevo valor y despues se va ordenando mediante la recursion y detiene hasta que esten completamente ordenados
(define (insert n lista)
  (cond ((null? lista) (list n))
        ((<= n (car lista)) (cons n lista))
        (else (cons (car l) 
                    (insert (cdr lista) n)))))


; Ejercicio 03 - Sebas




; Ejercicio 06 - Pablo

