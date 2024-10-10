(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false)  
)


(define (square n) (* n n))

(define (pow-expr base exp) 
   (define (pow-expr-helper base exp)
    (cond ((= exp 0) 1)
          ((= exp 1) `(* ,base 1))
          ((even? exp) `(square ,(pow-expr-helper base (/ exp 2))))
          (else `(* ,base (square ,(pow-expr-helper base (/ (- exp 1) 2)))))))
  (pow-expr-helper base exp))

(define-macro (repeat n expr)
  `(repeated-call ,n (lambda(),expr)))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      (f)
      (begin repeated-call (- n 1) f)))
