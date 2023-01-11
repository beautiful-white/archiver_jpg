from os import system

def start():
    return input('> ').split()


def engine(mod):
    if not mod:
        mod = [
         'a']
    com = mod[0].lower()
    if com in ('encode', 'decode', 'help', 'cls', 'reset'):
        if com == 'help':
            helpq()
        elif com == 'cls':
            clss()
        elif com == 'encode':
            encode()
        elif com == 'decode':
            decode()
        elif com == 'reset':
            reset()
    else:
        print('[!] Неверная операция, введите help для помощи в использовании')


def encode():
    name_f, name_f2, password = input('Имя картинки: '), input('Имя объекта шифровки (вместе с расширением): '), list(bytes(input('Ключ доступа: '), 'utf-8'))
    name_f = name_f.rstrip('.jpg') + '.jpg'
    if password == []:
        return print('[!] Ключ доступа не может быть пустым')
    try:
        f = open(name_f, 'rb')
        f.close()
    except:
        print(f"[!] Ошибка имени картинки {name_f}")
        return 1
    else:
        try:
            f = open(name_f2, 'rb')
            f.close()
        except:
            print(f"[!] Ошибка имени объекта {name_f2}")
            return 1
        else:
            system('mkdir out')
            with open(name_f, 'rb') as f:
                with open(name_f2, 'rb') as f2:
                    with open('out/' + name_f, 'wb') as f3:
                        waste = list(bytes('{' + name_f2 + '}', 'utf-8') + f2.read())
                        cou = 0
                        for i in range(len(waste)):
                            if password[cou] % 2 == 0 or password[cou] % 3 == 0 or password[cou] % 7 == 0:
                                waste[i] = waste[i] + 1 if waste[i] + 1 <= 255 else 0;
                            cou += 1
                            if cou == len(password):
                                cou = 0

                        waste = f.read() + bytes(waste)
                        f3.write(waste)
            print(f"[!] Успешная операция\n    Архив {name_f} сохранён в папке out")


def decode():
    name_f, password = input('Имя картинки: '), list(bytes(input('Ключ доступа: '), 'utf-8'))
    name_f = name_f.rstrip('.jpg') + '.jpg'
    try:
        with open(name_f, 'rb') as f:
            pass
    except:
        print('[!] Ошибка имени файла:', name_f)
        return
    else:
        system('mkdir out')
        with open(name_f, 'rb') as f:
            data = f.read()
            data = list(data[data.index(bytes.fromhex('FFD9')) + 2:])
            cou = 0
            for i in range(len(data)):
                if password[cou] % 2 == 0 or password[cou] % 3 == 0 or password[cou] % 7 == 0:
                    data[i] = data[i] - 1 if data[i] - 1 >= 0 else 255
                cou += 1
                if cou == len(password):
                    cou = 0
            data = bytes(data)
            try:
                name = "".join(map(chr,list(data[1:data.index(b"}")])))
            except:
                return print("[!] Критическая ошибка разархивации, проверьте правильность кода доступа")
            with open("out/" + name, "wb") as f2:
                f2.write(data[data.index(b"}")+1:])
                print(f"[!] Успешная операция\n    Файл {name} из архива {name_f} распакован в папке out")


def reset():
    name_f, name_f2 = input('Имя картинки: '), input('Имя для новой картинки: ')
    name_f = name_f.rstrip('.jpg') + '.jpg'
    name_f2 = name_f2.rstrip('.jpg') + '.jpg'
    try:
        try:
            open(name_f2, 'rb')
            if input('Файл с таким именем уже существует. Хотите заменить его? (Enter с пустой строкой - если да): ').split():
                print('[!] Операция прервана...')
                return
        except:
            pass

    finally:
        pass

    try:
        try:
            with open(name_f, 'rb') as f:
                try:
                    with open(name_f2, 'wb') as f2:
                        temp = f.read()
                        f2.write(temp[:temp.index(bytes.fromhex('FFD9')) + 2])
                except:
                    print('[!] Ошибка имени файла: Недопустимые знаки в имени новой картинки')
                    return

            print('[!] Операция выполнена успешно:', name_f, '->', name_f2)
        except:
            print('[!] Ошибка имени файла:', name_f)

    finally:
        return None


def helpq():
    print('Список команд:')
    print('¤ decode - для разархивирования')
    print('¤ encode - для архивирования')
    print('¤ reset - для удаления архива из картинки')
    print('¤ cls - очистка экрана')


def stop():
    return input()


def clss():
    system('cls')


if __name__ == '__main__':
    print('[WARN] Это дополнительный модуль, он не будет работать самостоятельно.\n       Запустите главный исполнительный файл...')