from image_creator import AvatarGenerator

def generate_avatar():
    generator = AvatarGenerator("./images")
    generator.generate_avatar(1)


if __name__ == "__main__":
    generate_avatar()
