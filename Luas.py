class KelilingLingkaran(object):
    def __init__(self, r):
        self.jarijari = r
    def hitungKeliling(self):
        return 2 * 3.14 * self.jarijari
        
        
class LuasLingkaran(object):
    def __init__(self, r):
        self.jarijari = r 
    def hitungLuas(self):
        return 3.14 * (self.jarijari * self.jarijari)

        
def main() :
    #lingkaran pertama
    Lingkaran11 = KelilingLingkaran(4)
    Lingkaran12 = LuasLingkaran(4)
    
    print('LINGKARAN 1')
    
    print('-KELILING')
    print('phi\t   : 3,14')
    print('jarijari\t: ',Lingkaran11.jarijari)
    print('Kelilingnya\t= ', Lingkaran11.hitungKeliling())
    
    print('LUAS') 
    print('phi\t : 3.14')
    print('jarijari\t: ', Lingkaran12.jarijari)
    print('Luasnya\t   = ', Lingkaran12.hitungLuas())
    
    print(' ')
    
    #lingkaran kedua 
    Lingkaran21 = KelilingLingkaran(8)
    Lingkaran22 = LuasLingkaran(8)
    
    
    print('LINGKARAN 2')
    
    print('-KELILING')
    print('phi\t  :3.14')
    print('jarijari\t: ', Lingkaran21.jarijari)
    print('Kelilingnya\t  = ',Lingkaran21.hitungKeliling())

    print('-LUAS ')
    print('phi\t  : 3.14')
    print('jarijari\t: ',Lingkaran22.jarijari)
    print('Luasnya\t  = ',Lingkaran22.hitungLuas())
    
    
if __name__ == "__main__":
        main()
    
    
    
    
 