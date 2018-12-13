class Vector3D:
    def __init__ (self, x1,x2,x3):
        self.x1=x1
        self.x2=x2
        self.x3=x3
    def __add__(self, v2):
        if isinstance(v2,int):
            return Vector3D( self.x1+v2, self.x2+v2,self.x3+v2 )
        
        return Vector3D( self.x1+v2.x1, self.x2+v2.x2, self.x3+v2.x3 )
    def __sub__(self,v2):
        if isinstance(v2,int):
            return Vector3D( self.x1-v2, self.x2-v2,self.x3-v2 )
        
        return Vector3D( self.x1-v2.x1, self.x2-v2.x2, self.x3-v2.x3 )
    def __mul__(self,v2):
        return Vector3D(self.x2*v2.x3,self.x3*v2.x1,self.x1*v2.x2)
    def dot(self,v2):
        return elf.x1*v2.x1+self.x2*v2.x2+self.x3*v2.x3
    def norm(self):
        return (self.x1**2+self.x2**2+self.x3**2)**0.5
