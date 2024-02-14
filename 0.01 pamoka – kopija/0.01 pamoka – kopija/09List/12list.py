cmUgis = [201, 200, 185, 175, 205, 198, 187, 168, 156, 201, 211, 164] 

colisUgis = [round(cm/2.54, 2) for cm in cmUgis ]
print(colisUgis)
txtUgis=['Aukš.' if cm >= 186 else 'Vid.' for cm in cmUgis]
print(txtUgis)
txtUgisKitas=['Aukš.' if cm >= 186 else 'Vid.' if cm >= 170 else 'Zem.' for cm in cmUgis]
print(txtUgisKitas)