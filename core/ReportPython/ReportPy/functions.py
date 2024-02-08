from variables import *

#-----------------------------------------------------#

def len_control():
    print(
        'data1:',len(data1),
        'data2:',len(data2),
        'data3:',len(data3),
        'data4:',len(data4),
        'data5:',len(data5),
        'data6:',len(data6),
        'data7:',len(data7),
        'data8:',len(data8),
        'data9:',len(data9),
        'data10:',len(data10),
        'data12:',len(data12),
        'data13:',len(data13),
        'data14:',len(data14),
        'data15:',len(data15),
        'data16:',len(data16),
        'data17:',len(data17),
        'data18:',len(data18),
        'data19:',len(data19),
        'data20:',len(data20),
        'data21:',len(data21),
        'data22:',len(data22),
        'data23:',len(data23),
        'data24:',len(data24),
    )    

def clear_list():
    del data1[:]
    del data2[:]
    del data3[:]
    del data4[:]
    del data5[:]
    del data6[:]
    del data7[:]
    del data8[:]
    del data9[:]
    del data10[:]
    del data11[:]
    del data12[:]
    del data13[:]
    del data14[:]
    del data15[:]
    del data16[:]
    del data17[:]
    del data18[:]
    del data19[:]
    del data20[:]
    del data21[:]
    del data22[:]
    del data23[:]
    del data24[:]

#-----------------------------------------------------#

def iter_generic(row, cont):
    for i in row:
        cont += 1
        try:
            if cont == 1:
                data1.append(i)
            elif cont == 2:
                data2.append(i)
            elif cont == 3:
                data3.append(i)
            elif cont == 4:
                data4.append(i)
            elif cont == 5:
                data5.append(i)
            elif cont == 6:
                data6.append(i)
            elif cont == 7:
                data7.append(i)
            elif cont == 8:
                data8.append(i)
            elif cont == 9:
                data9.append(i)
            elif cont == 10:
                data10.append(i)
            elif cont == 11:
                data11.append(i)
            elif cont == 12:
                data12.append(i)
            elif cont == 13:
                data13.append(i)
            elif cont == 14:
                data14.append(i)
            elif cont == 15:
                data15.append(i)
            elif cont == 16:
                data16.append(i)
            elif cont == 17:
                data17.append(i)
            elif cont == 18:
                data18.append(i)
            elif cont == 19:
                data19.append(i)
            elif cont == 20:
                data20.append(i)      
            elif cont == 21:
                desc = row[5]
                precio = row[8]
                a = row[1]
                descG = float(precio) * float(desc) / 100
                data21.append(descG)    
            elif cont == 22:
                descl = row[6]
                precioL = row[8]
                descL = float(precioL) * float(descl) / 100
                data22.append(descL)    
            elif cont == 23:
                data23.append(i)
            elif cont == 24:
                data24.append(i)
        except:
            print('Ocurrio un error')                


def iter_tarj(row, cont):
    for i in row:
        cont += 1
        try:
            if cont == 1:
                data1.append(i)
            elif cont == 2:
                data2.append(i)
            elif cont == 3:
                data3.append(i)
            elif cont == 4:
                data4.append(i)
            elif cont == 5:
                data5.append(i)
            elif cont == 6:
                data6.append(i)
            elif cont == 7:
                data7.append(i)
            elif cont == 8:
                data8.append(i)
            elif cont == 9:
                data9.append(i)
            elif cont == 10:
                data10.append(i)
            elif cont == 11:
                data11.append(i)
            elif cont == 12:
                data12.append(i)
            elif cont == 13:
                data13.append(i)
            elif cont == 14:
                data14.append(i)
            elif cont == 15:
                data15.append(i)
            elif cont == 16:
                data16.append(i)
        except:
            print('Ocurrio un error')                


def iter_pres(row, cont):
    for i in row:
        cont += 1
        try:
            if cont == 1:
                data1.append(i)
            elif cont == 2:
                data2.append(i)
            elif cont == 3:
                data3.append(i)
            elif cont == 4:
                data4.append(i)
            elif cont == 5:
                data5.append(i)
            elif cont == 6:
                data6.append(i)
            elif cont == 7:
                data7.append(i)
 
        except:
            print('Ocurrio un error')                


def iter_tarj_cierre(row, cont):
    for i in row:
        cont += 1
        try:
            if cont == 1:
                data1.append(i)
            elif cont == 2:
                data2.append(i)
            elif cont == 3:
                data3.append(i)
            elif cont == 4:
                data4.append(i)
            elif cont == 5:
                data5.append(i)
            elif cont == 6:
                data6.append(i)
            elif cont == 7:
                data7.append(i)
            elif cont == 8:
                data8.append(i)
            elif cont == 9:
                data9.append(i)
            elif cont == 10:
                data10.append(i)
            elif cont == 11:
                data11.append(i)
            elif cont == 12:
                data12.append(i)
            elif cont == 13:
                data13.append(i)
            elif cont == 14:
                data14.append(i)

        except:
            print('Ocurrio un error')                


def iter_promo(row, cont):
    for i in row:
        cont += 1
        try:
            if cont == 1:
                data1.append(i)
            elif cont == 2:
                data2.append(i)
            elif cont == 3:
                data3.append(i)
            elif cont == 4:
                data4.append(i)
            elif cont == 5:
                data5.append(i)
            elif cont == 6:
                data6.append(i)
            elif cont == 7:
                data7.append(i)
            elif cont == 8:
                data8.append(i)
            elif cont == 9:
                data9.append(i)
            elif cont == 10:
                data10.append(i)
            elif cont == 11:
                data11.append(i)
            elif cont == 12:
                data12.append(i)
            elif cont == 13:
                data13.append(i)
        except:
            print('Ocurrio un error')                


#-----------------------------------------------------#



def iter_ciber(row, cont):
    for i in row:
        cont += 1
        try:
            if cont == 1:
                data1.append(i)
            elif cont == 2:
                data2.append(i)
            elif cont == 3:
                data3.append(i)
            elif cont == 4:
                data4.append(i)
            elif cont == 5:
                data5.append(i)
            elif cont == 6:
                data6.append(i)
            elif cont == 7:
                data7.append(i)
            elif cont == 8:
                data8.append(i)
            elif cont == 9:
                data9.append(i)
            elif cont == 10:
                data10.append(i)
            elif cont == 11:
                data11.append(i)
            elif cont == 12:
                data12.append(i)
            elif cont == 13:
                data13.append(i)
        except:
            print('Ocurrio un error')                

def iter_cumple(row, cont):
    for i in row:
        cont += 1
        try:
            if cont == 1:
                data1.append(i)
            elif cont == 2:
                data2.append(i)
            elif cont == 3:
                data3.append(i)
            elif cont == 4:
                data4.append(i)
            elif cont == 5:
                data5.append(i)
            elif cont == 6:
                data6.append(i)
            elif cont == 7:
                data7.append(i)
            elif cont == 8:
                data8.append(i)
            elif cont == 9:
                data9.append(i)
            elif cont == 10:
                data10.append(i)
            elif cont == 11:
                data11.append(i)
            elif cont == 12:
                data12.append(i)
            elif cont == 13:
                data13.append(i)
            elif cont == 14:
                data14.append(i)
            elif cont == 15:
                data15.append(i)
            elif cont == 16:
                data16.append(i)
            elif cont == 17:
                data17.append(i)
            elif cont == 18:
                data18.append(i)
            elif cont == 19:
                fechaN = datetime.strptime(i, "%d-%m")
                fechaC = fechaN.strftime("%d-%m")
                data19.append(fechaC)
            elif cont == 20:
                data20.append(i)    
            elif cont == 21:
                desc = row[5]
                precio = row[8]
                a = row[1]
                descG = float(precio) * float(desc) / 100
                data21.append(descG)    
            elif cont == 22:
                descl = row[6]
                precioL = row[8]
                descL = float(precioL) * float(descl) / 100
                data22.append(descL)    
            elif cont == 23:
                data23.append(i)
            elif cont == 24:
                data24.append(i)
        except:
            print('Ocurrio un error')   

