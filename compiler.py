import marshal
import os

# Function to get Python code from user and save to a file
def get_code_and_compile():
    # Ask user for the filename
    file_name = input("Enter the name of the Python file (without extension): ") + ".py"import marshal
import base64
import os

# Function to get Python code from user and save to a file
def get_code_and_compile():
    # Ask user for the filename
    file_name = input("Enter the name of the Python file (without extension): ") + ".py"
    
    # Ask the user to input the Python code
    print("Enter your Python code. Press Ctrl+D (or Ctrl+Z on Windows) to finish input.")
    python_code = []
    
    try:
        # Taking multiline input from the user (until EOF)
        while True:
            line = input()
            python_code.append(line)
    except EOFError:
        pass
    
    # Join the list into a single string of code
    code_string = '\n'.join(python_code)

    # Save the code to the file
    with open(file_name, 'w') as f:
        f.write(code_string)
    
    print(f"Python code saved to {file_name}")

    # Ask the user which compilation method to use
    print("\nChoose the compilation method:")
    print("1. Marshal")
    print("2. Base64")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Compile the code using marshal
        compiled_code = compile(code_string, file_name, 'exec')

        # Save the compiled code using marshal
        compiled_file_name = file_name.replace(".py", ".pyc")
        with open(compiled_file_name, 'wb') as f:
            marshal.dump(compiled_code, f)
        
        print(f"Compiled bytecode saved to {compiled_file_name}")
    
    elif choice == "2":
        # Compile the code to base64
        compiled_code = compile(code_string, file_name, 'exec')

        # Convert the bytecode to base64
        bytecode = marshal.dumps(compiled_code)
        base64_code = base64.b64encode(bytecode).decode('utf-8')

        # Save the base64 encoded bytecode to a file
        base64_file_name = file_name.replace(".py", ".b64")
        with open(base64_file_name, 'w') as f:
            f.write(base64_code)
        
        print(f"Base64 encoded bytecode saved to {base64_file_name}")
    
    else:
        print("Invalid choice! Exiting...")
        exit()

# Run the function
get_code_and_compile()

    
    # Ask the user to input the Python code
    print("Enter your Python code. Press Ctrl+D (or Ctrl+Z on Windows) to finish input.")
    python_code = []
    
    try:
        # Taking multiline input from the user (until EOF)
        while True:
            line = input()
            python_code.append(line)
    except EOFError:
        pass
    
    # Join the list into a single string of code
    code_string = '\n'.join(python_code)

    # Save the code to the file
    with open(file_name, 'w') as f:
        f.write(code_string)
    
    print(f"Python code saved to {file_name}")

    # Compile the code into bytecode
    compiled_code = compile(code_string, file_name, 'exec')

    # Save the compiled code using marshal
    compiled_file_name = file_name.replace(".py", ".pyc")
    with open(compiled_file_name, 'wb') as f:
        marshal.dump(compiled_code, f)
    
    print(f"Compiled bytecode saved to {compiled_file_name}")

# Run the function
get_code_and_compile()
