import pandas as pd
from csv import DictReader


def file_parser():
    directory = '/home/lab/PycharmProjects/data_final/labeling-export-krystian/testing/bounding_boxes.txt'
    file = open(directory, 'r+')
    line = file.readline()

    data = pd.DataFrame(eval(line))
    data.to_csv('/home/lab/PycharmProjects/data_final/labeling-export-krystian/testing/bounding_boxes.csv')


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


def yolo_converter(list_of_data):
    image_width = 930
    image_height = 570
    factor = 2.0

    label = list_of_data[0]
    x = list_of_data[1]
    y = list_of_data[2]
    w = list_of_data[3]
    h = list_of_data[4]
    cx = x + (w / factor)
    cy = y + (h / factor)
    var1 = cx / image_width
    var2 = cy / image_height
    var3 = w / image_width
    var4 = h / image_height
    lbl = coordinate_classifier(label)

    # print(f'{lbl} {var1} {var2} {var3} {var4}')
    return "{} {} {} {} {}".format(lbl, var1, var2, var3, var4)


def csv_reader():
    with open('/home/lab/PycharmProjects/data_final/labeling-export-krystian/testing/bounding_boxes.csv', 'r') as read_object:
        csv_read = DictReader(read_object)
        for row in csv_read:
            if row['boundingBoxes']:
                data = row['boundingBoxes']
                data_eval = eval(data)
                if type(data_eval) == dict:
                    my_values = list(data_eval.values())
                    yolo_converter(my_values)
                    with open(f"/home/lab/PycharmProjects/data_final/labeling-export-krystian/testing/{row['frames']}.txt", "w") as txt_file:
                        txt_file.write(f'{yolo_converter(my_values)}')
                else:
                    my_data = list(data_eval)
                    with open(f"/home/lab/PycharmProjects/data_final/labeling-export-krystian/testing/{row['frames']}.txt", "w") as txt_file:
                        for dictionary in my_data:
                            sublist = list(dictionary.values())
                            yolo_converter(sublist)
                            txt_file.write(f'{yolo_converter(sublist)}\n')


file_parser()
csv_reader()
