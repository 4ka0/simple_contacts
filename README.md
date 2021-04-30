# Simple Contacts

A simple contacts management app built using Django.

This was essentially a self-study project for me to learn about handling user-uploaded images at the backend (user profile images in this case).

I initially opted to use the django-imagekit library and, specifically, the SmartResize processor class to dynamically crop user-uploaded images without the user having to specify an anchor point for the cropping, which it apparently does this based on the entropy of the image.  However, this led to complexities regarding the backend storage (an AWS S3 bucket in this case) being accessed a large number of times and my free tier privileges quickly disappearing and the consequent need to set up cache.

So, I instead opted for a simpler approach which was to use Pillow.  Now, user-uploaded images are dynamically cropped by finding the largest square in the centre of the image and then resizing this to 200 x 200 pixels. This method seemed sufficient for my needs.

The django-cleanup app is also used to remove any images from the S3 bucket if they are no longer required.

### Built using:

* Python 3.7.9
* Django 3.1.6
* pillow 8.1.2
* django-crispy-forms 1.11.0
* django-storages 1.11.1
* django-cleanup 5.1.0
* environs 9.3.1
* Bootstrap 5.0.0-beta2
* Visual Studio Code 1.53.2
* macOS 10.15.7

### Screenshots:

#### List view:</br>
<img src="screenshot-1.png" width="600"></br>

#### Detail view:</br>
<img src="screenshot-2.png" width="600"></br>

#### Delete view:</br>
<img src="screenshot-3.png" width="600"></br>
