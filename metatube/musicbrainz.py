# from flask import Request
import musicbrainzngs
from musicbrainzngs.musicbrainz import ResponseError
musicbrainzngs.set_useragent("metatube", "0.1")
def search(args):
    query = args['query']
    artist = args['artist']
    max = args['max']
    response = musicbrainzngs.search_releases(query, artist=artist, limit=max)
    print('Done with searching MBP \n')
    return response

def search_id_release(id):
    fields = ['artists', 'release-groups', 'recordings', 'isrcs', 'tags', 'media', 'artist-rels', 'labels', 'label-rels', 'work-level-rels', 'work-rels', 'genres']
    try:
        response = musicbrainzngs.get_release_by_id(id, includes=fields, release_type='album')
        return response
    except Exception as e:
        return str(e)

def search_id_recording(id):
    response = musicbrainzngs.search_recordings(rgid=id)
    return response

def search_id_release_group(id):
    try:
        release_group = musicbrainzngs.search_release_groups(rgid=id)
        release_cover = musicbrainzngs.get_release_group_image_list(id)
        response = {
            'release_group': release_group, 
            'release_cover': release_cover
        }
        return response
    except Exception as e:
        return str(e)
    
def get_cover(releaseid):
    try:
        return musicbrainzngs.get_image_list(releaseid)
    except ResponseError as e:
        return str(e.message)