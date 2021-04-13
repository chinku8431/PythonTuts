#Dynamic qrcode exampe to create qrcode and save
import qrcode

text=input("Enter a Message:")
file_path=input("Enter file name with path:")
qrcode.make(text).save(file_path)
print("qrcode created and save")