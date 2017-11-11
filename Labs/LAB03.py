import numpy as np
import pandas as pd
from sklearn.cluster import KMeans  # http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
import pprint as pp                 # I'm using just to print whit a better aspect

data_path = r"csv/iris.csv"
data = pd.read_csv(data_path)

# print(data.get_values()[0][4])

my_data = np.genfromtxt('csv/iris.csv', delimiter=',',skip_header=1) # using the numpy to read the csv like a array


my_data = np.delete(my_data,4,1) #  It's be careful, too not use directly non-numeral data


kmeans = KMeans(n_clusters=3, random_state=0, max_iter=1000000,n_jobs=100).fit(my_data)

pp.pprint(kmeans.cluster_centers_)

pp.pprint(kmeans.algorithm)

for i in range(len(my_data)):
    print("Sample number :","%3i"%(i)," |Cluster: ",kmeans.labels_[i]," |Class: %15s"%(data.get_values()[i][4]), " |Data :",my_data[i])


# data_size = len(my_data)
# data_type = [0,0]
#
# for i in range(len(my_data)):
#     if kmeans.labels_[i] == 0:
#         data_type[0] += 1
#     if kmeans.labels_[i] == 1:
#         data_type[1] += 1
#
