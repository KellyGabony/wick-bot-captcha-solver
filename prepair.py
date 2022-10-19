def prepair(img):
        image_data = img.load()
        height, width = img.size
        for loop1 in range(height):
            for loop2 in range(width):
                r, g, b, _ = image_data[loop1, loop2]
                if r in range(95, 110):
                    if g in range(95, 110):
                        if b in range(95, 110):
                            image_data[loop1, loop2] = 0, 0, 0, 0
        return img