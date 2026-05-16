# Image Steganography using LSB Technique

## Aim

To hide and retrieve secret information inside an image using the Least Significant Bit (LSB) steganography technique.

## File Structure

```text
SteganographyProject/
│
├── input.png
├── encode.py
├── decode.py
├── secret_image.png
└── README.md# Image-Steganography-Using-LSB
```

## Algorithm
1. Start the program.
2. Import the LSB module from the Stegano library.
3. Load the input image named input.png.
4. Hide the secret message inside the image using the LSB technique.
5. Save the output image as secret_image.png.
6. Load the stego image named secret_image.png.
7. Extract the hidden message from the stego image.
8. Display the hidden message.
9. Stop the program.

## Program

### Encoding Code
```
from stegano import lsb

# Hide secret message inside input.png
secret = lsb.hide("input.png", "This is my secret message")

# Save the new image
secret.save("secret_image.png")

print("Secret message hidden successfully!")
```

### Decoding Code
```
from stegano import lsb

# Reveal hidden message from secret_image.png
message = lsb.reveal("secret_image.png")

print("Hidden Message:")
print(message)
```

## Output
<img width="552" height="91" alt="image" src="https://github.com/user-attachments/assets/21c4af13-c00a-4f9a-b381-2ae354a5d1c3" />

## Result
Thus, the secret message was successfully hidden inside an image and retrieved using the Least Significant Bit steganography technique.
