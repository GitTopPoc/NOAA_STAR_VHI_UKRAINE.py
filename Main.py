
from __future__ import print_function
from numpy import genfromtxt

from urllib.request import urlopen
import glob, os

from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, show, legend
from datetime import date

list_province = [[1, 'Вінницька'],
                 [2, 'Волинська'],
                 [3, 'Дніпропетровська'],
                 [4, 'Донецька'],
                 [5, 'Житомирська'],
                 [6, 'Закарпатська'],
                 [7, 'Запорізька'],
                 [8, 'Івано-франківська'],
                 [9, 'Київська'],
                 [10, 'Кіровоградська'],
                 [11, 'Луганська'],
                 [12, 'Львівська'],
                 [13, 'Миколаївська'],
                 [14, 'Одеська'],
                 [15, 'Полтавська'],
                 [16, 'Рівненська'],
                 [17, 'Сумська'],
                 [18, 'Тернопільска'],
                 [19, 'Харківська'],
                 [20, 'Херсонська'],
                 [21, 'Хмельницька'],
                 [22, 'Черкаська'],
                 [23, 'Чернівецька'],
                 [24, 'Чернігівська'],
                 [25, 'Крим']]


def files_in_directory():
    try:
        os.chdir("vhi")
        print("- vhi")
        for file in glob.glob("*.csv"):
            print(file)
    except:
        os.chdir("../vhi")
        print("- vhi")
        for file in glob.glob("*.csv"):
            print(file)
   

def fix_file_vhi(s_file):
    fi = open(s_file)
    line = fi.readlines()
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(line[0],
                                 '')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi.close()
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(',', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace('  ', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace('  ', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi = open(s_file)
    line = fi.readlines()
    x = len(line)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(line[x - 1], '')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi.close()


def parser_file(province_id):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&" \
          + "provinceID=" + str(province_id) \
          + "&year1=1981&year2=2021&type=Mean"
    vhi_url = urlopen(url)

    try:
        out = open('../vhi/vhi_id_' + str(choosed_province) + '_' + str(date.today()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        try:
            s_file = '../vhi/vhi_id_' + str(choosed_province) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)
        except:
            s_file = 'vhi/vhi_id_' + str(choosed_province) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)
    except:
        out = open('vhi/vhi_id_' + str(choosed_province) + '_' + str(date.today()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        try:
            s_file = 'vhi/vhi_id_' + str(choosed_province) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)
        except:
            s_file = '../vhi/vhi_id_' + str(choosed_province) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)

    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&" \
          + "provinceID=" + str(province_id) \
          + "&year1=1981&year2=2021&type=VHI_Parea"
    vhi_url = urlopen(url)

    
def Average(lst): 
    return sum(lst) / len(lst) 
  

def analyzing_by_year(year, csv_v):
    list_week = []
    list_vhi = []

    c = 0
    for anbyyear in csv_v:
        if (csv_v[c][0] == year):
            list_week.append(csv_v[c][1])
            list_vhi.append(csv_v[c][6])
        c += 1

    figure()
    plot(list_week, list_vhi, 'r')
    xlabel('week')
    ylabel('vhi')
    title('Графік VHI за ' + str(year) + ' [min:' + str(min(list_vhi)) + ' and max:' + str(max(list_vhi)) + ']' + str(Average(list_vhi)))
    show()


def analyzing_by_years():
    list_weeks = []
    list_years = []
    list_avg = []
    c=0
    for chk in csv_v:
        if(csv_v[c][1] !=52):
            list_weeks.append(csv_v[c][6])
           
        elif csv_v[c][1] == 52:
            list_avg.append(Average(list_weeks))
            list_weeks = []
            list_years.append(csv_v[c][0])
    
        c +=1
     
    
    figure()
    plot(list_years, list_avg, 'r')
    xlabel('week')
    ylabel('vhi')
    title('Середнє значення VHI за всі роки')
    show()

def choose_default_vhi(province_id, date_in):
    try:
        csv_v = genfromtxt('vhi/vhi_id_' + str(province_id) + '_' + str(date_in) + '.csv', delimiter=' ')
    except:
        csv_v = genfromtxt('../vhi/vhi_id_' + str(province_id) + '_' + str(date_in) + '.csv', delimiter=' ')
    return csv_v



def clear_console():
    try:
        os.system('clear')
    except:
        os.system('cls')


def print_menu():
    print(30 * "-", "МЕНЮ", 30 * "-")
    print("1. Парс даних")
    print("2. Змінити файл")
    print("3. Графік за 1 рік")
    print("4. Графік за всі роки")
    print("0. Вихід")
    print(70 * "-")




if __name__ == '__main__':
    csv_v = choose_default_vhi("22", "2021-02-25")
    

    loop = True

    while loop:
        print_menu()
        choose = int(input("Вибір : "))

        if choose == 1:
            print(*list_province, sep='\n')
            province_id = int(input("Введіть ID області: "))
            choosed_province = province_id
            if province_id == 1:
                province_id = 24
            elif province_id == 2:
                province_id = 25
            elif province_id == 3:
                province_id = 5
            elif province_id == 4:
                province_id = 6
            elif province_id == 5:
               province_id = 27
            elif province_id == 6:
               province_id = 23
            elif province_id == 7:
                province_id = 26
            elif province_id == 8:
                province_id = 7
            elif province_id == 9:
                province_id = 12
            elif province_id == 10:
                province_id = 13
            elif province_id == 11:
                province_id = 14
            elif province_id == 12:
                province_id = 15
            elif province_id == 13:
                province_id = 16
            elif province_id == 14:
                province_id = 17
            elif province_id == 15:
                province_id = 18
            elif province_id == 16:
                province_id = 19
            elif province_id == 17:
                province_id = 21
            elif province_id == 18:
                province_id = 22
            elif province_id == 19:
                province_id = 8
            elif province_id == 20:
                province_id = 9
            elif province_id == 21:
                province_id = 10
            elif province_id == 22:
                province_id = 1
            elif province_id == 23:
                province_id = 3
            elif province_id == 24:
               province_id = 2
            elif province_id == 25:
                province_id = 4
            elif province_id == 26:
                province_id = 26
            elif province_id == 27:
                province_id = 27
                  
            parser_file(province_id)
            files_in_directory()
            province_id = int(input("Введіть ID: "))
            date_in = input("Введіть дату (yyyy-mm-dd): ")
            csv_v = choose_default_vhi(province_id, date_in)
        elif choose == 2:
            files_in_directory()
            province_id = int(input("Введіть ID: "))
            date_in = input("Введіть дату (yyyy-mm-dd): ")
            csv_v = choose_default_vhi(province_id, date_in)
        elif choose == 3:
            year = int(input("Введіть рік: "))
            analyzing_by_year(year, csv_v)
        elif choose == 4:
            analyzing_by_years()
        elif choose == 0:
            loop = False
