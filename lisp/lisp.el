
(insert "niah")
(delete-char 3)sassembly of section .text:
(insert buffer-file-name)

(insert buffer-file-truename)
(progn
  (message "hello,world")
  (sleep-for 4)
  (message "nihao")
  )

(+ 1 
   3 )

(set 'a 3)
(set 'b 5)
(+ b a)

(self-insert-and-exit)
(insert ?a)
(insert-char ?c)



/home/wuming/.emacs.d/elpa/26.3/develop/helm-20190527.1253

(add-to-list 'load-path "/home/wuming/.emacs.d/elpa/26.3/develop/helm-20190527.1253")

(defgroup wm-test nil
"This is a test."
:group 'wm
  )
