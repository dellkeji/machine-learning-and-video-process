# -*- coding:utf-8 -*-

import operator
from numpy import *

class KNNClassify(object):
    """knn classify
    """

    def __init__(self):
        pass

    def file_to_matrix(self, file_name):
        fd = open(file_name)
        data = fd.readlines()
        number_of_lines = len(data)
        # 初始化矩阵
        init_mat = zeros((number_of_lines, 3))
        class_label = []
        index = 0
        for line in data:
            line = line.strpe()
            split_list = line.split('\t')
            init_mat[index, :] = split_list[0:3]
            class_label.append(int(split_list[-1]))
            index += 1
        return init_mat, class_label

    def normal_data(self, data_set):
        # get min or max for every colume
        min_val = data_set.min(0)
        max_val = data_set.max(0)
        # get range
        range_val = max_val - min_val
        # init the matrix
        normal_data_set = zeros(shape(data_set))
        row_number = shape(data_set)[0]
        normal_data_set = data_set - title(min_val, (row_number, 1))
        normal_data_set = normal_data_set/title(range_val, (row_number, 1))
        return normal_data_set, range_val, min_val

    def classify(self, vec, data_set, labels, k):
        """
        calculate the distance
        @params vec:vector
        @params data_set: data set
        @params lables: lables
        @params k: number of optimal
        """
        data_set_size = data_set.shape[0]
        diff_mat = tile(vec, (data_set_size, 1)) - data_set
        # 平方
        square_diff_mat = diff_mat**2
        # 距离
        # matrix add for every line
        square_distance = square_diff_mat.sum(axis=1)
        distances = square_distance**0.5
        # 排序
        # return the index of number 
        sorted_distances = distances.argsort()
        # labels选取
        class_count = {}
        for i in range(k):
            vote_label = labels[sorted_distances[i]]
            class_count[vote_label] = class_count.get(vote_label, 0) + 1
        sorted_class_count = sorted(class_count.iteritems(),
            key = operator.itemgetter(1), reverse=True)
        # 返回
        return sorted_class_count[0][0]

    def test_knn_by_demo(self):
        test_ratio = 0.50
        data_set, labels = self.file_to_matrix('datingTestSet2.txt')
        norm_mat, ranges, min_val = self.normal_data(data_set)
        m = norm_mat.shape[0]
        num_test = int(m*test_ratio)
        error_count = 0.0
        for i in range(num_test):
            classify_result = self.classify((norm_mat[i,:],norm_mat[num_test:m,:],labels[numTestVecs:m],3))
            print "the classifier came back with: %d, the real answer is: %d" % (classify_result, labels[i])

            if (classifierResult != datingLabels[i]): 
                errorCount += 1.0
            print "the total error rate is: %f" % (errorCount/float(numTestVecs))
            print error_count



if __name__ == "__main__":
    knn_obj = KNNClassify()
    group = array([
        [1, 1.1],
        [1, 1],
        [0, 0],
        [0, 0.1]
    ])
    labels = ["A", "A", "B", "B"]
    print knn_obj.classify([0,0], group, labels, 3)

