import importlib


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main(input):
    # Contrived example of generating a module named as a string
    full_module_name = "problems.problem_" + input

    # The file gets executed upon import, as expected.
    mymodule = importlib.import_module(full_module_name)
    print(bcolors.OKBLUE + mymodule.problem.__doc__ + bcolors.ENDC)
    print("Solution : " + bcolors.OKGREEN + str(mymodule.problem()) + bcolors.ENDC)


if __name__ == "__main__":
    problem_input = input("Please enter the serial number of the problem you want to solve : ")
    main(problem_input)
