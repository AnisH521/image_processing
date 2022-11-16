with open("girl.pgm") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
    file_in.close()

new_image = []
pixels = []

for i in range(4):
    if i == 3:
        new_image.append(lines[i].replace("255\n", "1\n"))
    else:
        new_image.append(lines[i])

for line in lines[4:]:
    pixels.append(int(line))

for pixel in pixels:
    new_image.append(str(format(pixel, "08b")[5]) + "\n")

with open(f"bit_girl.pgm", "w") as file_out:
    for line in new_image:
        file_out.writelines(line)
    file_out.close()