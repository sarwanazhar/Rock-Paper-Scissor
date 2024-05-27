import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_file(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    print("\n")
    for index,video in enumerate(videos, start=1):
        print(f"{index}. Name: {video["name"]}. Duration:  {video["time"]}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name":name,"time":time})
    save_file(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number you want to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter new name: ")
        time = input("enter new time: ")
        videos[index-1] = {'name': name,'time': time}
        save_file(videos)
    else:
        print("invalid number")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_file(videos)
    else:
        print("invalid video index")
def main():
    videos = load_data() #yai array hoga
    while True:
        print("\n Youtube Manager | chose an option ")
        print("1. List all video ")
        print("2. Add a youtube video ")
        print("3. Update video detail ")
        print("4. Delete a youtube video ")
        print("5. Exit the App ")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()