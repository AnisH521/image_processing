def bit_plane_slicing() -> None:

    with open("dog.pgm") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        file_in.close()

    pixels = []

    for line in lines[4:]:
        pixels.append(int(line))    

    for i in range(8):
        new_image = []

        for j in range(4):
            if j == 3:
                new_image.append(lines[j].replace("255\n", "1\n"))
            else:
                new_image.append(lines[j])

        for pixel in pixels:
            new_image.append(format(pixel, "08b")[i] + "\n")

        with open(f"{i + 1}bit_dog.pgm", "w") as file_out:
                
            for line in new_image:
                file_out.writelines(line)

            file_out.close()


def main() -> None:
    bit_plane_slicing()

if __name__ == "__main__":
    main()