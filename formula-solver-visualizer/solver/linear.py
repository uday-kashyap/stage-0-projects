import numpy as np
import matplotlib.pyplot as plt

class Linear_Equations:
    
    def evaluation(self) -> None:
        """
        Handles both input and output
        """
        while True:
            options ={
                 1:"Roots of Equation in One Variable",
                 2:"Roots of Equations in Two Variables",
                 3:"Slope Intercept Form",
                 4:"Plot the Linear Equation",
                 5:"Previous Menu"
            }
            print("-------------------------------------")
            for key,value in options.items():
                print(F"{key}. {value}")
            print("-------------------------------------")
            try:
                choice = int(input("Enter your choice please: "))                         
                if choice not in options:
                    print("⚠️  Enter valid choice please!")
            except ValueError:
                print("⚠️  The input must be an integer only")
            else:
                if choice==1:
                    self.display_one_variable_root()
                    return
                if choice==2:
                    self.display_two_variable_roots()
                    return
                if choice==3:
                    self.display_slope_intercept_form()
                    return
                if choice==4:
                    self.plot_linear()
                    return
                if choice==5:
                    return
                            



    # Formats the integer type floating point number into integer
    def format_num(self, n: float) -> int|float:
        return int(n) if n.is_integer() else n



    
    # Roots of Equation in One Variable
    def get_input_one_line(self) -> tuple[float,float]:
        """
        Takes coefficient 'a' and a constant term 'c' of a given line in the form of 'ax+c=0'
        """
        while True:
            try:
                print("-------------------------------------")
                a=float(input("Enter the coefficient of x: "))
                if a==0:
                    print("❌ The coefficient of x cannot be zero in linear equation")
                    continue
                c=float(input("Enter the constant term: "))
                return a,c
            except ValueError:
                print("⚠️  The input must be a number only")

    def calculate_one_variable_root(self, a: int|float, c: int|float) -> float:
        # ax + c = 0
        return -c/a
    
    def display_one_variable_root(self):
        a,c = self.get_input_one_line()
        a,c = [self.format_num(value) for value in [a,c]]
        root = self.calculate_one_variable_root(a,c)
        print("-------------------------------------")
        print(f"Your Equation: {str(a)}x{'+' if c>=0 else '-'}{str(abs(c))}=0")
        print("x = ",round(root, 2))
    


    # Roots of Equations in Two Variables
    def get_input_abc(self, linenumber_str='the') -> tuple[float,float,float]:
        """
        Takes coefficients 'a','b' and a constant term 'c' of a straight line in the form of 'ax+by=c'
        """
        while True:
            try:
                print("-------------------------------------")
                a=float(input(f"Enter the coefficient of x for {linenumber_str} equation: "))
                b=float(input(f"Enter the coefficient of y for {linenumber_str} equation: "))
                c=float(input(f"Enter the constant term for {linenumber_str} equation: "))
                return a,b,c
            except ValueError:
                print("⚠️  The input must be a number only")

    def calculate_two_variable_roots(self, a1: int|float , b1: int|float , c1: int|float , a2: int|float , b2: int|float , c2: int|float) -> np.ndarray:
        # a1x + b1y = c1
        # a2x + b2y = c2
        A = np.array([[a1,b1],
                      [a2,b2]])
        B = np.array([c1,c2])
        solutions = np.linalg.solve(A,B)
        return solutions
    
    def display_two_variable_roots(self) -> None:
        a1,b1,c1 = self.get_input_abc('first')
        a2,b2,c2 = self.get_input_abc('second')
        if (a1==0 and b1==0) or (a2==0 and b2==0):
            print("❌ The coefficients of both x and y cannot be zero")
            return
        a1,b1,c1,a2,b2,c2 = [self.format_num(value) for value in [a1,b1,c1,a2,b2,c2]]
        print("-------------------------------------")
        print(f"Your Equation 1: {str(a1)}x{'+' if b1>=0 else '-'}{str(abs(b1))}y={str(c1)}")
        print(f"Your Equation 2: {str(a2)}x{'+' if b2>=0 else '-'}{str(abs(b2))}y={str(c2)}")
        if (a1/a2)!=(b1/b2): #unique solutions
            solutions = self.calculate_two_variable_roots(a1,b1,c1,a2,b2,c2)
            print("x = ", round(solutions[0],2))
            print("y = ", round(solutions[1],2))
        elif (a1/a2)==(b1/b2)==(c1/c2): #infinite solutions
            print("The given lines have infinite number of solutions!")
        else: #no solutions
            print("The given lines have no solutions!")
    


    # Slope Intercept Form
    def get_input_slope_intercept(self, coordinate_number: int) -> tuple[int|float, int|float]:
        """
        Takes x and y coordinates of a line passing from two points '(x1,y1) & (x2,y2)'
        """
        while True:
            try:
                print("-------------------------------------")
                x = int(input(f"Enter x{coordinate_number} coordinate: "))
                y = int(input(f"Enter y{coordinate_number} coordinate: "))
                return x,y
            except ValueError:
                print("⚠️  The input must be a number only")

    def calculate_slope_intercept(self, x1: int|float, y1: int|float, x2: int|float, y2: int|float) -> tuple[int|float, int|float]:
        # y = mx + c
        x = np.array([x1,x2])
        y = np.array([y1,y2])
        m,c = np.polyfit(x,y,1)
        m = round(m,2)
        c = round(c,2)
        return m,c
    
    def display_slope_intercept_form(self) -> None:
        x1,y1 = self.get_input_slope_intercept(1)
        x2,y2 = self.get_input_slope_intercept(2)
        x1,y1,x2,y2 = [self.format_num(value) for value in [x1,y1,x2,y2]]
        if x1 == x2:
            print("The line is vertical — slope is undefined.")
            print(f"Equation: x = {x1}")
            return
        m,c = self.calculate_slope_intercept(x1,y1,x2,y2)
        print("-------------------------------------")
        print(f"Your Equation: y={str(m)}x{'+' if c>=0 else '-'}{str(abs(c))}")
        print(f"(where, slope is {m} and y-intercept is {c})")



    # Plot the Linear Equation
    def plot_linear(self) -> None:
        a,b,c = self.get_input_abc()
        a,b,c = [self.format_num(value) for value in [a,b,c]]

        # No solutions
        if a == 0 and b == 0 and c != 0:
            plt.text(0.5, 0.5, 'No solution\nContradictory Equation',
                    horizontalalignment='center', verticalalignment='center',
                    transform=plt.gca().transAxes, fontsize=14, color='red')
            plt.title(f"Graph of: {str(a)}x + {str(b)}y = {str(c)}", color='red')
            plt.xlabel('X - axis')
            plt.ylabel('Y - axis')
            plt.grid(True, linestyle='--', alpha=0.3)
            plt.show()
            return
        
        # Infinite solutions
        if a == 0 and b == 0 and c == 0:
            plt.text(0.5, 0.5, '♾️ Infinitely many solutions\nAny point (x, y) satisfies',
                    horizontalalignment='center', verticalalignment='center',
                    transform=plt.gca().transAxes, fontsize=14, color='green')
            plt.title(f"Graph of: {str(a)}x + {str(b)}y = {str(c)}", color='red')
            plt.xlabel('X - axis')
            plt.ylabel('Y - axis')
            plt.grid(True, linestyle='--', alpha=0.3)
            plt.show()
            return
        
        x_intercept = c/a if a!=0 else None
        y_intercept = c/b if b!=0 else None
        if x_intercept is not None and y_intercept is not None:
            x = np.linspace(min(x_intercept-3,y_intercept-3),max(x_intercept+3,y_intercept+3),300)
            y = (c/b)-(a/b)*x

        #for constant equation: x = k or y = k
        if x_intercept is None and y_intercept is not None:
            x = np.linspace(-10,10,300)
            y = np.full_like(x,y_intercept)
        if x_intercept is not None and y_intercept is None:
            y = np.linspace(-10,10,300)
            x = np.full_like(y,x_intercept)
        
        plt.figure(figsize=(8,6))
        plt.axhline(0, color='black', linewidth=0.5)  # plot the x-axis
        plt.axvline(0, color='black', linewidth=0.5)  # plot the y-axis
        plt.plot(x,y,color='blue')
        if x_intercept is not None:
            plt.scatter(x_intercept, 0, color='green', label=f'X-Intercept (0,{round(x_intercept,2) if x_intercept!=0 else 0})') # mark the x-intercept
        if y_intercept is not None:
            plt.scatter(0, y_intercept, color='green', label=f'Y-Intercept (0,{round(y_intercept,2) if y_intercept!=0 else 0})') # mark the y-intercept
        plt.title(f"Graph of the equation: {str(a)}x{'+' if b>=0 else '-'}{str(abs(b))}y={str(c)}", color='red')
        plt.xlabel('X - axis')
        plt.ylabel('Y - axis')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.show()

        