from sklearn import tree

sudah = 1
belum = 0

ciri = [[120, 1],[150, 1],[200, 0],[250, 0]]
label = [0, 0, 1, 1]
mesin = tree.DecisionTreeClassifier()
mesin = mesin.fit(ciri, label)

print('Klasifikasi Syarat Pacaran Anak Papah Mamah')
a = input('Berapa Umur Saat ini ? (umur 0-16 pilih "0 atau 1"): ')
b = input('\nApakah umur saat ini sudah >= 17? \nsudah atau belum : ')

data = int(a)
if b.lower() == 'sudah':
    tekstur = 1
elif b.lower() == 'belum':
    tekstur = 0
else:
    print('Unknown')

c = mesin.predict([[data, tekstur]])
if c == 0:
    d = 'Selamat nak, kamu sudah bisa pacaran'
    if c == 1:
        d = 'Sayang Sekali, saat ini masih belum bisa pacaran nak'
else:
    d = 'Sayang Sekali, saat ini masih belum bisa pacaran nak'

print('Keputusan Papah Mamah : {}'.format(d))