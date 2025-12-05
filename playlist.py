def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

def add_song():
    title = input("Tên bài hát: ")
    artist = input("Tên ca sĩ: ")
    duration = int(input("Thời lượng (giây): "))

    song = {
        'title': title,
        'artist': artist,
        'duration': duration
    }

    songs.append(song)
    print("✔️ Đã thêm bài hát vào playlist.")

def view_playlist():
    if not songs:
        print("Playlist đang trống.")
        return

    print("\n--- DANH SÁCH PHÁT ---")
    for i, s in enumerate(songs, start=1):
        print(f"{i}. {s['title']} - {s['artist']} ({s['duration']}s)")

