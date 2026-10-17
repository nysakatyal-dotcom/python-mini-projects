import imageio.v3 as iio

filenames = ['image1.jpg', 'image2.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)

  #cd Desktop
  #python3 create_gif.py
  #open with safari and airdrop and to open on phone save to file then save it
  # to phtos then and
  # to change width and all sips -z 1920 1080 image1.jpg sips -z 1920 1080 image2.jpg
 # typethis in terminal
 
