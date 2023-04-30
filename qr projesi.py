import qrcode # pip install qrcode
from qrcode import constants
import cv2   # görüntüyü algılama  
import webbrowser
import barcode # pip install barcode
from barcode.writer import ImageWriter  #pip install python-barcode 
from pyzbar.pyzbar import decode # pip install pyzbar



code = qrcode.QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_L,
    box_size=20, border=5
)

print("")
print("|=================================== |")
print(" YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ:  ")
print("|=================================== |")
print("")
print("1 = QR KOD OLUŞTUR ")
print("2 = QR KOD OKU ")
print("3 = BARKODU OLUŞTUR ")
print("4 = BARKODU OKU ")
print("")


secim = input("(1/2/3/4) SEÇİMİNİZ: ")

if secim == '1': 
    print()
    giris = input("BAĞLANTIYI GİRİNİZ: ")

    qr = qrcode.QRCode(
    version=None,
    error_correction=constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

    qr.add_data(giris)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("")
    print("QR kodunuz oluşturuldu!")



elif secim == '2':
    print()
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        _,img = cap.read()
        data,one, _ = detector.detectAndDecode(img)


        if data:
            a = data
            break

        cv2.imshow('QRCODE OKUYUCU',img)

        if cv2.waitKey(1) == ord("q"):
            break

    b = webbrowser.open(str(a))
    cap.release()
    cv2.destroyAllWindows()



elif secim == '3':
    print()
    barkod_numarasi = input("Lütfen barkod numarasını girin: ")

    code128 = barcode.get('code128', barkod_numarasi, writer=ImageWriter())

    code128.save('barkod')

    print("BARKODUNUZ OLUŞTURULDU...")



elif secim == '4':
    print()
    cap = cv2.VideoCapture(0)


    while True:

        ret, frame = cap.read()
        decoded_objects = decode(frame)

        for obj in decoded_objects:

            print("Barkod içeriği:", obj.data.decode())

        cv2.imshow('BARCODE OKUYUCU', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



else:
    print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 seçimlerinden birini yapın.")

