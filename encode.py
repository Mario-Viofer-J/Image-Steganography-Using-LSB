from stegano import lsb

# Hide secret message inside input.png
secret = lsb.hide("input.png", "This is my secret message")

# Save the new image
secret.save("secret_image.png")

print("Secret message hidden successfully!")