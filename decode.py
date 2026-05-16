from stegano import lsb

# Reveal hidden message from secret_image.png
message = lsb.reveal("secret_image.png")

print("Hidden Message:")
print(message)