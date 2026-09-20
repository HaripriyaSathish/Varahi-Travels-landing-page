from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=150, default="Your Company Name")
    tagline = models.CharField(max_length=150, blank=True, help_text="e.g. TOURS & TRAVELS")
    logo = models.ImageField(upload_to="site/", blank=True, null=True)
    favicon = models.ImageField(upload_to="site/", blank=True, null=True)
    browser_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)

    phone = models.CharField(max_length=20, blank=True)
    whatsapp_number = models.CharField(
        max_length=20, blank=True, help_text="Digits only with country code, e.g. 919876543210"
    )
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    map_embed_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Website Settings"
        verbose_name_plural = "Website Settings"

    def __str__(self):
        return "Website Settings"

    def save(self, *args, **kwargs):
        self.pk = 1  # enforce a single row — there's only ever one site config
        super().save(*args, **kwargs)


class HeroSection(models.Model):
    location_label = models.CharField(
        max_length=100, default="MADURAI · TAMIL NADU · SOUTH INDIA"
    )
    heading_main = models.CharField(max_length=200, default="Explore South India With")
    heading_highlight = models.CharField(max_length=100, default="Comfort & Confidence")
    description = models.TextField(blank=True)
    button1_text = models.CharField(max_length=50, default="Book Your Ride")
    button1_link = models.CharField(max_length=300, default="#quick-enquiry")
    button2_text = models.CharField(max_length=50, default="Explore Packages")
    button2_link = models.CharField(max_length=300, default="#packages")

    # the three tick-mark trust badges under the buttons, e.g.
    # "Local expertise" / "Flexible itineraries" / "Direct support"
    trust_badge_1 = models.CharField(max_length=60, blank=True, default="Local expertise")
    trust_badge_2 = models.CharField(max_length=60, blank=True, default="Flexible itineraries")
    trust_badge_3 = models.CharField(max_length=60, blank=True, default="Direct support")

    background_image = models.ImageField(upload_to="hero/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Homepage Hero"
        verbose_name_plural = "Homepage Hero"

    def __str__(self):
        return "Homepage Hero"


class Enquiry(models.Model):
    SOURCE_CHOICES = [
        ("hero", "Hero Section - Quick Enquiry"),
        ("contact", "Contact Page Form"),
    ]
    VEHICLE_CHOICES = [
        ("mini", "Mini / Hatchback"),
        ("sedan", "Sedan"),
        ("suv", "SUV"),
        ("innova", "Innova"),
        ("innova_crysta", "Innova Crysta"),
        ("tempo", "Tempo Traveller"),
    ]

    pickup_location = models.CharField(max_length=150, blank=True)
    destination = models.CharField(max_length=150, blank=True)
    travel_date = models.DateField(null=True, blank=True)
    passengers = models.PositiveIntegerField(null=True, blank=True)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_CHOICES, blank=True)
    phone_number = models.CharField(max_length=15)

    # used by the separate Contact page form, optional for the hero quick-enquiry
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="hero")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Customer Enquiry"
        verbose_name_plural = "Customer Enquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.pickup_location or self.name} → {self.destination} ({self.get_source_display()})"


class TrustStat(models.Model):
    ICON_CHOICES = [
        ("heart", "Heart"),
        ("map", "Map"),
        ("headphones", "Headphones"),
        ("award", "Award / Medal"),
        ("car", "Car"),
    ]

    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default="heart")
    label_top = models.CharField(max_length=60, help_text="Small text above, e.g. 'Serving'")
    label_bottom = models.CharField(max_length=60, help_text="Bold text below, e.g. 'Travellers'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Trust Stat"
        verbose_name_plural = "Trust Stats (Serving Travellers row)"
        ordering = ["order"]

    def __str__(self):
        return f"{self.label_top} {self.label_bottom}"    

class FleetSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="RIDE YOUR WAY")
    heading = models.CharField(max_length=150, default="Our Comfortable Fleet")
    subtitle = models.CharField(
        max_length=250, blank=True,
        default="Choose a vehicle that fits your group, luggage and journey."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Fleet Section Heading"
        verbose_name_plural = "Fleet Section Heading"

    def __str__(self):
        return "Fleet Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class FleetVehicle(models.Model):
    image = models.ImageField(upload_to="fleet/", blank=True, null=True)
    name = models.CharField(max_length=100, help_text="e.g. Sedan, Innova Crysta")
    passengers = models.CharField(max_length=50, help_text="e.g. '4 passengers' or '6-7 passengers'")
    bags = models.CharField(max_length=50, help_text="e.g. '3 bags' or 'Group luggage'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Fleet Vehicle"
        verbose_name_plural = "Fleet Vehicles"
        ordering = ["order"]

    def __str__(self):
        return self.name    

class PackagesSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="CURATED JOURNEYS")
    heading = models.CharField(max_length=150, default="Popular Madurai Tour Packages")
    subtitle = models.CharField(
        max_length=250, blank=True,
        default="Discover carefully planned journeys across the most beautiful destinations in South India."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Packages Section Heading"
        verbose_name_plural = "Packages Section Heading"

    def __str__(self):
        return "Packages Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class TourPackage(models.Model):
    image = models.ImageField(upload_to="packages/", blank=True, null=True)
    duration = models.CharField(max_length=30, default="2 Days", help_text="e.g. '2 Days', '3 Days'")
    location_tag = models.CharField(max_length=150, help_text="e.g. 'MADURAI · RAMESHWARAM'")
    title = models.CharField(max_length=150, help_text="e.g. 'Madurai – Rameshwaram – 2 Days'")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tour Package"
        verbose_name_plural = "Tour Packages"
        ordering = ["order"]

    def __str__(self):
        return self.title    


class ServicesSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="WAYS TO TRAVEL")
    heading = models.CharField(max_length=150, default="Travel Services Designed Around You")
    subtitle = models.CharField(
        max_length=250, blank=True,
        default="From a quick city ride to a multi-day South India journey, every trip is thoughtfully arranged."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Services Section Heading"
        verbose_name_plural = "Services Section Heading"

    def __str__(self):
        return "Services Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Service(models.Model):
    ICON_CHOICES = [
        ("car", "Car"),
        ("route", "Route"),
        ("plane", "Plane"),
        ("map_pin", "Map Pin"),
        ("sparkles", "Sparkles"),
        ("users", "Users"),
    ]

    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default="car")
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    title = models.CharField(max_length=100, help_text="e.g. 'Local Cab Service'")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["order"]

    def __str__(self):
        return self.title    

class WhyUsSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="THE VISMI DIFFERENCE")
    heading = models.CharField(max_length=150, default="Why Travel With Us?")
    subtitle = models.CharField(
        max_length=250, blank=True,
        default="Thoughtful planning, reliable support and genuine local knowledge for every mile."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Why Us Section Heading"
        verbose_name_plural = "Why Us Section Heading"

    def __str__(self):
        return "Why Us Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class WhyUsItem(models.Model):
    ICON_CHOICES = [
        ("award", "Award"),
        ("car", "Car"),
        ("ticket", "Ticket"),
        ("map", "Map"),
        ("headphones", "Headphones"),
        ("shield", "Shield Check"),
        ("sparkles", "Sparkles"),
        ("navigation", "Navigation"),
    ]

    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default="award")
    title = models.CharField(max_length=100, help_text="e.g. 'Experienced Drivers'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Why Us Item"
        verbose_name_plural = "Why Us Items"
        ordering = ["order"]

    def __str__(self):
        return self.title    


class DestinationsSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="GO FURTHER")
    heading = models.CharField(max_length=150, default="Explore Popular Destinations")
    subtitle = models.CharField(
        max_length=250, blank=True,
        default="From sacred temple towns to misty hill stations and sunlit coastlines."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Destinations Section Heading"
        verbose_name_plural = "Destinations Section Heading"

    def __str__(self):
        return "Destinations Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Destination(models.Model):
    image = models.ImageField(upload_to="destinations/", blank=True, null=True)
    name = models.CharField(max_length=100, help_text="e.g. 'Madurai', 'Rameshwaram'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
        ordering = ["order"]

    def __str__(self):
        return self.name    

class StepsSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="SIMPLE BOOKING")
    heading = models.CharField(max_length=150, default="Your Journey, In Four Easy Steps")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Steps Section Heading"
        verbose_name_plural = "Steps Section Heading"

    def __str__(self):
        return "Steps Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Step(models.Model):
    ICON_CHOICES = [
        ("map_pin", "Map Pin"),
        ("car", "Car"),
        ("ticket", "Ticket"),
        ("palm", "Palm Tree"),
    ]

    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default="map_pin")
    title = models.CharField(max_length=100, help_text="e.g. 'Choose Your Destination'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Booking Step"
        verbose_name_plural = "Booking Steps"
        ordering = ["order"]

    def __str__(self):
        return self.title    


class AboutSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="ABOUT US")
    heading = models.CharField(max_length=200, default="Your Trusted Travel Partner in Madurai")
    paragraph_1 = models.TextField(
        blank=True,
        default=("Madurai Vismi Cabs is a Madurai-based travel service helping guests experience "
                  "South India with greater comfort and confidence. We arrange local cabs, airport "
                  "transfers, outstation travel and customized tour packages with a customer-first approach.")
    )
    paragraph_2 = models.TextField(
        blank=True,
        default=("Our local travel expertise, experienced drivers and comfortable vehicle options make "
                  "every journey feel simpler—from temple visits to family holidays and multi-day circuits.")
    )
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    badge_title = models.CharField(max_length=60, default="Madurai")
    badge_subtitle = models.CharField(max_length=100, default="Your South India gateway")
    button_text = models.CharField(max_length=50, default="Plan Your Trip")
    button_link = models.CharField(max_length=300, default="#quick-enquiry")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return "About Section"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class AboutChecklistItem(models.Model):
    about = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name="checklist_items")
    text = models.CharField(max_length=100, help_text="e.g. 'Local route knowledge'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About Checklist Item"
        verbose_name_plural = "About Checklist Items"
        ordering = ["order"]

    def __str__(self):
        return self.text    

class ReviewsSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="GUEST STORIES")
    heading = models.CharField(max_length=150, default="What Our Customers Say")
    subtitle = models.CharField(max_length=200, blank=True, default="Sample reviews shown for layout preview.")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reviews Section Heading"
        verbose_name_plural = "Reviews Section Heading"

    def __str__(self):
        return "Reviews Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Review(models.Model):
    RATING_CHOICES = [(i, f"{i} Stars") for i in range(1, 6)]

    name = models.CharField(max_length=100, help_text="e.g. 'Arun Kumar'")
    location = models.CharField(max_length=150, help_text="e.g. 'Madurai & Rameshwaram'")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    quote = models.TextField(help_text="The review text")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} — {self.rating} stars"

    @property
    def initials(self):
        parts = self.name.split()
        letters = "".join(p[0] for p in parts[:2] if p)
        return letters.upper()    

class GallerySection(models.Model):
    eyebrow = models.CharField(max_length=100, default="ON THE ROAD")
    heading = models.CharField(max_length=150, default="Travel Moments")
    subtitle = models.CharField(
        max_length=250, blank=True,
        default="A glimpse of the places, roads and experiences waiting across South India."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gallery Section Heading"
        verbose_name_plural = "Gallery Section Heading"

    def __str__(self):
        return "Gallery Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    caption = models.CharField(max_length=100, help_text="e.g. 'Our Fleet', 'Kodaikanal'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ["order"]

    def __str__(self):
        return self.caption    

class FAQSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="GOOD TO KNOW")
    heading = models.CharField(max_length=150, default="Frequently Asked Questions")
    subtitle = models.CharField(
        max_length=200, blank=True,
        default="Need help planning? Speak directly with our travel team."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ Section Heading"
        verbose_name_plural = "FAQ Section Heading"

    def __str__(self):
        return "FAQ Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class FAQItem(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ Item"
        verbose_name_plural = "FAQ Items"
        ordering = ["order"]

    def __str__(self):
        return self.question    

class ContactSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="START YOUR JOURNEY")
    heading = models.CharField(max_length=150, default="Plan Your Journey With Us")
    subtitle = models.CharField(
        max_length=250, blank=True,
        default="Tell us where you want to go. We'll help shape the right route, vehicle and travel plan."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact Section Heading"
        verbose_name_plural = "Contact Section Heading"

    def __str__(self):
        return "Contact Section Heading"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)    




class CtaSection(models.Model):
    eyebrow = models.CharField(max_length=100, default="THE ROAD IS WAITING")
    heading = models.CharField(max_length=150, default="Ready to Explore South India?")
    subtitle = models.CharField(
        max_length=250, blank=True,
        default="From temple trails to hill stations, let us make your journey comfortable and memorable."
    )
    background_image = models.ImageField(upload_to="cta/", blank=True, null=True)
    button1_text = models.CharField(max_length=50, default="Book Your Cab")
    button2_text = models.CharField(max_length=50, default="Chat on WhatsApp")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Final CTA Section"
        verbose_name_plural = "Final CTA Section"

    def __str__(self):
        return "Final CTA Section"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)        

class FooterSection(models.Model):
    description = models.TextField(
        blank=True,
        default="Comfortable cab services and thoughtfully customized South India journeys from Madurai."
    )
    tagline_note = models.CharField(max_length=150, blank=True, default="Journeys made personal in Madurai.")
    copyright_text = models.CharField(
        max_length=200, default="© 2026 Madurai Vismi Cabs. All rights reserved."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Footer Section"
        verbose_name_plural = "Footer Section"

    def __str__(self):
        return "Footer Section"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class FooterLink(models.Model):
    COLUMN_CHOICES = [
        ("quick_links", "Quick Links"),
        ("services", "Services"),
    ]

    column = models.CharField(max_length=20, choices=COLUMN_CHOICES, default="quick_links")
    label = models.CharField(max_length=60, help_text="e.g. 'Home', 'Local Cab'")
    url = models.CharField(
        max_length=200,
        help_text="Anchor to a section on this page, e.g. '#about', '#services', '#contact'"
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"
        ordering = ["order"]

    def __str__(self):
        return f"[{self.get_column_display()}] {self.label}"


class FooterSocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("youtube", "YouTube"),
        ("twitter", "Twitter / X"),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default="facebook")
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Footer Social Link"
        verbose_name_plural = "Footer Social Links"
        ordering = ["order"]

    def __str__(self):
        return self.get_platform_display()        