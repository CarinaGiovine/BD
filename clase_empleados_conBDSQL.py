# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:40:45 2021

@author: CarinaGiovine
"""
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=81&codigo=81&inicio=75  ver ese codigo
class Empleado():
    
    def __init__(self):
        pass
    
    '''def conexion(self):
        import pymysql
        conn = pymysql.connect(
        host='127.0.0.1', user='root',
        passwd='', db='employees')
        cursor = conn.cursor()'''
        
    def menu(): 
       #e=Empleado()
    
       opcion=0
       print("Menú de opciones: ")
       print(" 1- Agregar un nuevo Empleado.")
       print(" 2- Buscar un Empleado. ")
       print(" 3- Modificar/Actulizar datos de un empleado. ")
       print(" 4- Eliminar un empleado.")
       print(" 5- Salir")
       opcion=int(input("Ingresa la opción deseada: "))
       if opcion==1:
           e.agregar_empleado()
       elif opcion==2:
           e.buscar_empleado()
       elif opcion==3:
           e.modificar_empleado()
       elif opcion==4:
           e.eliminar_empleado()
       else:
           print("Gracias.")
   
        
    def agregar_empleado():
        #conexion()
        import pymysql
        conn = pymysql.connect(
        host='127.0.0.1', user='root',
        passwd='', db='employees')
        cursor = conn.cursor()
        nro_em=int(input("Ingresa el número del nuevo empleado: "))
        b_day=input("Ingresa la fecha de nacimiento formato aaaa/mm/dd: ")
        nombre=input("Ingrese en nombre: ")
        apellido=input("Ingrese el apellido: ")
        genero=input("Ingrese el genero M / F: ")
        f_alta=input("Ingrese la fecha de ingreso a la empresa, formato aaaa/mm/dd: ")
        sqlinsertar=" INSERT INTO `employees` (emp_no, birth_date,first_name, last_name,gender, hire_date) VALUES (%s,%s, %s, %s, %s, %s ) "
        datos=(nro_em,b_day,nombre,apellido,genero,f_alta)
        cursor.execute(sqlinsertar,datos)
        conn.commit()   # con commit se guardan los valores en la tabla
        sqlcon= " SELECT emp_no, first_name FROM `employees` WHERE  last_name=%s   "   #hago una consulta para ver si se agrego el valor que agregue en el insert
        cursor.execute(sqlcon,apellido)
        resul=cursor.fetchall()
        conn.close()
        for i in resul:
            print(i)
        
            
    def buscar_empleado():
        #conexion()
        import pymysql
        conn = pymysql.connect(
        host='127.0.0.1', user='root',
        passwd='', db='employees')
        cursor = conn.cursor()
        nro_em=int(input("Ingrese el nro de empleado que desea consultar: "))
        sql= "SELECT * FROM `employees` WHERE emp_no=%s " 
        cursor.execute(sql,nro_em)
        resultado=cursor.fetchall()
        conn.close()
        print(resultado)   #me muestra todos los resultados de mi consulta
        
        
    def modificar_empleado():
        #conexion()
        import pymysql
        conn = pymysql.connect(
        host='127.0.0.1', user='root',
        passwd='', db='employees')
        cursor = conn.cursor()
        nro_em=int(input("Ingrese el nro de empleado que desea modificar: "))
        gen=input("Ingrese el género actual: ")        
        sqlupd=" UPDATE `employees` SET gender=%s WHERE emp_no=%s "   #actualizo un dato del registro de empleado nro 10005
        d=(gen, nro_em)
        cursor.execute(sqlupd, d)
        conn.commit()
        sqlcons=" SELECT * FROM `employees` WHERE emp_no=%s"   # hago una consulta para verificar si se actualizo el registro
        cursor.execute(sqlcons,nro_em)
        resu=cursor.fetchone()
        conn.close()
        print(resu)
        
        
    def eliminar_empleado():
        #conexion()
        import pymysql
        conn = pymysql.connect(
        host='127.0.0.1', user='root',
        passwd='', db='employees')
        cursor = conn.cursor()
        nro_em=int(input("Ingrese el nro de empleado que desea eliminar: "))
        sqleli=" DELETE  FROM `employees` WHERE emp_no= %s"    #elimino de la BD el registro cuyo emp_no=5
        cursor.execute(sqleli, nro_em)
        conn.commit()
        cons_ver= "SELECT * FROM `employees` WHERE emp_no= %s"
        cursor.execute(cons_ver, nro_em)   #consulto la base para ver si aun está el registro que elimine en el query de arriba
        re=cursor.fetchone()
        conn.close()
        print(re)
            

e=Empleado
e.menu()

