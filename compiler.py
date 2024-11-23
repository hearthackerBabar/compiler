import marshal
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

    # Compile the code into bytecode
    compiled_code = compile(code_string, file_name, 'exec')

    # Save the compiled code using marshal
    compiled_file_name = file_name.replace(".py", ".pyc")
    with open(compiled_file_name, 'wb') as f:
        marshal.dump(compiled_code, f)
    
    print(f"Compiled bytecode saved to {compiled_file_name}")

# Run the function
get_code_and_compile()
