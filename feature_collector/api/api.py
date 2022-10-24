class API:
    def get_default_dict(self):
        """
        API요청을 위한 데이터 구조 반환
        """
        task_info = {
            "type": "",
            "url": "",
            "header": dict(),
            "data": dict(),
            "save_dir": "",
        }
        return task_info

    def get_converted_url(self, str):
        """
        URL 데이터의 / 와 \ 를 _로 치환
        """
        converted_url = str.replace("/", "_")
        converted_url = converted_url.replace("\/", "_")
        return converted_url
