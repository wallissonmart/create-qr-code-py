import qrcode
import json

objeto = {
    'id_venda': 50,
    'valor_venda': 30.00,
}

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(json.dumps(objeto))
qr.make(fit=True)
imagem_qr = qr.make_image(fill_color='black', back_color='white')

imagem_qr.save('qr_code_objeto.png')
