#Write a function that computes the volume of a sphere given its radius.

def sphere_volume(radius):
    volume = (4 / 3) * 3.14159 * (radius ** 3)
    return volume

radius = float(input("The radius of the sphere: "))
print(f"The volume of the sphere : {sphere_volume(radius):.2f}")
