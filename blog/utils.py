def upload_post_image(instance, filename):
    extension = filename.split(".")[-1]
    return f'post/image/{"_".join([str(instance.id)] + instance.title.lower().split(" "))}.{extension}'