;;; Lab08: Scheme

(define (over-or-under a b)
  'YOUR-CODE-HERE
  (cond
    ((< a b) -1)
    ((= a b) 0)
    (else 1)))


(define (make-adder n)
  'YOUR-CODE-HERE
  (lambda (k) (+ n k))
)


(define (composed f g)
  'YOUR-CODE-HERE
  (lambda (x) (f (g x)))
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  'YOUR-CODE-HERE
  (if (= b 0)
    a
    (gcd b (remainder a b)))
)


(define lst
  'YOUR-CODE-HERE
  (cons (cons 1 nil)
    (cons 2
        (cons (cons 3 (cons 4 nil))
            (cons 5 nil))))
)


(define (ordered s)
  'YOUR-CODE-HERE
  (cond
    ((null? s) #t)
    ((null? (cdr s)) #t)
    ((<= (car s) (car (cdr s))) (ordered (cdr s)))
    (else #f)
   )
)
