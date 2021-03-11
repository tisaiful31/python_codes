import mariadb
import time
import os 
mydb = mariadb.connect(
        host = 'localhost',
        user = 'root',
        password = '123',
        database = 'accounts'
)

mycur = mydb.cursor()

def findallnum(name,user):
   search = f'select * from {user}'
   mycur.execute(search)
   search_result = mycur.fetchall()
   if len(search_result) == 0:
       return 'this contact name is not listed yet in your contact book'
   else:
       for i in range(0,len(search_result)):
           a,b,c,d = search_result[i]
           print(i+1)
           print('name:  ',a)
           print('number:  ',b)
           print('email:  ',c)
           print('relation:  ',d)


def findnum(name,user):
    try:
        search  = f'select * from {user} where name like "{name}%"'
        mycur.execute(search)

    except:

        return 0
    search_result = mycur.fetchall()
    if len(search_result) == 0:
        return 'this contact name is not listed yet in your contact book'
    else:
    
            for i in range(0, len(search_result)):
                a, b, c, d = search_result[i]
                print(i + 1)
                print('name:  ', a)
                print('number:  ', b)
                print('email:  ', c)
                print('relation:  ', d)
            print("update")
            opt_choose = input('choose number or go back to main manue type 0 : ')
            print("opt_choose ", opt_choose)
            if not opt_choose or not (opt_choose > 0 and opt_choose <9):
                print('opt_choosse')
                return 0
            if int(opt_choose) >= 1 and int(opt_choose) <= len(search_result):
                print('if')
                return search_result[int(opt_choose) - 1]
            elif int(opt_choose) == 0 and int(opt_choose) > len(search_result):
                print('elif')
                return 0



def options(user):
    global name,tmp
    tmp = ''
    try:
        create_table = f'create table {user} (name varchar(50),number int,email varchar(50),relation varchar(50),primary key(name))'
        mycur.execute(create_table)

    except:
        pass
    print('\n')
    print('1. save contacts ')
    print('2. find my contacts')
    print('3. update an existing contact')
    print('4. wanna delete any contact')
    print('5. log out')
    print('\n')

    option = input(f' hey {user} , choose any option : ')
    if option == '1':
            
        while True:
            name = input('type any name for your contact : ')
            if name:
                number = input('type your contact number : ')
                if number.isdigit():
                        email = input('type email for this contact :  ')
                        relation = input("what is the relation of your's : ")
                        tmp = 'True'
                        break
                else:
                    print('please type only digits')
                    time.sleep(1)
                    os.system('clear')
                    options(user)
                    break
 
            else:
                print('you should type a contact  name')
                time.sleep(1)
                os.system('clear')
                options(user)
                break
            
        if tmp == 'True':
            save = input('for saving this number type 1 or go back to main manue type 0 : ')
            if save == '1':
                try:
                     insert_data = f'insert into {user} (name,number,email,relation) values(%s,%s,%s,%s)'
                     values = name,number,email,relation
                     mycur.execute(insert_data,values)
                     mydb.commit()
                     time.sleep(1)
                     os.system('clear')
                     options(user)
                     tmp = 'False'
                        
                except:
                    print('this name already exists. name should be unique, please try with a different name ')
                    time.sleep(1)
                    os.system('clear')
                    options(user)
                    tmp = 'False'
            elif save == '0':
                time.sleep(1)
                os.system('clear')
                options(user)
                tmp = 'False'

            else:
                print('you should have type 1 or 0')
                time.sleep(1)
                os.system('clear')
                options(user)
                tmp = 'False'
                    

    elif option == '2':
        find = input('type your contact name or for all available numbers type all : ')

        if find != 'all' and find:
            find_result = findnum(find,user)
            if find_result == 'this contact name is not listed yet in your contact book':
                print(find_result)
                time.sleep(1)
                os.system('clear')
                options(user)
            elif find_result == 0:
                time.sleep(1)
                os.system('clear')
                options(user)
            else:
                a,b,c,d = find_result
                print('\n')
                print('----------------result-------------------')
                print('name:  ',a)
                print('number:  ',b)
                print('email:  ',c)
                print('relation:  ',d)
                print('----------------end----------------------')
                print('\n')
                time.sleep(1)
                options(user)

        elif find == 'all':
            print('----------------result-------------------')
            findallnum(find,user)
            print('----------------end----------------------')
            time.sleep(1)
            options(user)

        else:
            time.sleep(1)
            os.system('clear')
            options(user)
        

    elif option == '3':
        update = input('type your contact name: ')
        if update:
            update_result = findnum(update,user)
            if update_result == 'this contact name is not listed yet in your contact book':
                print(update_result)
                time.sleep(1)
                os.system('clear')
                options(user)
            elif update_result == 0:
                time.sleep(1)
                os.system('clear')
                options(user)

            else:
                a,b,c,d = update_result
                i_for_while = 1
                while i_for_while != 0:
                    print('which value you wanna update??? ')
                    print('1. name')
                    print('2. number')
                    print('3. email')
                    print('4. relation')
                    value_for_update = input('please type a number between 1 - 4 : ')
                    if value_for_update == '1' and i_for_while == 1:
                        updated_name = input('type your contact name: ')
                        if updated_name:
                            updated_name_query = f'update {user} set name="{updated_name}" where name="{a}"'
                            mycur.execute(updated_name_query)
                            mydb.commit()
                            print('Name update successfully')
                            again_edit = input('do you want to update again  ?? please type yes or no : ')
                            if again_edit == 'yes'.lower() or again_edit == 'yes'.upper() or again_edit == 'y'.lower()  or again_edit == 'y'.upper():
                                i_for_while = 1
                                
                            else:
                                time.sleep(1)
                                os.system('clear')
                                options(user)
                                i_for_while = 0
                        else:
                            print("you didn't type any name . that's why your were sent back to main manue")
                            time.sleep(1)
                            os.system('clear')
                            options(user)
                            break

                    elif value_for_update == '2' and i_for_while == 1:
                        updated_number = input('type your contact number: ')
                        if updated_number.isdigit():
                            updated_number_query = f'update {user} set number={updated_number} where name="{a}" '
                            mycur.execute(updated_number_query)
                            mydb.commit()
                            print('Number update successfully')
                            again_edit = input('do you want to update again  ?? please type yes or no ')
                            if again_edit == 'yes'.lower() or again_edit == 'yes'.upper() or again_edit == 'y'.lower()  or again_edit == 'y'.upper():                               
                                i_for_while = 1
                                    

                            else:
                                time.sleep(1)
                                os.system('clear')
                                options(user)
                                i_for_while = 0

                        else:
                            print('you should type only digits')
                            time.sleep(1)
                            os.system('clear')
                            options(user)
                            break

                    elif value_for_update == '3' and i_for_while == 1:
                        updated_email = input('type your contact email: ')
                        if updated_email:
                            updated_email_query = f'update {user} set email="{updated_email}" where name="{a}" '
                            mycur.execute(updated_email_query)
                            mydb.commit()
                            print('email update successfully')
                            again_edit = input('do you want to update again  ?? please type yes or no ')
                            if again_edit == 'yes'.lower() or again_edit == 'yes'.upper() or again_edit == 'y'.lower()  or again_edit == 'y'.upper():
                                i_for_while = 1
                            else:
                                time.sleep(1)
                                os.system('clear')
                                options(user)
                                i_for_while = 0


                        else:
                            time.sleep(1)
                            os.system('clear')
                            options(user)
                            break
                    elif value_for_update == '4' and i_for_while == 1:
                        updated_relation = input('type your contact relation: ')
                        if updated_relation:
                            updated_relation_query = f'update {user} set relation="{updated_relation}" where name="{a}"'
                            mycur.execute(updated_relation_query)
                            mydb.commit()
                            print('Relation update successfully')
                            again_edit = input('do you want to update again  ?? please type yes or no ')
                            if again_edit != 'yes'.lower() or again_edit != 'yes'.upper() or again_edit != 'y'.lower()  or again_edit != 'y'.upper():
                                i_for_while = 1
                            else:
                                time.sleep(1)
                                os.system('clear')
                                options(user)
                                i_for_while = 0
                        else:
                            time.sleep(1)
                            os.system('clear')
                            options(user)
                            break

                    else:
                        time.sleep(1)
                        os.system('clear')
                        options(user)
                        break
                else:
                    time.sleep(1)
                    os.system('clear')
                    options(user)
                 


    elif option == '4':
        delete = input('type your contact name: ')
        if delete:
            delete_result = findnum(delete,user)
            print(delete_result)
            if delete_result == 'this contact name is not listed yet in your contact book':
                time.sleep(1)
                os.system('clear')
                options(user)
            else:
                a,b,c,d = delete_result
                input_for_confirmation = input('please type confirm to delete this number: ')
                if input_for_confirmation == 'confirm'.lower() or  input_for_confirmation == 'confirm'.upper() or  input_for_confirmation == 'c'.lower()  or  input_for_confirmation == 'c'.upper():
                    updated_delete_query = f'delete from {user} where name="{a}"'
                    mycur.execute(updated_delete_query)
                    mydb.commit()
                    print('Successfully deleted')
                    time.sleep(1)
                    options(user)
                else:
                    time.sleep(1)
                    os.system('clear')
                    options(user)

        else:
            time.sleep(1)
            os.system('clear')
            options(user)

    elif option == '5':
        print('bye, welcome anytime')
            
    else:
        if option:
            print('please choose number between 1-4 ')
            time.sleep(1)
            os.system('clear')
            options(user)
        else:
            print('bye')
                
while True:
    print('\n')
    print("------------------------------------WELCOME TO CONTACT BOOK-------------------------------------------------------")
    print("you can save your number's or find your number's by having an account . so, please create an account. ")
    print('\n')
    useraccount = input('do you have any account  ??? yes or no or press any key for leave ? ')

    if useraccount == 'yes'.lower() or useraccount == 'yes'.upper() or useraccount == 'y'.lower()  or useraccount == 'y'.upper():
        try:
            username = input('type your name: ')
            password = input('type your password: ')
            check = mycur.execute(f"select username,password from users where username='{username}' ")
            result = mycur.fetchone()
            a,b = result
            if a == username and b == password:
                time.sleep(1)
                options(username)
                break
        except:
                print('wrong username or password')


    elif useraccount == 'no'.lower() or useraccount == 'no'.upper() or useraccount == 'n'.lower()  or useraccount == 'n'.upper():
        createaccount = input('do you want to create any account  ??? yes or no ? ')
        if createaccount == 'yes'.lower() or createaccount == 'yes'.upper() or createaccount == 'y'.lower() or createaccount == 'y'.upper():
            username = input('type your name: ')
            password = input('type your password : ')
            try:
                sql = 'insert into users (username,password) values (%s,%s)'
                values = username,password
                mycur.execute(sql,values)
                time.sleep(1)
                options(username)
            except:
                print('this account already exists')
                time.sleep(1)
                options(username)
                break
        else:
            print('bye')
            break
            

    else:
        print('bye')
        break

name = ''
tmp = ''
