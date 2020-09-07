(defun chunyang-eww-import-bookmarks (bookmarks-html-file)
  "Import bookmarks from BOOKMARKS-HTML-FILE."
  (interactive "fBookmarks HTML File: ")

  ;; Check if some libraries exist
  (require 'eww)
  (unless (require 'dom nil 'no-error)
    (user-error "dom.el not available, it was added in Emacs 25.1"))
  (unless (fboundp 'libxml-parse-html-region)
    (user-error "`libxml-parse-html-region' not available, \
your Emacs doesn't have libxml2 support"))

  (with-temp-buffer
    (insert-file-contents bookmarks-html-file)
    (setq eww-bookmarks
          (loop with dom = (libxml-parse-html-region (point-min) (point-max))
                for a in (dom-by-tag dom 'a)
                for url = (dom-attr a 'href)
                for title = (dom-text a)
                for time = (current-time-string
                            (seconds-to-time
                             (string-to-number
                              (dom-attr a 'add_date))))
                collect (list :url url
                              :title title
                              :time time)))
    (eww-write-bookmarks))

  )
