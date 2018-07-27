import pandas as pd ;

columns = ["sepal_length","sepal_width","petal_length","petal_width","class"] ;
iris_df = pd.read_csv("data.csv", names = columns) ;
print(iris_df.head(),iris_df.tail()) ;
