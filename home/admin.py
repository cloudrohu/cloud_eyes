from django.contrib import admin
from .models import *


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):

    list_display = (
        'logo_tag',
        'site_name',
        'phone',
        'email',
        'working_days',
        'working_hours',
        'status',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'site_name',
        'phone',
        'email',
        'address',
    )

    readonly_fields = (
        'logo_tag',
    )

    fieldsets = (

        (
            'Website Information',
            {
                'fields': (
                    'site_name',
                    'logo',
                    'favicon',
                    'offer_img',
                )
            }
        ),



        (
            'Website Colors',
            {
                'fields': (
                    'header_footer_color',
                    'text_color',
                    'button_color',
                )
            }
        ),


        (
            'Contact Information',
            {
                'fields': (
                    'address',
                    'phone',
                    'whatsapp',
                    'email',
                    'google_map',
                )
            }
        ),

        (
            'Working Hours',
            {
                'fields': (
                    'working_days',
                    'working_hours',
                )
            }
        ),



        (
            'Google & Tracking',
            {
                'fields': (
                    'googletagmanager',
                )
            }
        ),



        (
            'SMTP Settings',
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'smtpserver',
                    'smtpemail',
                    'smtppassword',
                    'smtpport',
                )
            }
        ),



        (
            'SEO Settings',
            {
                'fields': (
                    'meta_title',
                    'meta_description',
                    'meta_keywords',
                )
            }
        ),


        (
            'Footer Settings',
            {
                'fields': (
                    'footer_text',
                    'copy_right',
                )
            }
        ),


        (
            'Legal Pages',
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'privacy_policy',
                    'terms_conditions',
                    'disclaimer',
                    'cookies',
                )
            }
        ),

        (
            'Social Media',
            {
                'fields': (
                    'facebook',
                    'instagram',
                    'twitter',
                    'youtube',
                )
            }
        ),


        (
            'Status',
            {
                'fields': (
                    'status',
                )
            }
        ),

    )


    @admin.display(
        description='Logo'
    )
    def logo_tag(self, obj):

        if obj.logo:

            return obj.logo_tag()

        return "(No Logo)"

class HeroSliderButtonInline(admin.TabularInline):
    model = HeroSliderButton
    extra = 1
    fields = (
        "text",
        "url",
        "style",
        "icon",
        "open_new_tab",
        "order",
        "is_active",
    )


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "badge_text",
        "order",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    list_filter = (
        "is_active",
        "badge_color",
    )

    search_fields = (
        "title",
        "highlighted_text",
        "description",
        "badge_text",
    )

    list_editable = (
        "order",
        "is_active",
    )

    ordering = (
        "order",
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Slider Content",
            {
                "fields": (
                    "title",
                    "highlighted_text",
                    "description",
                )
            },
        ),
        (
            "Badge",
            {
                "fields": (
                    "badge_text",
                    "badge_color",
                )
            },
        ),
        (
            "Slider Design",
            {
                "fields": (
                    "image",
                    "background",
                )
            },
        ),
        (
            "Settings",
            {
                "fields": (
                    "order",
                    "is_active",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),
    )

    inlines = [
        HeroSliderButtonInline,
    ]


@admin.register(HeroSliderButton)
class HeroSliderButtonAdmin(admin.ModelAdmin):

    list_display = (
        "text",
        "slider",
        "style",
        "url",
        "order",
        "is_active",
    )

    list_filter = (
        "style",
        "is_active",
        "open_new_tab",
    )

    search_fields = (
        "text",
        "url",
        "slider__title",
    )

    list_editable = (
        "order",
        "is_active",
    )

    ordering = (
        "slider",
        "order",
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = ("is_active",)
    search_fields = ("title", "meta_title", "meta_keywords")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (

        ("🏠 Main About", {
            "fields": (
                "title",
                "subtitle",
                "content",
                "image",
            )
        }),

        ("👥 Who We Are", {
            "fields": (
                "who_we_are_title",
                "who_we_are_subtitle",
                "who_we_are_description",
            )
        }),


        ("🎯 Mission & Vision", {
            "fields": (
                "our_mission_title",
                "our_mission",
                "our_vision_title",
                "our_vision",
            )
        }),

        ("💼 Looking To", {
            "fields": (
                "looking_to_title",
                "looking_to_description",
                "looking_to_button_text",
                "looking_to_button_link",
            )
        }),

        ("🌐 SEO", {
            "fields": (
                "meta_title",
                "meta_description",
                "meta_keywords",
            )
        }),

        ("⚙️ Background & Status", {
            "fields": (
                "home_bg",
                "search_bg",
                "is_active",
                "created_at",
                "updated_at",
            )
        }),
    )


