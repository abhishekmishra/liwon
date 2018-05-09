(define (make-model name params)
  (list
   (list "name" name)
   (list "params" params)))

(define (model-name model)
  (cadar model))

(define (model-params model)
  (cadadr model))

(define model-test (make-model "tm" '("p1" "p2")))

(display model-test)

(display (model-name model-test))
(display (model-params model-test))


;todo: we need to cdr down the params
;and create pairs for each param and its value
(define (make-model-instance model name)
  (list
   (list "name" name)
   (list "model-name" (model-name model))
   (list "params" (model-params model))))

