from TP3.CSV import CSV


bolsaMadrid=CSV('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000')

bolsaMadrid.obtenerCSV('id','ctl00_Contenido_tblAcciones','bolsaMadrid')
