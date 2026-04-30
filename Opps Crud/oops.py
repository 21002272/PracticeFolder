class Movie:
    def __init__(self):
        self.movies = {}
    def post(self, t,d,y,r):
        self.movies[t] = [d,y,r]
        print("Movie" + t+ "is created!")
    def get(self,t):
        print(self.movies[t])
    def get_all(self):
        print(self.movies)
    def put(self,t,new_value):
        self.movies[t]=new_value
    def delete(self,t):
        del self.movies[t]
m = Movie()
m.post("robo","a tech film",2000,4)
m.get("robo")
m.post("leo","action movie",2023,5)
m.get_all()
m.put("robo",["a sci-fi film",2010,5])
m.get("robo")
m.delete("leo")
m.get_all()