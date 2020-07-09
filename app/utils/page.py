from flask import request


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, *args, per_page=20, **kwargs):
        page = request.args.get('page', default=1)
        page_size = request.args.get('page_size', default=20)
        resources = query.paginate(page, page_size)
        data = {
            'items': [item.to_dict(*args, **kwargs) for item in resources.items],
            '_meta': {
                'page': page,
                'page_size': page_size,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
        }
        return data