def upload_project_image(instance, filename):
    extension = filename.split(".")[-1]
    return f'project/image/{"_".join(instance.title.lower().split(" "))}.{extension}'
