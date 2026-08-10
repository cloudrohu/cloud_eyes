from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField



class Setting(models.Model):

    site_name = models.CharField(max_length=150)

    logo = models.ImageField(upload_to='settings/',blank=True,null=True)

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

    ################ HOME CONTENT ################
    title = models.CharField(max_length=200,)
    subtitle = models.CharField(max_length=300, blank=True, null=True, help_text="Subtitle or tagline")
    content = RichTextUploadingField(blank=True, null=True,)
    read_legacy = RichTextUploadingField(blank=True, null=True,)
    image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Main image for About section")

    ################ ABOUT CONTENT ################
    about_title = models.CharField(max_length=200, blank=True, null=True,)
    about_subtitle = models.CharField(max_length=300, blank=True, null=True, help_text="Subtitle or tagline")
    about_content = RichTextUploadingField(blank=True, null=True,)

    ################ MISSION OR VISION CONTENT ################
    mission_title = models.CharField(max_length=200, blank=True, null=True)
    mission_content = RichTextUploadingField(blank=True, null=True,)
    vision_title = models.CharField(max_length=200, blank=True, null=True)
    vision_content = RichTextUploadingField(blank=True, null=True,)

    ################ ABOUT HERO CONTENT ################

    hero_title = models.CharField(max_length=250,blank=True,null=True,help_text="Main Hero Heading")
    hero_highlight = models.CharField(max_length=150,blank=True,null=True,help_text="Highlighted text in Hero Title")
    hero_subtitle = models.CharField(max_length=200,blank=True,null=True,help_text="Small heading above Hero Title")
    hero_description = RichTextUploadingField(blank=True,null=True,help_text="Hero description")
    hero_background = models.ImageField(upload_to='about/hero/',blank=True,null=True,help_text="Hero Background Image")
    button_one_text = models.CharField(max_length=50,default="Explore Legacy",blank=True,null=True)

    button_one_link = models.CharField(max_length=255,blank=True,null=True)

    button_two_text = models.CharField(max_length=50,default="View Projects",blank=True,null=True)

    button_two_link = models.CharField(max_length=255,blank=True,null=True)

    ################ SEO  CONTENT ################
    seo_title = models.CharField(max_length=200, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True, help_text="If disabled, this section won't appear on site")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    ################ IMAGES  CONTENT ################
    right_image1 = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Main image for About section")
    right_image2 = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Main image for About section")

    ################ STAT  CONTENT ################
    years_of_experience = models.CharField(max_length=100, blank=True, null=True)
    happy_families = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Section"
        ordering = ['-created_at']

    def __str__(self):
        return self.title