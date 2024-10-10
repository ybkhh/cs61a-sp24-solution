(define (curry-cook formals body) 
(if (null? formals)
    body
    `(lambda ,(cons (car formals) nil) ,(curry-cook (cdr formals) body))
  )
)

(define (curry-consume curry args)
  (if (null? args)
      curry
      (curry-consume (curry (car args)) (cdr args))
  )  
)
  (curry-helper formals))
(define (curry-consume curry args)
  'YOUR-CODE-HERE)


(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))
  (cons 'cond
        (map
         (lambda (case) (cons `(equal? ,(car (cdr switch-expr)) ,(car case)) (cdr case)))
         (car (cdr (cdr switch-expr))))))

(define (switch-to-cond switch-expr)
  (cons _________
        (map (lambda (option)
               (cons _______________ (cdr option)))
             (car (cdr (cdr switch-expr))))))
