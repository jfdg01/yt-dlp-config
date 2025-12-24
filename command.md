Run this command on cmd:

```cmd
yt-dlp -x --audio-format opus --audio-quality 0 ^
--force-ipv4 --limit-rate 5M ^
--sleep-requests 1.5 --min-sleep-interval 30 --max-sleep-interval 60 ^
--embed-thumbnail --embed-metadata --add-metadata ^
--parse-metadata "playlist_index:%(track_number)s" ^
--ppa "ThumbnailsConvertor+ffmpeg_o:-c:v png -vf crop=\"'if(gt(ih,iw),iw,ih)':'if(gt(iw,ih),ih,iw)'\"" ^
-P "D:\Music" ^
-o "%(playlist_title)U - [%(playlist_id)s]/%(track_number,playlist_index)02d - %(title)U.%(ext)s" ^
--download-archive "D:\yt-dlp-config\playlist_archive.txt" ^
"https://music.youtube.com/playlist?list=PLCNYGVveinBPrY0ZS2Hi59W1x39uAH2Y8"
```

Make sure the change the playlist URL (`"https://music.youtube.com/playlist?list=PLCNYGVveinBPrY0ZS2Hi59W1x39uAH2Y8"`), the output path (`-P "D:\Music"`)and the archive path (`--download-archive "D:\yt-dlp-config\playlist_archive.txt"`).--download-archive "D:\yt-dlp-config\playlist_archive.txt"

The archive path simply stores the already downloaded videos, so you don't have to download them again.

The files to be run should be:

```
D:\yt-dlp-config>dir
 Volume in drive D is D
 Volume Serial Number is 8202-3BA4

 Directory of D:\yt-dlp-config

24/12/2025  14:23    <DIR>          .
24/12/2025  14:23    <DIR>          ..
20/12/2025  12:18       119.244.248 deno.exe
22/12/2025  11:19       217.592.832 ffmpeg.exe
22/12/2025  11:19       217.387.008 ffprobe.exe
24/12/2025  15:03               987 playlist_archive.txt
24/12/2025  14:06           108.353 yt-dlp.exe
               5 File(s)    554.333.428 bytes
               2 Dir(s)  52.755.890.176 bytes free

D:\yt-dlp-config>
```

* get deno from [here](https://deno.land/)
* ffmpeg should be the "git-full" version from [here](https://www.gyan.dev/ffmpeg/builds/)
* yt-dlp should be the nighly version from [here](https://github.com/yt-dlp/yt-dlp-nightly-builds/releases).

It's recomended to add the folder to the path to run the command more comfortably, in this example it's `D:\yt-dlp-config`.