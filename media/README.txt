MEDIA FOLDER — साङ्ख्य सत्संग archive
=====================================

Drop your recovered recordings of the December 2006 telecast here.
The day pages are pre-wired to these exact filenames:

  day1-katha.mp4   day1-bhajan.mp3
  day2-katha.mp4   day2-bhajan.mp3
  day3-katha.mp4   day3-bhajan.mp3
  day4-katha.mp4   day4-bhajan.mp3
  day5-katha.mp4   day5-bhajan.mp3
  day6-katha.mp4   day6-bhajan.mp3
  day7-katha.mp4   day7-bhajan.mp3

Notes
-----
- MP4 (H.264 + AAC) plays in every browser. If your DVD rips are VOB/MPEG-2,
  convert with:  ffmpeg -i input.vob -c:v libx264 -crf 22 -c:a aac dayN-katha.mp4
- For multiple bhajans per day, add extra <audio> blocks in the day's HTML
  (copy the existing "media-block" div and change the filename).
- Large videos on Azure: consider uploading videos to the same Storage account
  in a separate "videos" container with public read access, and pointing the
  <source src> to that blob URL instead of bundling them with the site.
- Transcripts: paste directly into the "Transcript" media-block on each day page.
