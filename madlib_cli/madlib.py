def read_template(path):
    with open(path) as text:
        return text.read().strip()

def parse_template(template):
    final_stripped_template = ""
    collection_of_parts = []
    current_part = ""
    capturing_part = False
    for char in template:
        if char == "{":
            final_stripped_template += char
            capturing_part = True
            current_part = ""
        elif char == "}":
            final_stripped_template += char
            capturing_part = False
            collection_of_parts.append(current_part)
        elif capturing_part:
            current_part += char
        else:
            final_stripped_template += char

    return final_stripped_template, tuple(collection_of_parts)
    

def merge(template,parts):
    merged = template.format(*parts)
    return merged

