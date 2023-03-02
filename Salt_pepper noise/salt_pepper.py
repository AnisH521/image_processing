import numpy as np

def salt_pepper_noise_image() -> None:
    with open("girl.pgm") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        file_in.close()

    with open("noise_girl.pgm", "w") as file_out:
        file_out.close()

    with open("noise_girl.pgm", "a") as file_out:

        pepper = 0.05
        salt = 1 - pepper

        pixels = []
        new_image = []

        for line in lines[4:]:
            rdn = np.random.random()
            if rdn < pepper:
                pixels.append(str(0) + "\n")
            elif rdn > salt:
                pixels.append(str(255) + "\n")
            else:
                pixels.append(line)

        for i in range(4):
            new_image.append(lines[i])
        new_image.extend(pixels)

        for line in new_image:
            file_out.writelines(line)

        file_out.close()

def main() -> None:
    salt_pepper_noise_image()

if __name__ == "__main__":
    main()