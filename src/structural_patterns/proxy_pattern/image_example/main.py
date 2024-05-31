from image import ImageProxy

if __name__ == "__main__":
    proxy_image = ImageProxy("sample.jpg")

    # Image is not loaded yet
    print("Proxy created, image not loaded.")

    # Image is loaded only when display is called
    proxy_image.display()
