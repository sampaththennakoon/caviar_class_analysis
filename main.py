import glob
import os
import numpy

train_data_set_path = 'train/labels'
test_data_set_path = 'test/labels'
validation_data_set_path = 'val/labels'

classes = dict()
classes[0] = 'walking'
classes[1] = 'immobile'
classes[2] = 'meeting'
classes[3] = 'browsing'
classes[4] = 'fighting'
classes[5] = 'drop down'
classes[6] = 'leaving'

# analyse train data set
def analyse_train_classes():
    classes_ = []
    files = glob.glob(os.path.join(train_data_set_path, '*.txt'))
    for file in files:
        with open(file) as file_:
            for line in file_:
                classes_.append(line.split(' ')[0])
    unique, counts = numpy.unique(classes_, return_counts=True)
    unique_count_map = dict(zip(unique, counts))
    for val, unique_count in unique_count_map.items():
        print(classes.get(int(val)), unique_count)

# analyse test data set
def analyse_test_classes():
    classes_ = []
    files = glob.glob(os.path.join(test_data_set_path, '*.txt'))
    for file in files:
        with open(file) as file_:
            for line in file_:
                classes_.append(line.split(' ')[0])
    unique, counts = numpy.unique(classes_, return_counts=True)
    unique_count_map = dict(zip(unique, counts))
    for val, unique_count in unique_count_map.items():
        print(classes.get(int(val)), unique_count)


# analyse validation data set
def analyse_validation_classes():
    classes_ = []
    files = glob.glob(os.path.join(validation_data_set_path, '*.txt'))
    for file in files:
        with open(file) as file_:
            for line in file_:
                classes_.append(line.split(' ')[0])
    unique, counts = numpy.unique(classes_, return_counts=True)
    unique_count_map = dict(zip(unique, counts))
    for val, unique_count in unique_count_map.items():
        print(classes.get(int(val)), unique_count)


if __name__ == '__main__':
    analyse_train_classes()
    print('--------------')
    analyse_test_classes()
    print('--------------')
    analyse_validation_classes()
