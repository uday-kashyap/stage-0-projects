from solver import Quadratic_Equations, Linear_Equations

quad_eq = Quadratic_Equations()
linear_eq = Linear_Equations()

if __name__ == '__main__':
    print("----FORMULA SOLVER AND VISUALIZER----")
    while True:
        options = {
            1:"Linear Equations",
            2:"Quadratic Equations",
            3:"Exit"
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
                continue
        except ValueError:
            print("⚠️  The input must be an integer only")
        else:
            if choice==1:
                linear_eq.evaluation()
            if choice==2:
                quad_eq.evaluation()       
            if choice==3:
                exit("The program was terminated :)")
