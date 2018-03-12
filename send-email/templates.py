import os

def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not valid path")
    return file_path

def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

def render_context(template_string, context):
    return template_string


file_ = 'templates/email_msg.txt'
file_html = 'templates/email_msg.html'

template = get_template(file_)
template_html = get_template(file_html)
context = {

}

print(render_context(template, context))
print(render_context(template_html, context))
