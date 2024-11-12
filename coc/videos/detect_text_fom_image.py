def detect_text_from_image(image_path):
    print(settings.credentials)  # Add this line to debug

    # Use credentials stored in settings.py
    client = vision.ImageAnnotatorClient(credentials=settings.credentials)

    # Load the image into memory
    with open(image_path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image)
    return response