(defun c:WMSTOCAD ()
	(setq a (getpoint "\nSelect the lower left "))
	(setq b (getpoint "\nSelect the lower right"))
	(setq pathic (strcat "c:\\lispovska\\" "koordinata" ".txt"))
	(setq kvaliteta (getint "\nEnter the quality 4-10: "))
	(setq fajl (open pathic "w"))
		(write-line (strcat(rtos(car a))"|"(rtos(cadr a))"|"(rtos(car b))"|"(rtos(cadr b))"|"(rtos kvaliteta)) fajl)
	(close fajl)
(setq Shell (vlax-get-or-create-object "Wscript.Shell"))            
(setq updater(vlax-invoke-method Shell 'Exec "c:\\lispovska\\wtc.exe"))
(while ( = (vlax-get-property updater 'Status ) 0)  
    (command "_.delay" 1000)
)
(vlax-release-object Shell)
(setq slikapath (strcat "c:\\lispovska\\" (rtos(car a)) "-EPSG3765.tiff"))
(setq infile (open "c:\\lispovska\\koordinataizlaz.txt" "r"))
(setq x (read-line infile))
(setq y (read-line infile))
(setq mjerilo (atof (read-line infile)))
(setq umetanje (list (atof x) (atof y)))
(command "insunits" 0)
(command "image" "attach" slikapath umetanje mjerilo "0")
)
