import numpy as np
import matplotlib.pyplot as plt

class Quadratic_Equations:

    def evaluation(self) -> None:
        """
        Handles both input and output
        """
        while True:
            options = {
                1:"Roots of the Equation",
                2:"Sum of Roots",
                3:"Product of Roots",
                4:"Form Quadratic Equation",
                5:"Vertex Form and Axis of Symmetry",
                6:"Plot the Quadratic Equation",
                7:"Previous Menu"
            }
            print("-------------------------------------")
            for key,value in options.items():
                print(F"{key}. {value}")
            print("-------------------------------------")
            try:
                choice = int(input("Enter your choice please: "))
                 # check for choice in list           
                if choice not in options:
                    print("⚠️  Enter valid choice please!")
            except ValueError:
                print("⚠️  The input must be an integer only")
            else:
                if choice==1:
                    self.display_roots()
                    return
                if choice==2:
                    self.display_sum_of_roots()
                    return
                if choice==3:
                    self.display_product_of_roots()
                    return
                if choice==4:
                    self.display_quadratic()
                    return
                if choice==5:
                    self.vertex_form()
                    return
                if choice==6:
                    self.plot_quadratic()
                    return
                if choice==7:
                    return
                



    # Text Formatting
    def format_num(self, n: float) -> int|float:
        """
        Formats the integer type floating point number into integer (generally for displaying equation)
        """
        return int(n) if n.is_integer() else n




    # Roots of the Equation        
    def get_input_abc(self) -> tuple[float,float,float]:
        """
        Takes coefficients 'a','b' and a constant term 'c' of quadratic equation in the form of 'ax²+bx+c' 
        """
        while True:
            try:
                print("-------------------------------------")
                a=float(input("Enter the coefficient of x²: "))
                if a==0:
                    print("❌ The coefficient of x² cannot be zero in quadratic equation")
                    continue
                b=float(input("Enter the coefficient of x: "))
                c=float(input("Enter the constant term: "))
                return a,b,c
            except ValueError:
                print("⚠️  The input must be a number only")

    def calculate_roots(self, a: int|float, b: int|float, c: int|float) -> tuple[complex,complex]:
        # ax² + bx + c = 0 
        d = (b**2)-(4*a*c)
        sqrt_d = np.lib.scimath.sqrt(d)
        x1= ((-b)+sqrt_d)/(2*a)
        x2= ((-b)-sqrt_d)/(2*a)
        return x1,x2

    def display_roots(self) -> None:
        a,b,c = self.get_input_abc()
        a,b,c = [self.format_num(value) for value in [a,b,c]]
        x1,x2 = self.calculate_roots(a,b,c)
        print("-------------------------------------")
        print(f"Your Equation: {str(a)}x²{'+' if b>=0 else '-'}{str(abs(b))}x{'+' if c>=0 else '-'}{str(abs(c))}=0")
        print("Root 1 = ", round(x1,2))
        print("Root 2 = ", round(x2,2))




    # Vertex Form and Axis of Symmetry
    def calculate_vertex(self, a: int|float, b: int|float, c: int|float) -> tuple[float,float]:
        # (h,k)
        h = -b/(2*a)
        k = a*h**2+b*h+c
        return (h,k)
    
    def vertex_form(self) -> None:
        # y = a(x - h)² + k
        a,b,c = self.get_input_abc()
        a,b,c = [self.format_num(value) for value in [a,b,c]]
        vertex = self.calculate_vertex(a,b,c)  
        h = round(vertex[0],2)
        h_sign = ('-' if h<0 else '+')
        k = round(vertex[1],2)
        k_sign = ('-' if k<0 else '+')
        print("-------------------------------------")
        print(f"Vertex Form: y={a}(x{h_sign}{abs(h)})²{k_sign}{abs(k)}")
        print(f"Vertex: ({h},{k})")
        print(f"Axis of Symmetry: x={h}")



    # Product of Roots
    def get_input_por(self) -> tuple[float,float]:
        """
        Takes coefficient 'a' and a constant term 'c' of a line in the form of 'ax²+bx+c=0'
        """
        while True:
            try:
                print("-------------------------------------")
                a=float(input("Enter the coefficient of x²: "))
                if a==0:
                    print("❌ The coefficient of x² cannot be zero in quadratic equation")
                    continue
                c=float(input("Enter the constant term: "))
                return a,c
            except ValueError:
                print("⚠️  The input must be a number only")

    def calculate_product_of_roots(self, a: int|float, c: int|float) -> float:
        # x1 * x2 = c / a
        return c/a
    
    def display_product_of_roots(self) -> None:
        a,c = self.get_input_por()
        a,c = [self.format_num(value) for value in [a,c]]
        por = self.calculate_product_of_roots(a,c)
        print("-------------------------------------")
        print("Product of roots = ",round(por,2))



    # Sum of Roots
    def get_input_sor(self) -> tuple[float,float]:
        """
        Takes coefficients 'a' and 'b' of a line in the form of 'ax²+bx+c=0'
        """
        while True:
            try:
                print("-------------------------------------")
                a=float(input("Enter the coefficient of x²: "))
                if a==0:
                    print("❌ The coefficient of x² cannot be zero in quadratic equation")
                    continue
                b=float(input("Enter the coefficient of x: "))
                return a,b
            except ValueError:
                print("⚠️  The input must be a number only")

    def calculate_sum_of_roots(self, a: int|float, b: int|float) -> float:
        # xi + x2 = -b / a
        return -b/a
    
    def display_sum_of_roots(self) -> None:
        a,b = self.get_input_sor()
        a,b = [self.format_num(value) for value in [a,b]]
        sor = self.calculate_sum_of_roots(a,b)
        print("-------------------------------------")
        print("Sum of roots = ",round(sor,2))



    # Form Quadratic Equation
    def get_input_form_quadratic(self) -> tuple[float,float]:
        """
        Takes both the roots of the quadratic equation
        """
        while True:
            try:
                print("-------------------------------------")
                x1=float(input("Enter the first root: "))
                x2=float(input("Enter the second root: "))
                return x1,x2
            except ValueError:
                print("⚠️  The input must be a number only")

    def form_quadratic(self, x1: int|float, x2: int|float) -> str:
        # x² - (sum of roots) + (product of roots) = 0
        roots = np.array([x1,x2])
        equation = np.poly1d(roots, True)
        return equation
    
    def display_quadratic(self) -> None:
        x1,x2 = self.get_input_form_quadratic()
        equation = self.form_quadratic(x1,x2)
        print("-------------------------------------")
        print(equation)



    # Plot the Quatratic Equation
    def plot_quadratic(self) -> None:
        a,b,c = self.get_input_abc()
        a,b,c = [self.format_num(value) for value in [a,b,c]] 
        vertex = self.calculate_vertex(a,b,c)
        x1,x2=self.calculate_roots(a,b,c)
        h = vertex[0]
        k = vertex[1]
        x = np.linspace(min(-3,(2*h)-3),max(3,(2*h)+3), 300)
        y = a*x**2+b*x+c
        plt.figure(figsize=(8,6))
        plt.axhline(0, color='black', linewidth=0.5)  # plot the x-axis
        plt.axvline(0, color='black', linewidth=0.5)  # plot the y-axis
        plt.plot(x,y,color='blue')
        plt.scatter(h,k,color='black',marker='o',label=f'Vertex ({round(h,2)},{round(k,2)})') # mark the vertex
        plt.scatter(0, c, color='green', label=f'Y-Intercept (0,{round(c,2)})') # mark the y-intercept
        if not isinstance(x1, complex) and not isinstance(x2, complex):
            plt.scatter(x1,0,color='red',marker='o') # mark root 1
            plt.scatter(x2,0,color='red',marker='o') # mark root 2
        plt.title(f"Graph of the equation: {str(a)}x²{'+' if b>=0 else '-'}{str(abs(b))}x{'+' if c>=0 else '-'}{str(abs(c))}=0", color='red')
        plt.xlabel('X - axis')
        plt.ylabel('Y - axis')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.show()
        

            


