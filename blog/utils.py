def upload_post_image(instance, filename):
    extension = filename.split(".")[-1]
    return f'post/image/{"_".join(instance.title.lower().split(" "))}.{extension}'


def upload_blog_meta_data_image(instance, filename):
    return f'blogmetadata/image/{filename}'
