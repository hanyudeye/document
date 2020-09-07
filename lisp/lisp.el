
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

(add-to-list 'load-path "/home/wuming/.emacs.d/elpa/26.3/develop/helm-20190527.1253")

(defgroup wm-test nil
"This is a test."
:group 'wm
  )

(defun my-youdao-fanyi()
  (interactive)
  (my-youdao-dictionary-search-at-point+)
  )


(+ 99 32)
(message "小鸟在唱歌")


(next-window)

(previous-line)

(insert ?x)

(def-package! lsp-python-ms
  :demand nil
  :hook (python-mode . lsp)
  :config
  ;; for executable of language server, if it's not symlinked on your PATH
  (setq lsp-python-ms-executable
        (string-trim (shell-command-to-string
                      "fd -a ^Microsoft.Python.LanguageServer$ $HOME/.vscode/extensions | tail -1")))
  ;; for dev build of language server
  (setq lsp-python-ms-dir
        (file-name-directory lsp-python-ms-executable)))

(current-buffer)

#<buffer lisp.el>

(current-fill-column)
(date)


(alert "hello")
