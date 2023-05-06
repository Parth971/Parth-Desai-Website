def upload_skill_logo(instance, filename):
    extension = filename.split(".")[-1]
    return f'skills/logo/{"_".join(instance.name.lower().split(" "))}.{extension}'