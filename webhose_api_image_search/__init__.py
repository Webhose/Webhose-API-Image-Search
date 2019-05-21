import webhoseio


class WebhoseImage(object):

    def __init__(self, **kwargs):
        self.url = kwargs.get('url', None)
        self.uuid = kwargs.get('uuid', None)
        self.labels = kwargs.get('label', None)
        self.text = kwargs.get('text', None)
        self.thread_url = kwargs.get('thread_url', None)
        self.thread_title = kwargs.get('thread_title', None)
        self.meta_info = {}

    def get_meta_info(self):
        if not self.meta_info:
            if self.uuid:
                resp = webhoseio.query('images', {'q': 'uuid:{}'.format(self.uuid)})
                self.meta_info = resp['imageDocs'][0]
        return self.meta_info

    def __str__(self):
        return '\n'.join([self.thread_title, self.thread_url, ', '.join(self.labels)])


class ImageSearch(object):

    def __init__(self, token):
        webhoseio.config(token)

    def query(self, param_dict=None):
        return webhoseio.query('filterWebContent', param_dict)

    def get_images(self, label):
        images = []
        results = self.query({'q': 'image_label:({})'.format(label)})
        for post in results['posts']:
            for image in post['external_images']:
                if image['label'] and label in [l.lower() for l in image['label']]:
                    image['thread_url'] = post['thread']['url']
                    image['thread_title'] = post['thread']['title']
                    images.append(WebhoseImage(**image))
        return images



