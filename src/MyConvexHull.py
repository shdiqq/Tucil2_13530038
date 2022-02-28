import math

#Fungsi untuk melakukan sorting
def sort_key(koordinat):
    return koordinat[0]

#Fungsi menghitung jarak tegak lurus antara titik dan garis
def jarak_tegaklurus(A,B,x,y) :
    x1, y1 = A
    x2, y2 = B
    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    d = (abs((a*x + b*y + c))) / (math.sqrt(a*a + b*b))
    return(d)

#Fungsi untuk menentukan dimana posisi suatu titik berada terhadap garis AB
def status_sebuah_titik(A,B,koordinasi):
    x1, y1 = A
    x2, y2 = B
    x, y = koordinasi
    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    f = a*x + b*y + c
    if f < 0:
        return 'kiri'
    elif f > 0:
        return 'kanan'
    else:
        return 'satu-garis'

def menemukan_banyak_titik_terluar(partisi,A,B,solusi_titik):
    if len(partisi) == 0:
        if ( ( A in solusi_titik) == False ) :
            solusi_titik.append(A)
        if ( ( B in solusi_titik) == False ) :
            solusi_titik.append(B)
        return
    else : #mencari titik yang berada paling luar ( panjang tegak lurus terbesar terhadap garis AB)
        jarak_terjauh = -1
        C = None
        for koordinasi in partisi:
            x, y = koordinasi
            f = jarak_tegaklurus(A,B,x,y)
            if f > jarak_terjauh:
                jarak_terjauh = f
                C = koordinasi
        x,y = C
        
        #Hapus titik C pada partisi
        partisi.remove(C)

        #Menyeleksi titik-titik yang tersedia untuk disimpan pada tempatnya
        ACkiri = []
        for koordinasi in partisi:
            koordinasi_side = status_sebuah_titik(A,C,koordinasi)
            if koordinasi_side == 'kiri':
                ACkiri.append(koordinasi)
        CBkiri = []
        for koordinasi in partisi:
            koordinasi_side = status_sebuah_titik(C,B,koordinasi)
            if koordinasi_side == 'kiri':
                CBkiri.append(koordinasi)
                
         
        #Penerapan Divide and Conquer
        menemukan_banyak_titik_terluar(ACkiri,A,C,solusi_titik)
        menemukan_banyak_titik_terluar(CBkiri,C,B,solusi_titik)

def convex_hull(bucket):
    # buat array solusi
    solusi_titik = []

    # Ubah type dri numarr ke list
    koordinat = bucket.tolist()
    
    #Lakukan pengurutan titik berdasarkan koordinat X dari mengecil ke membesar
    koordinat.sort(key=sort_key, reverse=False)

    #Ambil titik koordinat pada elemen array pertama dan terakhir untuk membentuk garis AB nantinya
    A = koordinat[0]
    B = koordinat[-1]

    #Inisiasi array untuk bagian kumpulan titik-titik yang berada bada sisi kiri AB atau kiri BA
    ABkiri = []
    BAkiri = []

    #Menyeleksi titik-titik yang tersedia untuk disimpan pada tempatnya
    for koordinasi in koordinat:
        koordinasi_side = status_sebuah_titik(A,B,koordinasi)
        if koordinasi_side == 'kiri':
            ABkiri.append(koordinasi)
        elif koordinasi_side == 'kanan':
            BAkiri.append(koordinasi)
        else:
            pass

    #Penerapan Divide and Conquer
    menemukan_banyak_titik_terluar(ABkiri,A,B,solusi_titik)
    menemukan_banyak_titik_terluar(BAkiri,B,A,solusi_titik)

    #return(solusi_garis)
    return(solusi_titik)