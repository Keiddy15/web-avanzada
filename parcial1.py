"""
Dado un conjunto de puntos en un plano cartesiano, 
se te pide encontrar los dos puntos más cercanos entre sí. 
Implementa una función llamada pares_cercanos que tome una lista de coordenadas (puntos en el plano) 
y devuelva las coordenadas de los dos puntos más cercanos junto con su distancia. 
Utiliza el algoritmo "Divide y Vencerás" para resolver este problema de manera eficiente, 
este ejercicio deberá usar Decoradores, como args y kwargs.


"""
import math

#Finding the distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

#using divide and conquer for the closet pair
def closest_pair(points):
    n = len(points)
    if n <= 1:
        return None, None, float('inf')
    elif n == 2:
        return points[0], points[1], distance(points[0], points[1])
    
    # Sorting points by x-coordinate
    points.sort()

    mid = n // 2
    mid_point = points[mid]
    
    #  Divide points into left and right halves
    left_part = points[:mid]
    right_part = points[mid:]

    #Recursive: Find closest pairs in left and right halves
    left_c1, left_c2, left_dist = closest_pair(left_part)
    right_c1, right_c2, right_dist = closest_pair(right_part)

    if left_dist < right_dist:
        dist = left_dist
        pair = (left_c1, left_c2)
    else:
        dist = right_dist
        pair = (right_c1, right_c2)

    # Create a strip of points within min_dist of the middle x-coordinate
    strip = [point for point in points if abs(point[0] - mid_point[0]) < dist]


    # Sort the strip by y-coordinate
    strip.sort(key=lambda point: point[1])

    strip_p1, strip_p2, strip_dist = None, None, float('inf')

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < dist:
            dist = distance(strip[i], strip[j])
            if dist < strip_dist:
                strip_dist = dist
                strip_p1, strip_p2 = strip[i], strip[j]
            j += 1

    # Update min_dist and min_pair if an even closer pair is found 
    if strip_dist < dist:
        dist = strip_dist
        pair = (strip_p1, strip_p2)

    return pair[0], pair[1], dist

#Using decorators
def closest_pairs_decorator(*args, **kwargs):
    return closest_pair(args[0])


def main():
    print("FIRST EXAMPLE")
    coor = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    result = closest_pairs_decorator(coor)
    print(f"Closest points: {result[0]} {result[1]}]")
    print(f"Distance: {result[2]}")
    print("SECOND EXAMPLE")
    coor = [(.3, 2.3), (1.6, 30), (4, 5), (15, 1.8), (2.3, 10), (5.5, 6.7)]
    result = closest_pairs_decorator(coor)
    print(f"Closest points: {result[0]} {result[1]}]")
    print(f"Distance: {result[2]}")

if __name__ == "__main__":
    main()