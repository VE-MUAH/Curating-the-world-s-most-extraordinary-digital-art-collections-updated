from django.core.management.base import BaseCommand
from app.models import Collection, Piece

class Command(BaseCommand):
    help = 'Populates the database with sample art pieces'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding database...'))

        # Get existing collections or creating a Default one if none exist
        collections = Collection.objects.all()
        if not collections:
            self.stdout.write(self.style.WARNING('No collections found. Creating "Modern Art" collection.'))
            default_coll = Collection.objects.create(
                collection_name="Modern Art",
                description="A curated selection of modern masterpieces.",
                collcover="https://images.unsplash.com/photo-1541963463532-d68292c34b19?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80"
            )
            collections = [default_coll]

        # Sample Pieces Data
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
            },
             {
                "title": "Mona Lisa",
                "artist": "Leonardo da Vinci",
                "type": "Oil on Poplar",
                "year": 1503,
                "piececover": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/800px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"
            },
             {
                "title": "Creation of Adam",
                "artist": "Michelangelo",
                "type": "Fresco",
                "year": 1512,
                "piececover": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg/1200px-Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg"
            }
        ]

        # Distribute pieces across collections
        import random
        
        count = 0
        for collection in collections:
            self.stdout.write(f'Checking collection "{collection.collection_name}"...')
            # Always add 3 random pieces to ensure they "find something"
            pieces_to_add = random.sample(sample_pieces, 3) 
            for p_data in pieces_to_add:
                Piece.objects.create(
                    collection=collection,
                    title=p_data['title'],
                    artist=p_data['artist'],
                    type=p_data['type'],
                    year=p_data['year'],
                    piececover=p_data['piececover']
                )
                count += 1


        self.stdout.write(self.style.SUCCESS(f'Successfully added {count} new pieces!'))
