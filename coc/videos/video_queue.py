class VideoQueue:
    def __init__(self):
        self.queue = []

    def add_video(self, video_id):
        self.queue.append(video_id)
        print(f"Video {video_id} added to the queue.")

    def remove_video(self, video_id):
        if video_id in self.queue:
            self.queue.remove(video_id)
            print(f"Video {video_id} removed from the queue.")

    def clear_queue(self):
        self.queue.clear()
        print("All videos have been removed from the queue.")

    def display_queue(self):
        print("Current Video Queue:")
        for idx, video_id in enumerate(self.queue, start=1):
            print(f"{idx}. Video ID: {video_id}")
