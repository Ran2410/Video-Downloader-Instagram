import instaloader

x = input("Massukan Link Video: ")

shortcode = x.split('/')[-2] if x.endswith('/') else x.split('/')[-1]

L = instaloader.Instaloader(
    download_comments=False,
    download_geotags=False,
    download_pictures=False,
    download_video_thumbnails=False,
    save_metadata=False,
)

try:
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    if post.is_video:
        L.download_post(post, target="downloads")
        print("Video Berhasil di Unduh ke Folder 'downloads'")
    else:
        print("Link yang diberikan bukan video.")
except Exception as e:
    print(f"Terjadi Error {e}")
    print("Patikan link yang di berikan bukan akun private atau link yang salah.")
