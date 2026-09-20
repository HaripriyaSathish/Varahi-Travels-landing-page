from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import EnquiryForm
from .models import (
    HeroSection, TrustStat, FleetSection, FleetVehicle,
    PackagesSection, TourPackage, ServicesSection, Service,
    WhyUsSection, WhyUsItem, DestinationsSection, Destination,
    StepsSection, Step, AboutSection, AboutChecklistItem,
    ReviewsSection, Review, GallerySection, GalleryImage,
    FAQSection, FAQItem, ContactSection, CtaSection,
    FooterSection, FooterLink, FooterSocialLink,
)


def index(request):
    context = {
        "hero": HeroSection.objects.filter(is_active=True).first(),
        "trust_stats": TrustStat.objects.filter(is_active=True).order_by("order"),
        "fleet_section": FleetSection.objects.first(),
        "fleet_vehicles": FleetVehicle.objects.filter(is_active=True).order_by("order"),
        "packages_section": PackagesSection.objects.first(),
        "tour_packages": TourPackage.objects.filter(is_active=True).order_by("order"),
        "services_section": ServicesSection.objects.first(),
        "services": Service.objects.filter(is_active=True).order_by("order"),
        "whyus_section": WhyUsSection.objects.first(),
        "whyus_items": WhyUsItem.objects.filter(is_active=True).order_by("order"),
        "destinations_section": DestinationsSection.objects.first(),
        "destinations": Destination.objects.filter(is_active=True).order_by("order"),
        "steps_section": StepsSection.objects.first(),
        "steps": Step.objects.filter(is_active=True).order_by("order"),
        "about": AboutSection.objects.first(),
        "about_checklist": AboutChecklistItem.objects.filter(is_active=True).order_by("order"),
        "reviews_section": ReviewsSection.objects.first(),
        "reviews": Review.objects.filter(is_active=True).order_by("order"),
        "gallery_section": GallerySection.objects.first(),
        "gallery_images": GalleryImage.objects.filter(is_active=True).order_by("order"),
        "faq_section": FAQSection.objects.first(),
        "faq_items": FAQItem.objects.filter(is_active=True).order_by("order"),
        "contact": ContactSection.objects.first(),
        "cta": CtaSection.objects.first(),
        "footer": FooterSection.objects.first(),
        "footer_quick_links": FooterLink.objects.filter(is_active=True, column="quick_links").order_by("order"),
        "footer_service_links": FooterLink.objects.filter(is_active=True, column="services").order_by("order"),
        "footer_socials": FooterSocialLink.objects.filter(is_active=True).order_by("order"),
    }
    return render(request, "landing/index.html", context)


def submit_enquiry(request):
    """
    Handles both the hero 'Quick Enquiry' form and the separate Contact
    page form. They post to the same endpoint; a hidden 'source' field
    tells us (and the notification email) which one was used.
    """
    if request.method != "POST":
        return redirect("/")

    form = EnquiryForm(request.POST)

    if form.is_valid():
        enquiry = form.save()
        source_label = enquiry.get_source_display()

        body_lines = [f"Source: {source_label}", ""]
        if enquiry.name:
            body_lines.append(f"Name: {enquiry.name}")
        if enquiry.email:
            body_lines.append(f"Email: {enquiry.email}")
        if enquiry.pickup_location:
            body_lines.append(f"Pickup: {enquiry.pickup_location}")
        if enquiry.destination:
            body_lines.append(f"Destination: {enquiry.destination}")
        if enquiry.travel_date:
            body_lines.append(f"Travel Date: {enquiry.travel_date}")
        if enquiry.passengers:
            body_lines.append(f"Passengers: {enquiry.passengers}")
        if enquiry.vehicle_type:
            body_lines.append(f"Vehicle: {enquiry.get_vehicle_type_display()}")
        body_lines.append(f"Phone: {enquiry.phone_number}")
        if enquiry.message:
            body_lines.append(f"Message: {enquiry.message}")

        send_mail(
            subject=f"New Enquiry — {source_label}",
            message="\n".join(body_lines),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.OWNER_EMAIL],
            fail_silently=False,
        )

        messages.success(request, "Thanks! We'll contact you shortly.")
        anchor = "quick-enquiry" if enquiry.source == "hero" else "contact"
        return redirect(f"/#{anchor}")

    messages.error(request, "Please check the highlighted fields and try again.")
    return redirect("/")