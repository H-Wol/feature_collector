class API:
    def get_default_dict(self):
        task_info = {
            "type": "",
            "url": "",
            "header": dict(),
            "data": dict(),
            "save_dir": "",
        }
        return task_info

    def get_converted_url(self, str):
        converted_url = str.replace("/", "_")
        converted_url = converted_url.replace("\/", "_")
        return converted_url
