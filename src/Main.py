import pandas as pd 
import matplotlib.pyplot as plt
import MyConvexHull as MCH
from sklearn import datasets

while (True) :
    #Meminta input dari user terkait dataset yang akan diolah
    data = None
    print("Kumpulan dataset : ")
    print("1. Breast Cancer")
    print("2. Iris")
    print("3. Wine")
    correct_input_j  = False
    while ( correct_input_j == False ) :
        j = int(input("Silakan pilih dataset yang akan digunakan (0 Jika ingin keluar dari program) >> "))
        if ( (j < 0 or j > 3) == False ) :
            correct_input_j = True

    if ( j == 1 ) :
        data = datasets.load_breast_cancer()
    elif ( j == 2) :
        data = datasets.load_iris()
    elif ( j == 3 ) : 
        data = datasets.load_wine() 
    else :
        exit()

    length = len(data.feature_names)
    for i in range(length):
        print(i+1, '.', data.feature_names[i])

    x = None
    y = None
    correct_input_x = False
    correct_input_y = False

    while ( correct_input_x == False ) :
        x = int(input("Silakan pilih informasi atribut yang akan digunakan sebagai sumbu X (0 Jika ingin keluar dari program) >> "))
        if ( (x < 0 or x > length) == False ) :
            if ( x == 0 ) :
                exit()
            else :
                correct_input_x = True

    while ( correct_input_y == False ) :
        y = int(input("Silakan pilih informasi atribut yang akan digunakan sebagai sumbu Y (0 Jika ingin keluar dari program) >> "))
        if ( (y < 0 or y > length) == False ) :
            if ( y == x ) :
                correct_input_opsi = False
                while ( correct_input_opsi == False ) :
                    print("Atribut yang dipilih telah dipilih sebelumnya sebagai sumbu X, tetap ingin melanjutkan ? (Y/N)")
                    opsi = str(input(">> "))
                    if ( opsi == "Y" ) :
                        correct_input_y = True
                        correct_input_opsi = True
                    elif ( opsi == "N" ) :
                        correct_input_y = False
                        correct_input_opsi = True
                    else :
                        correct_input_opsi = False
            elif ( y == 0 ) :
                exit()
            else : 
                correct_input_y = True

    #create a DataFrame 
    df = pd.DataFrame(data.data, columns=data.feature_names) 
    df['Target'] = pd.DataFrame(data.target) 
    print("Berikut isi dari atribut informasi yang telah dipilih")
    print(df.iloc[0:, [x-1,y-1]])

    #visualisasi hasil ConvexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g','c','m','y','k']
    plt.title(f'{data.feature_names[x-1]} vs {data.feature_names[y-1]}')
    plt.xlabel(data.feature_names[x-1])
    plt.ylabel(data.feature_names[y-1])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[x-1,y-1]].values

        #gunakan library yg telah dibuat
        test1 = MCH.convex_hull(bucket)

        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], c = colors[i])

        # Mengolompokkan titik menjadi per titik pada sumbu x dan sumbu y
        x_values = [float(aw[0]) for aw in test1]
        y_values = [float(aw[1]) for aw in test1]
        x_values.append(test1[0][0])
        y_values.append(test1[0][1])

        # Membuat garis
        plt.plot(x_values, y_values, colors[i])

    plt.legend()
    plt.show()

    correct_input_quit = False
    while ( not correct_input_quit ) :
        print("Ingin tetap melanjutkan? (Y/N)")
        quit = str(input(">> "))
        if ( quit == 'N' ) :
            exit()
        elif ( quit == 'Y' ) :
            correct_input_quit = True
        else :
            correct_input_quit = False