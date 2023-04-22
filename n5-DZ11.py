import cv2
from PIL import Image, ImageFilter

print('note that latest result will overwrite previous')
print('coordinate mode - left, upper, right, lower')
path = input('source path: ')
image = cv2.imread(path)
print('0/1')
rcgn_p = int(input('recognize people? - '))
rcgn_c = int(input('recognize cats? - '))
if rcgn_p == 1:
    human_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    human_face = human_face_cascade.detectMultiScale(image)
if rcgn_c == 1:
    cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
    cat_face = cat_face_cascade.detectMultiScale(image)
img = Image.open(path)
img = img.convert('RGBA')

print('glasses_overlay; filter_blur; crop; paste; resize; convert')
mode = input('mode: ')
if mode == 'glasses_overlay':
    path_glasses = input('glasses path: ')
    glasses = Image.open(path_glasses)
    glasses = glasses.convert('RGBA')

    if rcgn_c == 1:
        for (x, y, w, h) in cat_face:
            print('cat face found')
            glasses = glasses.resize((w, int(h/3)))
            img.paste(glasses, (x, int(y+h/4)), glasses)
    if rcgn_p == 1:
        for (x, y, w, h) in human_face:
            print('human face found')
            glasses = glasses.resize((w, int(h/3)))
            img.paste(glasses, (x, int(y+h/4)), glasses)

    if rcgn_c == 0 and rcgn_p == 0:
        img.show('source')
        print(f'width {img.width}')
        print(f'height {img.height}')
        pstw = int(input('paste width: '))
        psth = int(input('paste height: '))
        img.paste(glasses, (pstw, psth), glasses)

    img.save('latest.png')
    img.show('result')

elif mode == 'filter_blur':
    if rcgn_c == 1:
        for (x, y, w, h) in cat_face:
            print('cat face found')
            imgcat = img.crop((x, y, (x + w), (y + h)))
            imgcat = imgcat.filter(ImageFilter.BLUR)
            img.paste(imgcat, (x, y))
    if rcgn_p == 1:
        for (x, y, w, h) in human_face:
            print('human face found')
            imghuman = img.crop((x, y, (x + w), (y + h)))
            imghuman = imghuman.filter(ImageFilter.BLUR)
            img.paste(imghuman, (x, y))

    if rcgn_c == 0 and rcgn_p == 0:
        img.show('source')
        print(f'width {img.width}')
        print(f'height {img.height}')
        pstw = int(input('paste width: '))
        psth = int(input('paste height: '))
        img.filter(ImageFilter.BLUR)

    img.save('latest.png')
    img.show('result')

elif mode == 'crop':
    if rcgn_c == 1:
        for (x, y, w, h) in cat_face:
            print('cat face found')
            img_crop_cat = img.crop((x, y, (x + w), (y + h)))
            img_crop_cat.save('latest_crop_cat.png')
            img_crop_cat.show('result_cat')
    if rcgn_p == 1:
        for (x, y, w, h) in human_face:
            print('human face found')
            img_crop_human = img.crop((x, y, (x + w), (y + h)))
            img_crop_human.save('latest_crop_human.png')
            img_crop_human.show('result_human')

    if rcgn_c == 0 and rcgn_p == 0:
        img.show('source')
        print(f'width {img.width}')
        print(f'height {img.height}')
        crpw1 = int(input('crop1 width: '))
        crpw2 = int(input('crop2 width: '))
        crph1 = int(input('crop1 height: '))
        crph2 = int(input('crop2 height: '))
        img.crop((crpw2, crpw1, crph2, crph1))
        img.save('latest.png')
        img.show('result')

elif mode == 'paste':
    img.show('source')
    print(f'width {img.width}')
    print(f'height {img.height}')
    path_paste = input('paste path: ')
    img_paste = Image.open(path_paste)
    paste_x = int(input('left x: '))
    paste_y = int(input('up y: '))
    resize_x = int(input('resize x: '))
    resize_y = int(input('resize y: '))
    img_paste = img_paste.resize((resize_x, resize_y))
    img.paste(img_paste, (paste_x, paste_y), img_paste)
    img.save('latest.png')
    img.show('result')

elif mode == 'resize':
    resize_x = int(input('resize x: '))
    resize_y = int(input('resize y: '))
    img = img.resize((resize_x, resize_y))
    img.save('latest.png')
    img.show('result')

elif mode == 'convert':
    print('example: .png')
    exfrm = input('format: ')
    img.save(f'latest{exfrm}')
