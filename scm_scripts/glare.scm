(define (glare filename new-filename x1 y1 x2 y2)
  (let* ((image (car (gimp-file-load RUN-NONINTERACTIVE filename filename)))
	 (drawable (car (gimp-image-get-active-layer image))))
    (gimp-context-set-foreground "#FFF")
    (gimp-context-set-gradient-fg-transparent)
    (gimp-drawable-edit-gradient-fill drawable 2 0 TRUE 5 2 TRUE x1 y1 x2 x2)
    (gimp-file-save RUN-NONINTERACTIVE image drawable new-filename new-filename)
    (gimp-image-delete image)))


