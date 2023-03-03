def threshold_image() -> None:
    with open("girl.pgm") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        file_in.close()

    with open("thresolding_girl.pgm", "w") as file_out:
        file_out.close()

    with open("thresolding_girl.pgm", "a") as file_out:
        pixels = []
        new_image = []

        for line in lines[4:]:
            pixels.append(int(line))

        thresold = 130
        
        for i in range(4):
            new_image.append(lines[i])
        for pixel in pixels:
            if pixel > thresold:
                pixel = 255
                new_image.append(str(pixel) + "\n")
            else:
                pixel = 0
                new_image.append(str(pixel) + "\n")
                
            #print(new_image)        

        for line in new_image:
            file_out.writelines(line)

        file_out.close()

def main() -> None:
    threshold_image()

if __name__ == "__main__":
    main()
