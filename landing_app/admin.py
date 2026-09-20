from django.contrib import admin

from .models import (
    Enquiry, HeroSection, TrustStat, FleetSection, FleetVehicle,
    PackagesSection, TourPackage, ServicesSection, Service,
    WhyUsSection, WhyUsItem, DestinationsSection, Destination,
    StepsSection, Step, AboutSection, AboutChecklistItem,
    ReviewsSection, Review, GallerySection, GalleryImage,
    FAQSection, FAQItem, SiteSettings, ContactSection, CtaSection,
    FooterSection, FooterLink, FooterSocialLink,
)


@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ("copyright_text", "is_active")


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "column", "url", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("column",)
    ordering = ("column", "order")


@admin.register(FooterSocialLink)
class FooterSocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(CtaSection)
class CtaSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "phone", "whatsapp_number")


@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("heading_main", "heading_highlight", "is_active")


@admin.register(FleetSection)
class FleetSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(FleetVehicle)
class FleetVehicleAdmin(admin.ModelAdmin):
    list_display = ("name", "passengers", "bags", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(PackagesSection)
class PackagesSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "location_tag", "duration", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(WhyUsSection)
class WhyUsSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(WhyUsItem)
class WhyUsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(DestinationsSection)
class DestinationsSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(StepsSection)
class StepsSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


class AboutChecklistItemInline(admin.TabularInline):
    model = AboutChecklistItem
    extra = 1


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")
    inlines = [AboutChecklistItemInline]


@admin.register(ReviewsSection)
class ReviewsSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "rating", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(GallerySection)
class GallerySectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(FAQSection)
class FAQSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ("question", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(TrustStat)
class TrustStatAdmin(admin.ModelAdmin):
    list_display = ("label_top", "label_bottom", "icon", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "pickup_location", "destination", "phone_number",
        "source", "created_at",
    )
    list_filter = ("source", "vehicle_type", "created_at")
    search_fields = ("pickup_location", "destination", "phone_number", "name", "email")
    readonly_fields = [f.name for f in Enquiry._meta.fields]

    def has_add_permission(self, request):
        # Enquiries come from the website, not created manually in Admin
        return False