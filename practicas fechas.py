from datetime import datetime, timedelta
hoy= datetime.now()
#print("hoy es : " + str(hoy))
#un_dia= timedelta(days=1)
#mañana= hoy + un_dia
#print("mañana es: " + str(mañana))

#una_semana= timedelta(weeks=1)
#semana_pasada= hoy - una_semana
#print("semana_pasada: " + str(semana_pasada))
print("dia: " + str(hoy.day))
print("semana: " + str(hoy.weekday))
print("mes: " + str(hoy.month))
print("año: " + str(hoy.year))
print("hora: " + str(hoy.hour))
print("segundo: " + str(hoy.second))
