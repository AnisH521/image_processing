import numpy as np

def negative_image() -> None:
    with open("dog.pgm") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        file_in.close()

    with open("log_transformed_dog.pgm", "w") as file_out:
        file_out.close()

    with open("log_transformed_dog.pgm", "a") as file_out:

        c = 70

        pixels = []
        new_image = []

        for line in lines[4:]:
            pixels.append(str(round(c*np.log10(1 + int(line)))) + "\n")
        for i in range(4):
            new_image.append(lines[i])
        new_image.extend(pixels)

        for line in new_image:
            file_out.writelines(line)

        file_out.close()

def main() -> None:
    negative_image()

if __name__ == "__main__":
    main()