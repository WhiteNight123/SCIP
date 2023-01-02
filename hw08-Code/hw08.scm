;;; HW08: Scheme

;;; Required Problems

(define (square x) (* x x))

(define (pow base exp)
  'YOUR-CODE-HERE
  (cond ((= exp 0) 1)
    ((even? exp) (square (pow base (/ exp 2))))
    (else (* base (pow base (- exp 1)))))
)


(define (filter-lst fn lst)
  'YOUR-CODE-HERE
  (cond ((null? lst) lst)
    ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
    (else (filter-lst  fn (cdr lst))))
)


(define (no-repeats s)
  'YOUR-CODE-HERE
  (cond ((null? s) nil)
    (else (cons (car s)
        (no-repeats (filter-lst (lambda (x) (not (= x (car s)))) (cdr s)))
        )))
)


(define (substitute s old new)
  'YOUR-CODE-HERE
  (if (null? s)
  ()
  (if (eq? (car s) old)
  (cons new (substitute (cdr s) old new))
  (if (pair? (car s))
  (cons (substitute (car s) old new) (substitute (cdr s) old new))
  (cons (car s) (substitute (cdr s) old new)))))
)


(define (sub-all s olds news)
  'YOUR-CODE-HERE
  (if (or (null? s) (null? olds))
  s
  (sub-all (substitute s (car olds) (car news))(cdr olds)(cdr news)))
)


(define (tree label branches)
  'YOUR-CODE-HERE
  (cons label branches)
)

(define (label t)
  'YOUR-CODE-HERE
  (car t)
)

(define (branches t)
  'YOUR-CODE-HERE
  (cdr t)
)

(define (is-leaf t)
  'YOUR-CODE-HERE
  (if (null? (branches t))#t #f)
)

; A tree for test

(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 5 nil)
          (tree 6 (list
            (tree 8 nil)))))
    (tree 3 nil)
    (tree 4
      (list
        (tree 7 nil))))))


(define (label-sum t)
  'YOUR-CODE-HERE
  (+ (label t) (sum (map label-sum (branches t))))
)

(define (sum lst)
(if (null? lst) 0 (+ (car lst) (sum (cdr lst)))))


;;; Just for fun Problems

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (first-operand s) (cadr s))
(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
; You can access the operands from the expressions with
; first-operand and second-operand
(define (first-operand p) (cadr p))
(define (second-operand p) (caddr p))

(define (derive-sum expr var)
  'YOUR-CODE-HERE
  (make-sum (derive (first-operand expr) var)
  (derive (second-operand expr) var))
)

(define (derive-product expr var)
  'YOUR-CODE-HERE
  (make-sum
    (make-product (derive (first-operand expr) var)
        (second-operand expr))
    (make-product (derive (second-operand expr) var)
        (first-operand expr)))
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  'YOUR-CODE-HERE
  (cond ((and (number? base) (number? exponent)) (expt base exponent))
    ((=number? exponent 0) 1)
    ((=number? exponent 1) base)
    (else (list '^ base exponent)))
)



(define (exp? exp)
  'YOUR-CODE-HER
  (and (list? exp) (eq? (car exp) '^))
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  'YOUR-CODE-HERE
  (make-product (second-operand exp)
    (make-exp (first-operand exp)
       (- (second-operand exp) 1)))
)
