from django.shortcuts import get_object_or_404, render

from .models import Material, Subject


def subject_list(request):
    subjects = Subject.objects.filter(is_active=True)

    return render(
        request,
        "learning/subject_list.html",
        {"subjects": subjects},
    )


def material_list(request, slug):
    subject = get_object_or_404(
        Subject,
        slug=slug,
        is_active=True,
    )

    materials = Material.objects.filter(
        subject=subject,
        is_published=True,
    )

    return render(
        request,
        "learning/material_list.html",
        {
            "subject": subject,
            "materials": materials,
        },
    )


def material_detail(request, slug):
    material = get_object_or_404(
        Material,
        slug=slug,
        is_published=True,
    )

    return render(
        request,
        "learning/material_detail.html",
        {"material": material},
    )