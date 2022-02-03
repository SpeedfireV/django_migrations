
class Prostokat:
    def __init__(self, a, b, kolor):
        print(f'inicjalizuje klase prostokat z bokami a = {a} i b = {b}. Pole={a*b}')


class DziwnyProstokat(Prostokat):
    def __init__(self, **kwargs):

        print('kwargs przed', kwargs)
        kolor = kwargs.pop('kolor')
        print('kwargs po', kwargs)

        super().__init__(**kwargs)
        print(f"Inicjalizuję klasę DziwnyProstokat  x  x ")

#p = Prostokat(a=5, b=10)
k = DziwnyProstokat(a=5, b=10, kolor='czerwony')

'''def zrob_cos(text):
    print('otrzymany text=', text)
zrob_cos(text='qweqwe')'''

'''
colors_choices = [1,2,3]
k = Kwadrat()
'''

