#PythonGL instance
class PyGL:
    def __init__(self,  w: int, h:int): #init values
        self.w = w 
        self.h = h
        self.sqr = 0
        self.cw = 1 # For making height!
        self.n = ""
    def area(self): 
        """ Calculate area. Run before render!"""
        sqr = self.w*self.h
        self.sqr = sqr
    def render(self):
        """Render 2D image."""
        cw = self.cw
        n = self.nn
        sqr = self.sqr
        for i in range(sqr):
            n+="x"
            if cw  == self.w:
                n+="\n"
                cw = 1
            else:
                cw += 1
        print(n)
        
gl = PyGL(30, 5)
gl.area()
gl.render()
        

    

