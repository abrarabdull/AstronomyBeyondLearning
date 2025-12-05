from .models import ContactMessage

def new_messages_processor(request):
    if request.user.is_authenticated and request.user.is_staff:

        unread = ContactMessage.objects.filter(is_read=False).order_by("-created_at")

        return {
            "latest_message": unread.first(),    
            "unread_count": unread.count(),      
        }

    return {
        "latest_message": None,
        "unread_count": 0,
    }
