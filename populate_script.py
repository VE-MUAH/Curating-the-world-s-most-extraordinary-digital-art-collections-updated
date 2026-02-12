from app.models import Collection, Piece
import random

sample_pieces = [
    {
        "title": "Starry Night",
        "artist": "Vincent van Gogh",
        "type": "Oil on Canvas",
        "year": 1889,
        "piececover": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
    },
    {
        "title": "The Persistence of Memory",
        "artist": "Salvador Dalí",
        "type": "Oil on Canvas",
        "year": 1931,
        "piececover": "https://upload.wikimedia.org/wikipedia/en/d/dd/The_Persistence_of_Memory.jpg"
    },
    {
        "title": "Girl with a Pearl Earring",
        "artist": "Johannes Vermeer",
        "type": "Oil on Canvas",
        "year": 1665,
        "piececover": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/1665_Girl_with_a_Pearl_Earring.jpg/800px-1665_Girl_with_a_Pearl_Earring.jpg"
    },
    {
        "title": "The Great Wave off Kanagawa",
        "artist": "Hokusai",
        "type": "Woodblock Print",
        "year": 1831,
        "piececover": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Great_Wave_off_Kanagawa2.jpg/1200px-Great_Wave_off_Kanagawa2.jpg"
    }
]

for c in Collection.objects.all():
    count = c.piece_set.count()
    print(f"Collection '{c.collection_name}' has {count} pieces.")
    if count == 0:
        print(f"Populating '{c.collection_name}'...")
        # Add random pieces
        for p in sample_pieces:
             Piece.objects.create(
                collection=c,
                title=p['title'],
                artist=p['artist'],
                type=p['type'],
                year=p['year'],
                piececover=p['piececover']
            )
print("Done.")
