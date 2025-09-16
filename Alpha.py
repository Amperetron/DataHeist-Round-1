import Bravo
import Charly      
import Delta

def assemble_password():
    # Collect fragments from remaining modules
    part1 = Bravo.get_fragment()
    part2 = Charly.get_fragment()   
    part3 = Delta.get_fragment()

   
    return part1 + "-" + part2 + "-" + part3

if __name__ == "__main__":
    print("Final Password:", assemble_password())

