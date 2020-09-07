(require 'shr)

(defun scrape-hurriyet-headlines ()
  "Scrape the top Hurriyet Daily News headlines.

The Hurriyet home page is expected to be laid out as follows:

<front matter>

Home Page

<topic -- LINK>
<story>

<headline>

<topic -- LINK>
<story>

<headline>

<topic -- LINK>
<story>

<headline>

...

The scraping strategy will be to jump to that home page section, then
walk down the first seven links and copy the headlines associated with
them, pasting them in to a result file.
"
  (interactive)
  (let ((site "http://www.hurriyetdailynews.com/")
        (file (find-file "~/hurriyet-headlines"))
        (headline-count 7))
    ;; Add date and time
    (switch-to-buffer file)
    (goto-char (point-min))
    (insert (format-time-string "%F %T %Z" nil t))
    (newline 2)

    ;; Give eww some time to load
    (eww site)
    (sit-for 2)

    ;; Jump to "Home Page" header
    (re-search-forward "^home page$")

    ;; Stories look like this in eww:
    ;;   <topic -- LINK>
    ;;   <story>
    ;;
    ;;   <headline>

    (dotimes (_ headline-count)
      ;; Navigate to headline
      (shr-next-link)
      (dotimes (_ 3)
        (forward-line))

      ;; Copy headline
      (set-mark-command nil)
      (move-end-of-line nil)
      (kill-ring-save t t t)
      (deactivate-mark)

      ;; Paste headline
      (switch-to-buffer file)
      (yank)
      (newline)
      (switch-to-buffer "*eww*"))

    ;; Save and prepare file for next invocation
    (switch-to-buffer file)
    (newline 2)
    (save-buffer file)))
