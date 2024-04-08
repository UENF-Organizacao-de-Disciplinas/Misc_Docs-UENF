;; Introdução à Linguagem Scheme-Racket
;; Prof. Ausberto S. Castro Vera       (ascv@uenf.br)
;; UENF-CCT-LCMAT - Curso de Ciencia da Computacao
;; Setembro - 2021 
;; Aluno: João Vítor Fernandes Dias
#lang racket      ;; define a linguagem default
; ------------------------------------------------
(display "  UENF-CCT-LCMAT-CC, 2021") (newline)
(display "  Paradigmas de Linguagens de Programação (Prof. Ausberto Castro)") (newline)
(display "  Aluno:  João Vítor Fernandes Dias ") (newline) (newline) (newline)

(define-struct data     (dia mes ano))
(define-struct endereco (bairro rua numero))
(define-struct dadoPessoal (data endereco))

(define (mostrarDadosPessoais pessoa) (begin (
  ;geral
  (display "Data de nascimento: ")  (display dadoPessoal-data)
  (display "Endereço: ")            (display dadoPessoal-endereco)
  (newline) (newline)
  ;Mais específico
  ;(display "Data de nascimento: (")  (display dadoPessoal-data-dia)
  ;(display "/")  (display dadoPessoal-data-mes)
  ;(display "/")  (display dadoPessoal-data-ano)
  ;(display ")") (newline)

  ;(display "Endereço: (Bairro: ") (display dadoPessoal-endereco-bairro)
  ;(display "; Rua: ") (display dadoPessoal-endereco-rua)
  ;(display "; Número: ") (display dadoPessoal-endereco-numero)
  ;(display ")") (newline)
)))

(define lerDadosPessoais (begin (
  (display "Digite sua data de nascimento: ") (newline)

  (display "Dia: ")   (define d (read))
  (display "Mês: ")   (define m (read))
  (display "Ano: ")   (define a (read))
  (define nascimento (make-data d m a))

  
  
  (display "Digite seu endereço: ") (newline)
  (display "Bairro: ")   (define b (read))
  (display "Rua:    ")   (define r (read))
  (display "Número: ")   (define n (read))
  (define casa (make-endereco b r n))

  (define pessoa (make-dadoPessoal casa nascimento))

  (mostrarDadosPessoais pessoa)
)))

(lerDadosPessoais)
(lerDadosPessoais)

