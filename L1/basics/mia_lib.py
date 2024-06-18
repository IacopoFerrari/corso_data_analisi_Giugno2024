#esempio di modulo di libreria
diz = {
       'Ferrari': [[47, 98, -32, -73], [-55, 90, -80, 39], [-86, -66, 56, -8], [84, -62, -53, -3], [20, -36, 78, 86], [28, 63, -9, -34], [25, -79, -42, -57], [80, 47, 28, -11], [-17, 56, -57, 4], [-3, -65, 6, 15], [48, -47, -20, -14], [36, -67, -49, 78], [34, -23, -87, 66], [-59, -56, 36, -10], [-21, -88, 71, 15]],
       'stud1': [[74, -9, 23, 93], [-17, -95, 14, 32], [49, -19, -32, -76], [87, 35, 11, -55], [72, -72, -21, -62], [-28, 13, -71, 9], [76, 21, -1, 17], [-45, 93, 55, 12], [62, -82, -29, 94], [96, -83, 64, -39], [59, 92, 100, -3], [-63, -27, -15, 80], [85, -90, 27, -99], [-4, 86, 89, 91], [30, 97, 80, -33]], 
       'stud2': [[35, -35, -11, 61, -34, 19], [81, -66, 21, -83, 94, -16], [26, -94, -52, -96, -5, -48], [-36, 92, 83, 73, 9, -10], [-57, 79, -17, -81, 71, -5], [-97, 74, -67, -36, 4, 34], [-56, -77, 62, 4, -26, 83], [21, 33, 75, -53, -11, 60], [-9, -38, 84, -74, -37, -80], [80, 42, -61, -28, -53, -42], [35, -9, 67, -84, -87, 25], [35, 99, 49, 83, -50, -58], [57, -86, 73, -73, -27, 6], [15, -91, 18, 87, 11, 86], [-60, 41, 92, -27, -45, -40], [-39, -74, -59, -43, -53, 57], [44, -24, 50, 88, -59, 43], [73, 80, 0, 34, 43, -10]], 
       'stud3': [[-17, -18, 76, -33, 34, -95], [53, 6, 28, 82, 13, 84], [38, -19, -23, 78, -44, 95], [65, -13, 9, -45, 15, -45], [45, -72, 52, -93, -29, 49], [-34, 91, -4, 16, -54, 36], [-45, -78, -82, -76, -82, -93], [-74, -53, -60, 39, 93, 47], [93, -92, 88, 45, 80, 53], [-23, -14, 88, 41, 30, 79], [-41, -55, 52, -27, -2, -76], [-31, 68, 16, -13, -30, -44], [-89, -73, -17, 1, -66, -99], [-68, 35, 31, 57, 46, 15], [-83, 5, 37, 40, -61, -44]], 
       'stud4': [[32, -77, -66, 60, 93, 79], [-70, -11, -30, -75, 27, -100], [65, 64, 75, 68, 86, -61], [-55, -74, -49, -15, -42, -34], [-94, 56, -5, 34, 83, -66], [40, -97, 82, 72, 51, 48], [1, -85, 19, 88, -4, 15], [35, 71, 33, 75, 2, 98], [64, 61, -90, -70, -91, -79], [-15, -45, -89, 9, 75, -94], [65, 49, 69, -29, -78, -8], [81, 27, 98, 70, 37, 91], [12, -71, 2, -74, -4, 85], [53, 67, -30, -49, -81, 29], [81, -11, -26, -51, 66, 66], [-32, 47, -67, 18, 17, 63], [-55, 93, -43, -43, 6, -88], [58, 28, 16, 41, -32, -88], [-89, -88, 29, 54, -75, -85], [15, 99, -89, -56, 85, -69]], 
       'stud5': [[80, 99, 2, 5, 10, 52], [35, -100, 8, -33, -73, -37], [-94, -72, 47, -17, -79, -37], [14, -87, -1, 60, -24, -12], [57, 23, 48, -100, 36, 87], [-87, -65, -4, -88, -14, -32], [-85, 60, -7, -45, 38, -60], [-76, -81, -85, -6, -40, 26], [19, -28, -86, -68, -39, 99], [14, -96, 18, 5, 27, -28], [-48, 96, -11, -25, -67, -36], [-66, 81, -11, 61, 57, 25], [-48, -38, 10, -38, 15, -82], [31, 79, -63, -41, 85, 52], [2, -96, 3, 63, -93, -9], [86, 79, 9, -7, -27, 93], [-76, 31, -59, 24, 97, -73], [21, 3, -23, 1, 65, 54], [61, 1, 30, -95, -41, 89]], 
        }


def dimmi_i_miei_dati(nome_cognome):
    return diz[nome_cognome]

if __name__ == "__main__":
    print("eseguo il codice nel MAIN di mia lib")
    a = dimmi_i_miei_dati("Ferrari")
    print(a)