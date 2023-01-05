;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (cond
    ((null? s) nil)
    ((f (car s)) (cons-stream (car s) (filter-stream f (cdr-stream s))))
    (else (filter-stream f (cdr-stream s))))
)


(define (slice s start end)
  'YOUR-CODE-HERE
  (cond
    ((or (null? s) (= end 0)) nil)
    ((> start 0)
      (slice (cdr-stream s) (- start 1) (- end 1)))
    (else
      (cons (car s)
        (slice (cdr-stream s) (- start 1) (- end 1)))))
)

(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (cons-stream 1 (combine-with * (naturals 1) factorials))
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))
)

(define (pow n power)
  (define (pow-tail power-tail number-so-far)
    (if (= power-tail power)
      number-so-far (pow-tail (+ power-tail 1) (* number-so far n))
    )
)
(pow-tail 0 1))

(define (exp x)
  (let ((terms (combine-with (lambda (a b) (/ (expt x a) b))
    (cdr-stream (naturals 0))
    (cdr-stream factorials))))
  (cons-stream 1 (combine-with + terms (exp x))))
)


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (cond ((null? s) nil)
    ((null? (cdr-stream s)) (cons-stream (list (car s)) nil))
    (else (if (> (car s) (car (cdr-stream s)))
      (cons-stream (list (car s)) (nondecrease (cdr-stream s)))
      (let ((rest (nondecrease (cdr-stream s))))
        (cons-stream (cons (car s) (car rest)) (cdr-stream rest))))))
)


;;; Just For Fun Problems

(define-macro (my-cons-stream first second) ; Does this line need to be changed?
  `(list, first (lambda (), second))
)

(define (my-car stream)
  (car stream)
)

(define (my-cdr-stream stream)
  ((car (cdr stream)))
)


(define (sieve s)
  (cons-stream (car s)     
    (sieve (filter-stream (lambda (x) (< 0 (remainder x (car s)))) (cdr-stream s))))
)

(define primes (sieve (naturals 2)))
