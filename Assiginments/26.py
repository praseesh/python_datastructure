# import sys

# def copy_input_with_spaces():
#     input_text = sys.stdin.read()
#     words = input_text.split()
#     output_text = ' '.join(words)
    
#     print(output_text)
    
# copy_input_with_spaces()

def copy_input_with_spaces(input_text):
    words = input_text.split()
    output_text = ' '.join(words)
    return output_text

input_text = "This is    some    text   with   multiple    spaces."
output_text = copy_input_with_spaces(input_text)
print(output_text)
