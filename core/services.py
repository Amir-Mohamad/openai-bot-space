def format_chat_history(history_queryset):
    messages = []
    for history in history_queryset:
        for detail in history.history_detail.all():
            messages.append({
                "role": detail.role,
                "content": detail.message
            })
    return {"messages": messages}