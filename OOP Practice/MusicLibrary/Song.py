
class Song:

    """This class is used to store Song's Data."""

    def __init__(self,title,artist,duration) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration


    def __str__(self) -> str:
        return (f"Title:    {self.title}\n"
                f"Artist:   {self.artist}\n"
                f"Duration: {self.duration}\n")