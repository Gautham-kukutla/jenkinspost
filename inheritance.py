class Polygon:
    def sides_no(self):
        pass


class Triangle(Polygon):
    def area(self):
        pass


obj_polygon = Polygon()
obj_triangle = Triangle()
print(isinstance(obj_triangle, Triangle))   	# true
print(isinstance(obj_triangle, Polygon))    	# false
print(isinstance(obj_polygon, Polygon)) 	# true
print(isinstance(obj_triangle, Polygon))
