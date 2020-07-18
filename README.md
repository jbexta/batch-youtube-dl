# batch-youtube-dl
A little python3 script to download a batch of URLs read from a csv

Dependencies:
- youtube-dl

Replace the paths in the py file with your desired locations.

When adding a channel url to `batch.csv`, be sure they are in one of these formats:
- `youtube.com/<username>`
- `youtube.com/user/<username>`
The below format is the one youtube uses by default but it throws an error:
- `youtube.com/c/<username>`

Watch out for commas in the batch.csv description field!

Happy downloading :)
