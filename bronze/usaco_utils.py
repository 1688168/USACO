import sys, os

def get_inputs(filename):
    full_path=os.path.join(os.getcwd(), filename)

    output=[]
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            line = f.readline()
            print(" ===== reading inputs =====")
            while line:
                print(line, end='')
                output.append(line.strip())
                line = f.readline()

            print()
    except Exception as e:
        print(" exception: ", e)
        raise
    print()
    print("===== end of getting inputs =====")
    return output