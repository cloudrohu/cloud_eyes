from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField # Correct




class Setting(models.Model):

    site_name = models.CharField(max_length=150)

    logo = models.ImageField(upload_to='settings/',blank=True,null=True)

    why_choose_img = models.ImageField(upload_to='settings/',blank=True,null=True)

    favicon = models.ImageField(upload_to='settings/',blank=True,null=True)

    offer_img = models.ImageField(upload_to='settings/',blank=True,null=True)


    header_footer_color = models.CharField(max_length=150,blank=True)

    text_color = models.CharField(max_length=150,blank=True)

    button_color = models.CharField(max_length=150,blank=True)

    googletagmanager = models.CharField(max_length=150,blank=True)

    google_map = models.CharField(max_length=1000,blank=True)



    address = models.CharField(max_length=500,blank=True)

    phone = models.CharField(max_length=15,blank=True)

    whatsapp = models.CharField(max_length=15,blank=True)

    email = models.CharField(max_length=50,blank=True)

    working_days = models.CharField(max_length=100,blank=True,help_text="Example: Mon - Sat")

    working_hours = models.CharField(max_length=100,blank=True,help_text="Example: 10:00 AM - 6:00 PM")




    smtpserver = models.CharField(max_length=50,blank=True)

    smtpemail = models.CharField(max_length=50,blank=True)

    smtppassword = models.CharField(max_length=100,blank=True)

    smtpport = models.CharField(max_length=5,blank=True)




    meta_title = models.CharField(max_length=200,blank=True,null=True)

    meta_description = models.TextField(blank=True,null=True)

    meta_keywords = models.TextField(blank=True,null=True)

    footer_text = models.CharField(max_length=250,blank=True,null=True)

    copy_right = models.CharField(max_length=100,blank=True)

    privacy_policy = RichTextUploadingField(blank=True)

    terms_conditions = RichTextUploadingField(blank=True)

    disclaimer = RichTextUploadingField(blank=True)

    cookies = RichTextUploadingField(blank=True)


    facebook = models.CharField(max_length=50,blank=True)

    instagram = models.CharField(max_length=50,blank=True)

    twitter = models.CharField(max_length=50,blank=True)

    youtube = models.CharField(max_length=50,blank=True)


    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS
    )


    class Meta:
        verbose_name_plural = '0. Website Settings'


    def __str__(self):
        return self.site_name


    def logo_tag(self):

        if self.logo:

            return mark_safe(
                f'<img src="{self.logo.url}" width="100"/>'
            )

        return "(No Logo)"


    @property
    def logo_or_name(self):

        if self.logo and self.logo.name:
            return self.logo.url

        return None

class HeroSlider(models.Model):

    BADGE_COLOR_CHOICES = [
        ("sky", "Sky"),
        ("blue", "Blue"),
        ("cyan", "Cyan"),
        ("orange", "Orange"),
        ("green", "Green"),
        ("purple", "Purple"),
    ]

    title = models.CharField(max_length=200,help_text="Main heading of the slider")

    highlighted_text = models.CharField(max_length=100,blank=True,help_text="Text which will appear highlighted")

    description = models.TextField(blank=True)

    badge_text = models.CharField(max_length=100,blank=True)

    badge_color = models.CharField(max_length=20,choices=BADGE_COLOR_CHOICES,default="sky")

    image = models.ImageField(upload_to="hero-sliders/")

    background = models.CharField(max_length=200,default="from-sky-50 to-white",help_text="Tailwind gradient classes")

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Hero Slider"
        verbose_name_plural = "Hero Sliders"

    def __str__(self):
        return self.title


class HeroSliderButton(models.Model):

    BUTTON_STYLE_CHOICES = [
        ("primary", "Primary"),
        ("secondary", "Secondary"),
    ]

    slider = models.ForeignKey(HeroSlider,on_delete=models.CASCADE,related_name="buttons")

    text = models.CharField(max_length=100,help_text="Button text")

    url = models.CharField(max_length=500,help_text="Example: https://example.com, tel:+919999999999, mailto:info@example.com, #appointment")

    style = models.CharField(max_length=20,choices=BUTTON_STYLE_CHOICES,default="primary")

    icon = models.CharField(max_length=100,blank=True,help_text="Font Awesome class, e.g. fa-solid fa-calendar-check")

    open_new_tab = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.slider.title} - {self.text}"

class About(models.Model):

    search_bg = models.ImageField(upload_to='about/backgrounds/',blank=True, null=True,help_text="Background image for the top search banner (optional)")
    home_bg = models.ImageField(upload_to='about/backgrounds/',blank=True, null=True,help_text="Background image for home about section")

    title = models.CharField(max_length=200, help_text="Main heading (e.g., 'About Makaan Hub')")
    subtitle = models.CharField(max_length=300, blank=True, null=True, help_text="Subtitle or tagline")
    content = RichTextUploadingField(blank=True, null=True, help_text="Detailed About Us content with formatting")
    image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Main image for About section")


    who_we_are_title = models.CharField(max_length=200, default="Who We Are")
    who_we_are_subtitle = models.CharField(max_length=300, blank=True, null=True)
    who_we_are_description = RichTextUploadingField(blank=True, null=True, help_text="Description about company identity")

 
    our_mission_title = models.CharField(blank=True, null=True,max_length=200, default="Our Mission")
    our_mission = RichTextUploadingField(blank=True, null=True)
    our_vision_title = models.CharField(blank=True, null=True,max_length=200, default="Our Vision")
    our_vision = RichTextUploadingField(blank=True, null=True)

    looking_to_title = models.CharField(blank=True, null=True,max_length=200, help_text="Title for 'Looking To...' section")
    looking_to_description = RichTextUploadingField(blank=True, null=True)
    looking_to_button_text = models.CharField(max_length=50, default="Contact Us", help_text="Call-to-action button text")
    looking_to_button_link = models.URLField(blank=True, null=True, help_text="Button link (e.g., contact page)")

    meta_title = models.CharField(max_length=255, blank=True, null=True, help_text="SEO meta title")
    meta_description = models.TextField(blank=True, null=True, help_text="SEO meta description")
    meta_keywords = models.TextField(blank=True, null=True, help_text="SEO keywords separated by commas")

    is_active = models.BooleanField(default=True, help_text="If disabled, this section won't appear on site")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "2. About Section"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class USP(models.Model):
    title =  models.CharField(max_length=300,)
    description =  models.CharField(max_length=1000,)

    def __str__(self):
        return self.title

class why_choose(models.Model):
    title =  models.CharField(max_length=300,)
    description =  models.CharField(max_length=1000,)
    icon =  models.CharField(max_length=1000,)


    def __str__(self):
        return self.title

class technologies(models.Model):
    title =  models.CharField(max_length=300,)
    description =  models.CharField(max_length=1000,)
    image =  models.ImageField()


    def __str__(self):
        return self.title        