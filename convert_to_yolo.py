import pandas as pd
from csv import reader, DictReader


def file_parser():
    directory = '/home/lab/PycharmProjects/data/data.txt'
    file = open(directory, 'r+')
    line = file.readline()

    data = pd.DataFrame(eval(line))
    # data.to_json('/home/lab/PycharmProjects/data/json_data.json')
    data.to_csv('/home/lab/PycharmProjects/data/csv_data.csv')


def coordinate_classifier(label):
    value = 0
    if label == 'person':
        value = 0
    elif label == 'car':
        value = 1
    elif label == 'tram':
        value = 2
    elif label == 'airplane':
        value = 3
    return value


def csv_reader():
    image_width = 930
    image_height = 570
    object_classificator = {'person': 0, 'car': 1, 'tram': 2, 'airplane': 3}

    with open('/home/lab/PycharmProjects/data/csv_data.csv', 'r') as read_object:
        csv_read = DictReader(read_object)
        for row in csv_read:
            if row['boundingBoxes']:
                data = row['boundingBoxes']
                data_eval = eval(data)
                # print(type(data_eval))
                if type(data_eval) == dict:
                    # print('DICT')
                    my_values = list(data_eval.values())
                    print(my_values)
                    label = my_values[0]
                    x = my_values[1]
                    y = my_values[2]
                    w = my_values[3]
                    h = my_values[4]
                    cx = x + (w / 2.0)
                    cy = y + (h / 2.0)
                    var1 = cx / image_width
                    var2 = cy / image_height
                    var3 = w / image_width
                    var4 = h / image_height

                    lbl = coordinate_classifier(label)

                    print(f'YOLO coordinates: {lbl} {var1} {var2} {var3} {var4}')
                else:
                    # print('TUPLE')
                    """TODO: """
                    pass


# file_parser()
csv_reader()


"""
    Procedura: 
    1. Zmiana zawartości pliku na obiekt DataFrame.
    2. Zapisanie zawartości zmiennej DataFrame do pliku CSV.
    3. W pliku CSV usunąć niepotrzebne kolumny.
    4. W pliku CSV za pomocą narzędzia znajdź usunąć przedni oraz tylny nawias kwadratowy 
       z kolumny boundingBoxes (bo jest szybciej).
    5. Potraktować kolumnę boundingBoxes funkcją eval(), żeby otrzymać słownik lub tuplę.
    6. Przeszukać słowniki w celu wyekstraktowania danych.
"""