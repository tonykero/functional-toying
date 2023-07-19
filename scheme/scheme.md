# Scheme

See [R5RS](https://people.eecs.berkeley.edu/~bh/61a-pages/Volume2/r5rs.pdf)


```scheme
; data types
(define i 2)
(define f 2.75)
(define b #t)
(define l (list a b c))

; core functions
(define symbol expression) ; declare variable 
(lambda (symbols...) <body>) ; create lambda
(apply lambda list)

; Logical
(or expr1 expr2) ; disjunction
(and expr1 expr2) ; conjunction
(= expr1 expr2) ; equality
(< expr1 expr2) ; increasing
(> expr1 expr2) ; decreasing
(if expr body1 body2)

; Mathematical
(+ expr1 expr2) ; addition
(- expr1 expr2) ; substraction
(* expr1 expr2) ; multiplication
(/ expr1 expr2) ; division

; List
(list a b c)
(cons val list) ; append val to list
(car list) ; head
(cdr list) ; tail
```
