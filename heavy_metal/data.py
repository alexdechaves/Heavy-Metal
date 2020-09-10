# DATA MANIPULATION


def map_asset_data(query_list):
    assets = []
    for asset in query_list:
        assets.append(
            {
                'id': asset.id,
                'title': asset.title,
                'filename': asset.filename,
                'path': asset.path,
                'status': asset.status
            }
        )
    return assets


def map_show_data(query_list):
    #  for single db object queries
    if not isinstance(query_list, list):
        return {
            'id': query_list.id,
            'show': query_list.show
        }

    # any other kind of query
    shows = []
    for show in query_list:
        shows.append(
            {
                'id': show.id,
                'show': show.show
            }
        )
    return shows