import asyncio
from datetime import datetime

import aiohttp
import isodate

from permissions.custom_errors import ApiError
from utils.converters import DiscordDatetime


async def get_youtube_video(
    session: aiohttp.ClientSession, api_key: str, url: str
) -> tuple[str, datetime, str, str]:
    """
    Get the title, created_at, duration, and thumbnail_url of a YouTube video.

    Returns:
    --------
    tuple
        - title (str): The title of the video.
        - created_at (str): The date and time the video was published.
        - duration (str): The duration of the video.
        - thumbnail_url (str): The URL of the thumbnail image.
    """
    # video_id = re.split(r"v=|youtu\.be/", url, maxsplit=1)[1]  # Extract the video ID from the URL.
    url = f"https://content-youtube.googleapis.com/youtube/v3/videos?id=Eh9mlbDAXtI&part=snippet,contentDetails&key={api_key}"

    try:
        async with session.get(url) as response:
            if response.status == 200:
                res = await response.json()
            else:
                raise ApiError(res)
    except (aiohttp.ClientConnectorError, asyncio.TimeoutError) as error:
        raise ApiError(str(error))

    title = res["items"][0]["snippet"]["title"]
    created_at = await DiscordDatetime.convert("_", time_string=res["items"][0]["snippet"]["publishedAt"])
    print(created_at)
    duration = isodate.parse_duration(res["items"][0]["contentDetails"]["duration"]).total_seconds()
    print(duration)
    thumbnail_url = res["items"][0]["snippet"]["thumbnails"]["maxres"]["url"]

    return title, created_at, duration, thumbnail_url
